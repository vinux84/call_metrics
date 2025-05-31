from django.db import models
from django.contrib.auth.models import User # importing our user model we have created already in views.py
import datetime

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, help_text='The name of the project')
    date_creation = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'
    
class CallLog(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    log_date = models.DateField



























