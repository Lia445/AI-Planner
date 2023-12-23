from django.forms import ModelForm
from .models import Task

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'date', 'hours', 'group', 'plan']
        help_texts = {
            "title": "Required",
            "date": "Required",
        }
        

     
    
    
