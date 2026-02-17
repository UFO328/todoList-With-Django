from django.shortcuts import render,get_object_or_404,redirect
from .package import paginationList,paginationListSucces
from .models import Task
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def task_page(request):
  page_obj = paginationList(request)
  return render(request,'task/task.html',{'page_obj':page_obj})

@login_required
def task_add(request):
  if request.method == 'POST':
    tasks = request.POST.get('task')
    task = Task(
      user=request.user,
      task_name=tasks
      )
    task.save()
    return redirect('task_app:task_page')
    
@login_required
def edit_task(request,id):
  if request.method == 'POST':
     tasks = request.POST.get('newTask')
     task = Task.objects.get(id=id)
     task.task_name = tasks 
     task.save()
     return redirect('task_app:task_page')

@login_required
def delete_task(request,id):
  if request.method == 'POST':
     task = Task.objects.get(id=id)
     task.delete()
     return redirect('task_app:task_page')
     
@login_required
def succes_task(request,id):
  if request.method == 'POST':
    task = Task.objects.get(id=id)
    task.is_completed = True
    task.save()
    return redirect('task_app:task_page')

@login_required
def succes_task_page(request):
  page_obj = paginationListSucces(request)
  return render(request,'task/task_succes.html',{'page_obj':page_obj})