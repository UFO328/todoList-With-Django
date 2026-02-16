from django.urls import path 
from .views import task_page,task_add,edit_task

app_name = "task_app"
urlpatterns = [
  path('task/',task_page,name='task_page'),
  path('add_task/',task_add,name='add_task'),
  path('edit_task/<int:id>/',edit_task,name='edit_task'),
  #path('registrasi/',registrasi,name='registrasi'),
  ]