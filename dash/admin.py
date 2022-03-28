from django.contrib import admin
from .models import UserTracker, AdminTracker
# Register your models here.
admin.site.register(UserTracker)
admin.site.register(AdminTracker)