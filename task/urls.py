from django.urls import path 
from .views import task_page,task_add,edit_task,delete_task,succes_task,succes_task_page

app_name = "task_app"
urlpatterns = [
  path('task/',task_page,name='task_page'),
  path('add_task/',task_add,name='add_task'),
  path('edit_task/<int:id>/',edit_task,name='edit_task'),
  path('delete_task/<int:id>/',delete_task,name='delete_task'),
  path('succes_task_page/',succes_task_page,name='succes_task_page'),
  path('succes_task/<int:id>/',succes_task,name='succes_task'),
  ]