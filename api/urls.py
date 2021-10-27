from django.urls import path
from . import views


urlpatterns = [
  path('', views.apiOverview, name='home'), 
  path('task-list/', views.taskList, name='tasklist'),
  path('task-detail/<str:pk>', views.taskDetail, name='taskdetail'),
]