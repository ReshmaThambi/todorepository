from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from todoapp.forms import TodoForm
from todoapp.models import Task


# Create your views here.
class TaskListView(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'task1'


class TaskDetailView(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'task'


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name', 'priority', 'date')


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbrhome')


def get_success_url(self):
    return reverse_lazy('cbrdetail', kwargs={'pk': self.object.id})


def add(request):
    task1 = Task.objects.all()
    if request.method == 'POST':
        name1 = request.POST.get('task', '')
        priority1 = request.POST.get('priority', '')
        date1 = request.POST.get('date', '')
        task = Task(name=name1, priority=priority1, date=date1)
        task.save()
    return render(request, 'home.html', {'task1': task1})


# def details(request):
#     task = Task.objects.all()
#     return render(request, 'details.html', {'task': task})


def delete(request, taskid):
    task = Task.objects.get(id=taskid)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request, 'delete.html')


def update(request, taskid):
    task = Task.objects.get(id=taskid)
    form1 = TodoForm(request.POST or None, instance=task)
    if form1.is_valid():
        form1.save()
        return redirect('/')
    return render(request, 'edit.html', {'form1': form1, 'task': task})
