from django.contrib import admin

from hrms.models import Department, Level, Employee, Leave

admin.site.register(Department)
admin.site.register(Level)
admin.site.register(Employee)
admin.site.register(Leave)