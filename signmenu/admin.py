from django.contrib import admin
from .models import User,DeleteUser

admin.site.register(User)
admin.site.register(DeleteUser)