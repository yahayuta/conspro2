from django.db import models
from django_currentuser.db.models import CurrentUserField

# Create your models here.
class Maker(models.Model):
    id = models.AutoField(verbose_name="メーカーID", primary_key=True)
    name = models.CharField(verbose_name="メーカー名", max_length=256)
    creator = CurrentUserField(verbose_name="作成者", editable=False, related_name="create_maker")
    created = models.DateTimeField(verbose_name="作成日", auto_now_add=True)
    modifier = CurrentUserField(verbose_name="更新者", editable=False, related_name="update_maker", on_update=True, )
    modified = models.DateTimeField(verbose_name="更新日", auto_now=True)

    def __str__(self):
        return str(self.id) +':' + self.name

    class Meta:
        verbose_name = "メーカー"
        verbose_name_plural = "メーカー"