from django.db import models
from django_currentuser.db.models import CurrentUserField
from django.urls import reverse

# Create your models here.
class RentalOrder(models.Model):
    id = models.AutoField(verbose_name="レンタル注文ID", primary_key=True)
    rental_inventory = models.ForeignKey('Inventory', on_delete=models.SET_NULL, null=True, db_column='inventory_id', verbose_name="レンタル在庫")
    company = models.ForeignKey('Company', on_delete=models.SET_NULL, null=True, db_column='company_id', verbose_name="会社")
    hours_start = models.IntegerField(verbose_name="稼動時間開始時", blank=True, null=True)
    enrollment = models.CharField(verbose_name="在籍", blank=True, null=True, max_length=256)
    order_type = models.CharField(verbose_name="注文区分", blank=True, null=True, max_length=256)
    close_date = models.DateField(verbose_name="締め日", blank=True, null=True)
    out_date = models.DateField(verbose_name="出庫日", blank=True, null=True)
    in_date = models.DateField(verbose_name="返却日", blank=True, null=True)
    start_date = models.DateField(verbose_name="レンタル開始日", blank=True, null=True)
    end_date = models.DateField(verbose_name="レンタル終了日", blank=True, null=True)
    hours_end = models.IntegerField(verbose_name="稼動時間終了時", blank=True, null=True)
    client = models.ForeignKey('Client', on_delete=models.SET_NULL, blank=True, null=True, verbose_name="顧客", related_name="client")
    memo = models.TextField(verbose_name="備考欄", max_length=256, blank=True, null=True)
    sum = models.IntegerField(verbose_name="明細計",default=0)
    adjust = models.IntegerField(verbose_name="調整額",default=0)
    total = models.IntegerField(verbose_name="総合計",default=0)
    order_name = models.CharField(verbose_name="ユーザー名", max_length=256, blank=True, null=True)
    order_place = models.CharField(verbose_name="搬入先", max_length=256, blank=True, null=True)

    creator = CurrentUserField(verbose_name="作成者", editable=False, related_name="create_rental_order")
    created = models.DateTimeField(verbose_name="作成日", auto_now_add=True)
    modifier = CurrentUserField(verbose_name="更新者", editable=False, related_name="update_rental_order", on_update=True, )
    modified = models.DateTimeField(verbose_name="更新日", auto_now=True)

    def __str__(self):
        return str(self.id) +':' + self.rental_inventory.name

    def get_absolute_url(self):
        return reverse('rental_order_list')

    class Meta:
        verbose_name = "レンタル注文"
        verbose_name_plural = "レンタル注文"
