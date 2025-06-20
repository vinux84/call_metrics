from django.db import models
from django.contrib.auth.models import User 

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=200)
    date_creation = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'
    
class CallLog(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    log_date = models.DateField



























