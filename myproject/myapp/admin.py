from django.contrib import admin

# Register your models here.
# admin.py

from django.contrib import admin
from .models import User, UserProfile

# Register your models here.

admin.site.register(User)
admin.site.register(UserProfile)
from .models import SalaryPrediction

# Register the SalaryPrediction model
admin.site.register(SalaryPrediction)