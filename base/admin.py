from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile
# Unregister groups
admin.site.unregister(Group)

# Mix profile info into user info
class ProfileInline(admin.StackedInline):
    model = Profile
    
# Extend User Model
class UserAdmin(admin.ModelAdmin):
    model = User
    #Just deisplay username fiels on admin page
    fields = ['username']
    inlines = [ProfileInline]
    
# Unregister initial User
admin.site.unregister(User)
# Register User
admin.site.register(User, UserAdmin)
# admin.site.register(Profile)

