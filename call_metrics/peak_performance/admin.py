from django.contrib import admin
from django.contrib.auth.models import User
from .models import Project, CallLog


admin.site.register(Project)
admin.site.register(CallLog)

