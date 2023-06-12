from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy

from todoapp.forms import TodoForm
from todoapp.models import Task
from django.views.generic import UpdateView, DeleteView
from django.views.generic.detail import DetailView


# generic view here.
#class TaskListview(ListView):
#    model = Task
##    template_name = "add_task.html"
#    context_object_name = 'task1'

class TaskDetailview(DetailView):
    model = Task
    template_name = "details.html"
    context_object_name = 'task'

class TaskUpdateview(UpdateView):
    model = Task
    template_name = "update.html"
    context_object_name = 'task'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('TaskDetailview',kwargs={'pk':self.object.id})

class TaskDeleteview(DeleteView):
    model = Task
    template_name = "delete.html"
    success_url= reverse_lazy('add')


# Create your views here.
def add(request):
     taskk=Task.objects.all()
     if request.method=="POST":
         name=request.POST.get('name',)
         priority =request.POST.get('priority',)
         date = request.POST.get('date',)
         task=Task(name=name,priority=priority,date=date)
         task.save()
     return render(request,"add_task.html",{'task1':taskk})

def done(request, id):
    task = Task.objects.get(id=id)
    if request.method == "POST":
        task.delete()
        return redirect('/')
    return render(request, "delete.html")


def update(request, id):
    task = Task.objects.get(id=id)
    f = TodoForm(request.POST or None, instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request, 'edit.html', {"form": f, "task": task})
