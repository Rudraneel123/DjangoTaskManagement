from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=Task
        # fields='_all_'
        fields = ['id', 'title', 'description', 'completed', 'updated','created']
