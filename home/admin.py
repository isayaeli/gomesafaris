from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Park, Contact

admin.site.site_header = 'Gome Safaris Admin'
admin.site.site_title = "Gomesafaris Admin"

admin.site.unregister(Group)
admin.site.register(Park)
admin.site.register(Contact)