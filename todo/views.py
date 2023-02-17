from rest_framework import generics
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer

class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskComplete(generics.UpdateAPIView):
    queryset = Task.objects.all()

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.completed = True
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class TaskIncomplete(generics.UpdateAPIView):
    queryset = Task.objects.all()

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.completed = False
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)