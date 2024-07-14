from django.shortcuts import render
from .models import Task
from .serializers import TaskSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404



# Create your views here.
class TaskList(APIView):
    def get(self,request):
        try:
             tasks=Task.objects.all()
             serializer=TaskSerializer(tasks,many=True)
             return Response(serializer.data)
        except Exception as e:
             return Response(str(e),status=status.HTTP_500_INTERNAL_SERVER_ERROR)    

             
        
    
    def post(self,request):
        try:
            serializer=TaskSerializer(data=request.data)
            if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(str(e),status=status.HTTP_500_INTERNAL_SERVER_ERROR) 
        
class TaskUpdate(APIView):
     def get_object(self, pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:  
            raise Http404
        
                 
        
     def get(self,request,pk):
       try:  
         task=self.get_object(pk)
         serializer=TaskSerializer(task)
         return Response(serializer.data)
       except Exception as e:
            return Response(str(e),status=status.HTTP_500_INTERNAL_SERVER_ERROR)
     
     def put(self,request,pk):
       try:  
         task=self.get_object(pk)
         serializer=TaskSerializer(task,data=request.data)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data)
         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
       except Exception as e:
            return Response(str(e),status=status.HTTP_500_INTERNAL_SERVER_ERROR)
     
     def delete(self,request,pk):
        try: 
         task=self.get_object(pk)
         task.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(str(e),status=status.HTTP_500_INTERNAL_SERVER_ERROR)
         