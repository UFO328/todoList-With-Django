from django.shortcuts import render,get_object_or_404,redirect
from .package import paginationList,paginationListSucces
from .models import Task
from django.contrib.auth.models import User


def task_page(request):
  page_obj = paginationList(request)
  return render(request,'task/task.html',{'page_obj':page_obj})

def task_add(request):
  if request.method == 'POST':
    tasks = request.POST.get('task')
    task = Task(
      user=request.user,
      task_name=tasks
      )
    task.save()
    return redirect('task_app:task_page')

def edit_task(request,id):
  if request.method == 'POST':
     tasks = request.POST.get('newTask')
     task = Task.objects.get(id=id)
     task.task_name = tasks 
     task.save()
     return redirect('task_app:task_page')

def delete_task(request,id):
  if request.method == 'POST':
     task = Task.objects.get(id=id)
     task.delete()
     return redirect('task_app:task_page')
     

def succes_task(request,id):
  if request.method == 'POST':
    task = Task.objects.get(id=id)
    task.is_completed = True
    task.save()
    return redirect('task_app:task_page')

def succes_task_page(request):
  page_obj = paginationListSucces(request)
  return render(request,'task/task_succes.html',{'page_obj':page_obj})