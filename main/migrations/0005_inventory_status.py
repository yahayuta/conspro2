# Generated by Django 3.2.19 on 2023-07-10 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20230701_0609'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='status',
            field=models.CharField(choices=[('0', '有効'), ('1', '締め'), ('9', '削除')], default='0', max_length=2, verbose_name='ステータス'),
        ),
    ]
