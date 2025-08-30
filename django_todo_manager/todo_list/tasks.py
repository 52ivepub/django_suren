from django.core.mail import send_mail
from .models import ToDoItem
from django.template.loader import render_to_string

def notify_admin_todo_archived(todo_id: int):
        todo = ToDoItem.objects.get(pk=todo_id)
        subject = f"ToDo # {todo.id} {todo.title!r} archived "
        message = ""
        context = {
            "todo": todo,
        }
        message_body = render_to_string(
            # x = "todo_list/templates/todo_list/todo-item-archived.txt"
            template_name="todo_list/todo-item-archived.txt",
            context=context 
            )
        send_mail(
        subject=subject,
        message=message_body,
        from_email="service@admin.com",
        recipient_list=["recipient@example.com"],
        fail_silently=False,
        )