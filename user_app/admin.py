# Form을 장고 관리자 페이지에 적용
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserChangeForm, UserCreationForm
from .models import User

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('name', 'currentAddress','phone')
    list_filter = ('is_admin',)
    fieldsets=(
        (None,{'fields':('name','password')}),
        ('Personal info',{'fields':('phone','currentAddress')}),
        ('Permissions',{'fields':('is_admin',)}),
    )

    add_fieldsets=(
        (None,{
            'classes':('wide',),
            'fields':('name','currentAddress','phone','password1','password2')
        }),
    )

    search_fields=('name',)
    ordering=('name',)
    filter_horizontal=()

admin.site.register(User,UserAdmin)
admin.site.unregister(Group)

