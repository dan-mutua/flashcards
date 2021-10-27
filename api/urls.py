from django.urls import path
from . import views


urlpatterns = [
  path('', views.apiOverview, name='home'), 
  path('task-list/', views.taskList, name='tasklist'),
  path('task-detail/<str:pk>/', views.taskDetail, name='taskdetail'),
  path('task-create/', views.taskCreate, name='taskcreate'),
  path('task-update/', views.taskUpdate, name='taskupdate'),
]