from django.db import models
from django.urls import reverse
from django_currentuser.db.models import CurrentUserField

from main.models.inventory import Inventory

# Create your models here.
class InventoryOrderRow(models.Model):
    id = models.AutoField(verbose_name="明細ID", primary_key=True)
    inventory = models.ForeignKey(Inventory, related_name='inventory_id', on_delete=models.CASCADE)
    name = models.CharField(verbose_name="品目", max_length=256)
    count = models.IntegerField(verbose_name="数量",default=1)
    price = models.IntegerField(verbose_name="単価",default=0)
    total = models.IntegerField(verbose_name="合計",default=0)
    memo = models.CharField(verbose_name="備考欄", max_length=256, blank=True, null=True)
    is_out = models.BooleanField(verbose_name="出力", default=True)

    creator = CurrentUserField(verbose_name="作成者", editable=False, related_name="create_inventory_order_row")
    created = models.DateTimeField(verbose_name="作成日", auto_now_add=True)
    modifier = CurrentUserField(verbose_name="更新者", editable=False, related_name="update_inventory_order_row", on_update=True, )
    modified = models.DateTimeField(verbose_name="更新日", auto_now=True)

    def __str__(self):
        return str(self.inventory.name)+':'+str(self.inventory.serial_no)+':'+str(self.id)+':'+str(self.name)

    def get_absolute_url(self):
        return reverse('inventory_order_row_list')

    class Meta:
        verbose_name = "在庫注文明細"
        verbose_name_plural = "在庫注文明細"