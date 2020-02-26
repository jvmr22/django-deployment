from django.contrib import admin
from basic_app.models import UserProfile
from basic_app.forms import UserProfileForm

# Register your models here.
# admin.site.register(UserProfileForm)
admin.site.register(UserProfile)
