from django import forms
from django.contrib.auth.models import User
from .models import Task, TaskGroup

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'assigned_to', 'assigned_group']

    assigned_group = forms.ModelChoiceField(queryset=TaskGroup.objects.all(), required=False)

class TaskGroupForm(forms.ModelForm):
    class Meta:
        model = TaskGroup
        fields = ['name', 'director', 'staff_members']

    staff_members = forms.ModelMultipleChoiceField(queryset=User.objects.all(), required=False, widget=forms.CheckboxSelectMultiple)
