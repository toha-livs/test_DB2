from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Post, Comments, Like

from .models import UserAll


class UserAllInline(admin.StackedInline):
    model = UserAll
    can_delete = False
    verbose_name_plural = 'userall'


class UserAdmin(UserAdmin):
    inlines = (UserAllInline, )


admin.site.register(Like)
admin.site.register(Post)
admin.site.register(Comments)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)