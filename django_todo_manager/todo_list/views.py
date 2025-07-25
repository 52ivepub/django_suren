import re
from django.shortcuts import render
from django.http import HttpRequest



def index_view(request: HttpRequest):
    todo_items = [
        "Item 1",
        "Item 2",
    ]
    return render(request=request,
                  template_name="todo_list/index.html",
                  context={"todo_items": todo_items},
                  )

