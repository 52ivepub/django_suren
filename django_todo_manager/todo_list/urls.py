from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from .views import ToDoListView

app_name = "todo_list"

urlpatterns = [
    # path("", index_view, name='index'), 
    path("", ToDoListView.as_view(), name='index'), 
]
 