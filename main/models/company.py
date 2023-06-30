from django.db import models
from django_currentuser.db.models import CurrentUserField

# Create your models here.
class Company(models.Model):
    id = models.AutoField(verbose_name="会社ID", primary_key=True)
    name = models.CharField(verbose_name="会社名", max_length=256)
    zip = models.CharField(verbose_name="郵便番号", max_length=7)
    address = models.CharField(verbose_name="住所", max_length=256)
    tel = models.CharField(verbose_name="電話番号", max_length=16)
    fax = models.CharField(verbose_name="FAX番号", blank=True, null=True, max_length=16)
    email = models.EmailField(verbose_name="メールアドレス", blank=True, null=True)
    ceo_name = models.CharField(verbose_name="代表名", blank=True, null=True, max_length=256)
    registration_number = models.CharField(verbose_name="インボイス登録番号", blank=True, null=True, max_length=256)
    name_en = models.CharField(verbose_name="英語会社名", max_length=256)
    address_en = models.CharField(verbose_name="英語住所", max_length=256)
    tel_en = models.CharField(verbose_name="英語電話番号", max_length=16)
    fax_en = models.CharField(verbose_name="英語FAX番号", blank=True, null=True, max_length=16)
    creator = CurrentUserField(verbose_name="作成者", editable=False, related_name="create_company")
    created = models.DateTimeField(verbose_name="作成日", auto_now_add=True)
    modifier = CurrentUserField(verbose_name="更新者", editable=False, related_name="update_company", on_update=True, )
    modified = models.DateTimeField(verbose_name="更新日", auto_now=True)

    def __str__(self):
        return str(self.id) + ':' + self.name

    class Meta:
        verbose_name = "会社"
        verbose_name_plural = "会社"