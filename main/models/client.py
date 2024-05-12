from django.db import models
from django_currentuser.db.models import CurrentUserField

# 業種区分
CLIENT_TYPE_CHOICES = (
    ('1','1：貿易'),
    ('2','2：オークション'),
    ('3','3：個人ブローカー'),
    ('4','4：新車ディーラー'),
    ('5','5：中古車ディーラー'),
    ('6','6：レンタル'),
    ('7','7：修理'),
    ('8','8：エンドユーザー'),
    ('9','9：その他'),
)

# 与信管理区分
CREDIT_TYPE_CHOICES = (
    ('A','A：入金前引渡OK'),
    ('B','B：入金後引渡'),
    ('C','C：問題あり'),
)

# Create your models here.
class Client(models.Model):
    id = models.AutoField(verbose_name="顧客ID", primary_key=True)
    client_type = models.CharField(verbose_name="業種", blank=True, null=True, choices=CLIENT_TYPE_CHOICES, max_length=3)
    credit_type = models.CharField(verbose_name="与信管理", blank=True, null=True, choices=CREDIT_TYPE_CHOICES, max_length=3)
    name = models.CharField(verbose_name="会社名", max_length=256)
    country_code = models.CharField(verbose_name="国番号", blank=True, null=True, max_length=16, default='81')
    zip = models.CharField(verbose_name="郵便番号", max_length=7)
    address = models.CharField(verbose_name="住所", max_length=256)
    tel = models.CharField(verbose_name="電話番号", max_length=16)
    fax = models.CharField(verbose_name="FAX番号", blank=True, null=True, max_length=16)
    email = models.EmailField(verbose_name="メールアドレス", blank=True, null=True)
    office = models.CharField(verbose_name="支店営業所名", blank=True, null=True, max_length=256)
    pic = models.CharField(verbose_name="担当", blank=True, null=True, max_length=256)
    memo = models.TextField(verbose_name="メモ", blank=True, null=True)
    creator = CurrentUserField(verbose_name="作成者", editable=False, related_name="create_client")
    created = models.DateTimeField(verbose_name="作成日", auto_now_add=True)
    modifier = CurrentUserField(verbose_name="更新者", editable=False, related_name="update_client", on_update=True, )
    modified = models.DateTimeField(verbose_name="更新日", auto_now=True)

    def __str__(self):
        return str(self.id) + ':' + self.name

    class Meta:
        verbose_name = "顧客"
        verbose_name_plural = "顧客"