from django import forms
from .models import ToDoItem

class ToDoItemCreateForm(forms.ModelForm):
    title = forms.CharField(
        max_length=250,
        widget=forms.Textarea(),
        )

    class Meta:
        model = ToDoItem
        fields = ("title", "description")
        widgets= {
            "title": forms.Textarea(attrs={"cols": 10, "rows": 5}),
            "description": forms.Textarea(attrs={"cols": 60, "rows": 10}),
            }
        help_texts = {
            "description": "Some useful help text",
        }



class ToDoItemUpdateForm(forms.ModelForm):
    class Meta(ToDoItemCreateForm.Meta):
        fields = (
            "title",
            "description",
            "done",
        )
