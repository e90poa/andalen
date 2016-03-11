from django.shortcuts import render

from models import Task
from forms import TaskForm

# Create your views here.
def index(request):

	form = TaskForm()

	if request.method == 'POST':

		form = TaskForm(request.POST)
		name = request.POST['name']
		task = Task(name=name)
		task.save()
		
	tasks = Task.objects.all()
	context = dict(
		tasks = tasks,
		form = form
	)
	return render(request, 'tasks/index.html', context)
