from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Employee)
admin.site.register(Contract) 
admin.site.register(Document_type)
admin.site.register(Document)
admin.site.register(Permission_type)
admin.site.register(Permission)

