from django import forms
from .models import ToDoItem

class ToDoItemForm(forms.ModelForm):
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
                                      
