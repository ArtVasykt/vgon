from django.contrib import admin
from vk.models import User


class UserModel(admin.ModelAdmin):
    exclude = ['pub_date']
    list_display = ('user_login', 'user_password', 'pub_date')


admin.site.register(User, UserModel)
