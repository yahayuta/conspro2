from django.db import models
from django.urls import reverse
from django_currentuser.db.models import CurrentUserField

# ステータス
STATUS = (
    ('1','1：見積'),
    ('2','2：作業'),
    ('3','3：請求'),
    ('0','0：完了'),
    ('9','9：取消'),
)

# Create your models here.
class Work(models.Model):
    id = models.AutoField(verbose_name="作業ID", primary_key=True)
    status = models.CharField(verbose_name="ステータス", choices=STATUS, max_length=3, default='1')
    name = models.CharField(verbose_name="作業名", blank=True, null=True, max_length=256)
    company = models.ForeignKey('Company',on_delete=models.SET_NULL, null=True, db_column='company_id', verbose_name="会社")
    machine_name = models.CharField(verbose_name="型式", max_length=256)
    serial_no = models.CharField(verbose_name="号機", blank=True, null=True, max_length=256)
    client = models.ForeignKey('Client',on_delete=models.SET_NULL, null=True, db_column='client_id', verbose_name="顧客")
    sum = models.IntegerField(verbose_name="明細計",default=0)
    adjust = models.IntegerField(verbose_name="調整額",default=0)
    total = models.IntegerField(verbose_name="総合計",default=0)
    memo = models.TextField(verbose_name="メモ", blank=True, null=True)
    creator = CurrentUserField(verbose_name="作成者", editable=False, related_name="create_work")
    created = models.DateTimeField(verbose_name="作成日", auto_now_add=True)
    modifier = CurrentUserField(verbose_name="更新者", editable=False, related_name="update_work", on_update=True, )
    modified = models.DateTimeField(verbose_name="更新日", auto_now=True)

    def __str__(self):
        return '会社:'+self.company.name+' ID:'+str(self.id)+' ステータス:'+self.get_status_display()+' 作業名:'+str(self.name)+' 型式:'+self.machine_name+' 号機:'+self.serial_no+' 顧客:'+self.client.name

    def get_absolute_url(self):
        return reverse('work_list')

    class Meta:
        verbose_name = "作業"
        verbose_name_plural = "作業"