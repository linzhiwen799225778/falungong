from django.contrib import admin
from permission import models
# Register your models here.
admin.site.register(models.Permission)
admin.site.register(models.Role)
admin.site.register(models.User)