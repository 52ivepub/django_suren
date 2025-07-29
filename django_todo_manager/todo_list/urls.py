from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from .views import ToDoItemCreateView, ToDoListIndexView, ToDoListView, ToDoListDoneView, ToDoDetailView

app_name = "todo_list"

urlpatterns = [
    # path("", index_view, name='index'), 
    path("", ToDoListIndexView.as_view(), name='index'), 
    path("<int:pk>/", ToDoDetailView.as_view(), name='detail'), 
    path("list/", ToDoListView.as_view(), name='list'), 
    path("done/", ToDoListDoneView.as_view(), name='done'), 
    path("create/", ToDoItemCreateView.as_view(), name='create'), 
    
    
]
 