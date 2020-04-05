from django.shortcuts import render, redirect
from .models import TaskModel
from .forms import TaskForm, UpdateTaskForm
from django.utils import timezone

def TaskList(request):
	model = TaskModel.objects.all()

	form = TaskForm(request.POST)

	if request.method == "POST":
		if form.is_valid():
			new_task = form.save(commit=False)
			new_task.created_at = timezone.now
			new_task.complete = 0
			new_task.save()
			return redirect('TaskList')
		else:
			form = TaskForm


	context = {"model":model, "form":form}
	template = "task/index.html"

	return render(request, template, context)

def update(request, pk):
	model = TaskModel.objects.get(pk=pk)
	form = UpdateTaskForm(instance=model)

	if request.method == "POST":
		form = UpdateTaskForm(request.POST, instance=model)
		if form.is_valid():
			form.save()

			return redirect('TaskList')

	context = {"model":model, "form":form}
	template = "task/update.html"

	return render(request, template, context)


def delete(request, pk):
	model = TaskModel.objects.get(pk=pk)
	if request.method == "POST":
		model.delete()
		return redirect("TaskList")

	context = {"model":model}
	template = "task/delete.html"

	return render(request, template, context)