from django.contrib import admin

# Register your models here.
from .models import Company, Client, Maker, Type_Machine, Notice, Inventory

admin.site.register(Company)
admin.site.register(Client)
admin.site.register(Maker)
admin.site.register(Type_Machine)
admin.site.register(Notice)
admin.site.register(Inventory)

admin.site.site_header = 'CONSPRO2管理画面'
admin.site.index_title = 'マスター管理'

