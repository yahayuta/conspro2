# Generated by Django 3.2.19 on 2023-07-10 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_inventory_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='status',
            field=models.CharField(choices=[('0', '有効在庫'), ('1', '締め在庫'), ('5', 'その他在庫'), ('6', '削除その他在庫'), ('9', '削除在庫')], default='0', max_length=2, verbose_name='ステータス'),
        ),
    ]
