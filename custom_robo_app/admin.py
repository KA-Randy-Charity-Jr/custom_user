from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from custom_robo_app.models import CustomRobo


admin.site.register(CustomRobo, UserAdmin)