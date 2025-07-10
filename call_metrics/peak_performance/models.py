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
    call_id = models.BigAutoField(primary_key=True)
    call_status = models.BooleanField(null=False, blank=False)
    requires_callback = models.BooleanField(default=False)
    callback_number = models.CharField(max_length=4, blank=True, null=True)
    log_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        status_text = "Successful" if self.call_status else "Unsuccessful"
        callback_info = ""
        if self.requires_callback:
            callback_info = f" - Callback (Ext: {self.callback_number or 'N/A'})"
        return f'Call ID: {self.call_id} for {self.project.name} on {self.log_date.strftime("%Y-%m-%d %H:%M")} - {status_text}{callback_info}'



























