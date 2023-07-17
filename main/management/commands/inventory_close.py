from main.models import Inventory

from django.core.management.base import BaseCommand

# 在庫締めバッチ
class Command(BaseCommand):
    
    def handle(self, *args, **options):
        filter_conditions = {
            'sell_month__isnull': False,
            'status': '0',
        }
        found_objects = Inventory.objects.filter(**filter_conditions)
        found_objects.update(status='1')
