from django.db import models
from django_currentuser.db.models import CurrentUserField

# Create your models here.
class Notice(models.Model):
    id = models.AutoField(verbose_name="お知らせID", primary_key=True)
    notice = models.TextField(verbose_name="お知らせ内容", max_length=1000)
    creator = CurrentUserField(verbose_name="作成者", editable=False, related_name="create_notice")
    created = models.DateTimeField(verbose_name="作成日", auto_now_add=True)
    modifier = CurrentUserField(verbose_name="更新者", editable=False, related_name="update_notice", on_update=True, )
    modified = models.DateTimeField(verbose_name="更新日", auto_now=True)

    def __str__(self):
        return str(self.id) +':' + self.notice

    class Meta:
        verbose_name = "お知らせ"
        verbose_name_plural = "お知らせ"