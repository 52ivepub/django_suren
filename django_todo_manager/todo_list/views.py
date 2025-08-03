from django.shortcuts import render
from django.http import HttpRequest
from django.urls import reverse, reverse_lazy
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
    model = ToDoItem


class ToDoListIndexView(ListView):
    template_name = "todo_list/index.html"
    queryset = ToDoItem.objects.all()[:3] 

    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["todo_items"] = ToDoItem.objects.all()
    #     return context

class ToDoListDoneView(ListView):
    queryset = ToDoItem.objects.filter(done=True).all() 



class ToDoListView(ListView):
    model = ToDoItem
    
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

    



