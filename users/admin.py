from django.contrib import admin

from users.models import User, Profile


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'username', 'email', 'city', 'gender', 'user_type')
    list_filter = ('gender', 'user_type', 'city',)
    search_fields = ('username', 'city', 'gender', 'user_type')


admin.site.register(User, UserAdmin)
admin.site.register(Profile)
