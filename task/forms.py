from django import forms
from .models import TaskModel

class TaskForm(forms.ModelForm):
	class Meta:
		model = TaskModel
		fields = ["task"]


class UpdateTaskForm(forms.ModelForm):
	class Meta:
		model = TaskModel
		fields = ["task", "complete"]