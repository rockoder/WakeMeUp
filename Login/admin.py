from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from login.models import UserProfile, Quote, Log

# Refer: https://docs.djangoproject.com/en/1.5/topics/auth/customizing/#extending-the-existing-user-model
class UserProfileInline(admin.StackedInline):
    model = UserProfile

class UserAdmin(UserAdmin):
    inlines = (UserProfileInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Quote)
admin.site.register(Log)