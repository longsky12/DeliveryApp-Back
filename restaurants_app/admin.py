from django.contrib import admin
from .models import Restaurant,Menu,MenuOption, Dib

admin.site.register(Restaurant)
admin.site.register(Menu)
admin.site.register(MenuOption)
admin.site.register(Dib)