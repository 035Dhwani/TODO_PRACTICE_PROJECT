from django.contrib import admin

from .models import role,department,employee

# Register your models here.
admin.site.register(role)
admin.site.register(department)
admin.site.register(employee)
