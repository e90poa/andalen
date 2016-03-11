from django import forms

from models import Task



class TaskForm(forms.ModelForm):
    hej_hopp = forms.CharField(label='The hej hopp name', max_length=100)


    class Meta:
    	model = Task
    	fields = ['hej_hopp', 'name', 'completed']
    	exclude = ['date_created', 'date_modified']