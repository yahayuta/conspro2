from django.db import models
from django_currentuser.db.models import CurrentUserField

# Create your models here.
class Type_Machine(models.Model):
    id = models.AutoField(verbose_name="機械分類ID", primary_key=True)
    name = models.CharField(verbose_name="機械分類名", max_length=256)
    creator = CurrentUserField(verbose_name="作成者", editable=False, related_name="create_type_machine")
    created = models.DateTimeField(verbose_name="作成日", auto_now_add=True)
    modifier = CurrentUserField(verbose_name="更新者", editable=False, related_name="update_type_machine", on_update=True, )
    modified = models.DateTimeField(verbose_name="更新日", auto_now=True)

    def __str__(self):
        return str(self.id) + ':' + self.name

    class Meta:
        verbose_name = "機械分類"
        verbose_name_plural = "機械分類"