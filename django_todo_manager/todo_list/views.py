from celery.result import AsyncResult
from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.db import transaction

from .tasks import notify_admin_todo_archived
from .forms import ToDoItemCreateForm, ToDoItemUpdateForm
from .models import ToDoItem
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView



def index_view(request: HttpRequest):
    todo_items = ToDoItem.objects.all()[:3] 
    return render(request=request,
                  template_name="todo_list/index.html",
                  context={"todo_items": todo_items},
                  )


class ToDoDetailView(DetailView):
    # model = ToDoItem
    queryset = ToDoItem.objects.filter(archived=False)


class ToDoListIndexView(ListView):
    template_name = "todo_list/index.html"
    # TODO: custom queryset, archive
    queryset = ToDoItem.objects.all()[:3] 

    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["todo_items"] = ToDoItem.objects.all()
    #     return context

class ToDoListDoneView(ListView):
    queryset = ToDoItem.objects.filter(done=True).all() 



class ToDoListView(ListView):
    queryset = ToDoItem.objects.filter(archived=False)
    
    # def get_context_data(self, **kwargs):
    #     print(ToDoItem._meta.app_label)
    #     print(ToDoItem._meta.model_name)
    #     return super().get_context_data(**kwargs)

    
class ToDoItemCreateView(CreateView):
    model = ToDoItem
    form_class = ToDoItemCreateForm
    # fields= ("title", "description")


class ToDoItemUpdateView(UpdateView):
    model = ToDoItem
    template_name_suffix = "_update_form"
    form_class = ToDoItemUpdateForm


class ToDoItemDeleteView(DeleteView):
    model = ToDoItem
    success_url = reverse_lazy("todo_list:list")

    @transaction.atomic
    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.archived = True
        self.object.save()
        # notify_admin_todo_archived.delay(todo_id=self.object.pk)
        notify_admin_todo_archived.delay_on_commit(todo_id=self.object.pk)
        
        return HttpResponseRedirect(success_url)


def task_status(request: HttpRequest):
    task_id  =request.GET.get("task_id") or ""
    context = {"task_id":  task_id}
    result = AsyncResult(task_id)
    context.update(
        status=result.status,
        ready=result.ready,
    )
    return render(
        request,
        template_name="todo_list/task-status.html",
        context=context,

    )





