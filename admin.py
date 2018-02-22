from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Profile


class ProfilInline(admin.StackedInline):
    model = Profile
    can_delete = False


class CustomUserAdmin(UserAdmin):
    inlines = (ProfilInline, )
    list_display = ('username', 'email','first_name', 'last_name', 'is_staff', 'get_province')
    #list_select_related = ('profile', )


    def get_province(self, instance):
        return instance.profile.get_province_display()
    get_province.short_description = 'Province'


    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request,obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
