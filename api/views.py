from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Assignment
from .serializers import AssignmentSerializer
from .models import Assignment

# Create your views here.
@api_view(['GET'])
def  apiOverview(request):
  api_urls ={
    'List':'/task-list',
    'Detail view':'/task-detail/<str:pk>/',
    'Create':'/task-create/',
    'Update':'/task-update/<str:pk>/',
    'Delete':'/task-delete/<str:pk>/',
  }
 
  return Response(api_urls)

@api_view(['GET'])
def taskList(request):
  assignments=Assignment.objects.all()
  serializer=AssignmentSerializer(assignments,many=True) 
  return Response(serializer.data) 


@api_view(['GET'])
def taskDetail(request,pk):
  assignments=Assignment.objects.get(id=pk)
  serializer=AssignmentSerializer(assignments,many=False) 
  return Response(serializer.data) 


@api_view(['POST'])
def taskCreate(request):
  serializer=AssignmentSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()

  return Response(serializer.data) 

@api_view(['POST'])
def taskUpdate(request,pk):
  assignments=Assignment.objects.get(id=pk)
  serializer=AssignmentSerializer(instance=assignments, data=request.data)
  if serializer.is_valid():
    serializer.save()
    
  return Response(serializer.data)   
