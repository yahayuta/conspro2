from django.db import models
from django.urls import reverse
from django_currentuser.db.models import CurrentUserField

from main.models.work import Work

# ステータス
TYPE = (
    ('1','1：工賃'),
    ('2','2：部品'),
    ('3','3：費用'),
)

# Create your models here.
class WorkRow(models.Model):
    id = models.AutoField(verbose_name="明細ID", primary_key=True)
    work = models.ForeignKey(Work, related_name='work_id', on_delete=models.CASCADE)
    type = models.CharField(verbose_name="分類", choices=TYPE, max_length=3)
    name = models.CharField(verbose_name="品目", max_length=256)
    count = models.IntegerField(verbose_name="数量",default=1)
    price = models.IntegerField(verbose_name="単価",default=0)
    total = models.IntegerField(verbose_name="合計",default=0)
    parts_name = models.CharField(verbose_name="部品番", blank=True, null=True, max_length=256)
    parts_delivery_date = models.DateField(verbose_name="納品予定日", blank=True, null=True)
    client = models.ForeignKey('Client',on_delete=models.SET_NULL, blank=True, null=True, db_column='client_id', verbose_name="仕入先")
    memo = models.CharField(verbose_name="備考欄", max_length=256, blank=True, null=True)
    
    creator = CurrentUserField(verbose_name="作成者", editable=False, related_name="create_work_row")
    created = models.DateTimeField(verbose_name="作成日", auto_now_add=True)
    modifier = CurrentUserField(verbose_name="更新者", editable=False, related_name="update_work_row", on_update=True, )
    modified = models.DateTimeField(verbose_name="更新日", auto_now=True)

    def __str__(self):
        return str(self.work)+':'+str(self.id)+':'+str(self.name)+':'+str(self.client.name)

    def get_absolute_url(self):
        return reverse('work_row_list')

    class Meta:
        verbose_name = "作業明細"
        verbose_name_plural = "作業明細"