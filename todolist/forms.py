from todolist.models import Task
from django.forms import ModelForm

class taskForm(ModelForm):
    class Meta:
        model = Task
        fields = ('user', 'date', 'title', 'description')
        exclude = ['user', 'date']