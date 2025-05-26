from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile, Project

admin.site.register(Profile)
admin.site.register(Project)

# mix profile info and user info
class ProfileInline(admin.StackedInline):
    model = Profile

# extend user model
class UserAdmin(admin.ModelAdmin):
    model = User
    field = ['username', 'first_name', 'last_name', 'email']
    inlines = [ProfileInline]

# unregiser old way
admin.site.unregister(User)

#re-regsiter
admin.site.register(User, UserAdmin)