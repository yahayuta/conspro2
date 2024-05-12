from django.contrib import admin

# Register your models here.
from .models import Company, Client, Maker, Type_Machine, Notice, Inventory, Work, WorkRow

admin.site.register(Company)
admin.site.register(Client)
admin.site.register(Maker)
admin.site.register(Type_Machine)
admin.site.register(Notice)
admin.site.register(Inventory)
admin.site.register(Work)
admin.site.register(WorkRow)

admin.site.site_header = '管理画面'
admin.site.index_title = 'マスター管理'

