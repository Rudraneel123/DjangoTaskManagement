from django.db import models

# Create your models here.
class Task(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField(blank=True,max_length=255)
    completed=models.BooleanField(default=False)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title