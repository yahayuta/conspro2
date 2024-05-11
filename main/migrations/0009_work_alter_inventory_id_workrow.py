# Generated by Django 4.2.2 on 2024-05-11 05:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_currentuser.db.models.fields
import django_currentuser.middleware


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0008_auto_20230912_2213'),
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='作業ID')),
                ('status', models.CharField(choices=[('1', '1：見積'), ('2', '2：作業'), ('3', '3：請求'), ('0', '0：完了'), ('9', '9：取消')], default='1', max_length=3, verbose_name='ステータス')),
                ('name', models.CharField(blank=True, max_length=256, null=True, verbose_name='作業名')),
                ('machine_name', models.CharField(max_length=256, verbose_name='型式')),
                ('serial_no', models.CharField(blank=True, max_length=256, null=True, verbose_name='号機')),
                ('sum', models.IntegerField(default=0, verbose_name='明細計')),
                ('adjust', models.IntegerField(default=0, verbose_name='調整額')),
                ('total', models.IntegerField(default=0, verbose_name='総合計')),
                ('memo', models.TextField(blank=True, null=True, verbose_name='メモ')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='作成日')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='更新日')),
                ('client', models.ForeignKey(db_column='client_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.client', verbose_name='顧客')),
                ('company', models.ForeignKey(db_column='company_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.company', verbose_name='会社')),
                ('creator', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='create_work', to=settings.AUTH_USER_MODEL, verbose_name='作成者')),
                ('modifier', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, on_update=True, related_name='update_work', to=settings.AUTH_USER_MODEL, verbose_name='更新者')),
            ],
            options={
                'verbose_name': '作業',
                'verbose_name_plural': '作業',
            },
        ),
        migrations.AlterField(
            model_name='inventory',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='在庫ID'),
        ),
        migrations.CreateModel(
            name='WorkRow',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='明細ID')),
                ('type', models.CharField(choices=[('1', '1：工賃'), ('2', '2：部品'), ('3', '3：費用')], max_length=3, verbose_name='分類')),
                ('name', models.CharField(max_length=256, verbose_name='品名')),
                ('count', models.IntegerField(default=1, verbose_name='数量')),
                ('price', models.IntegerField(default=0, verbose_name='単価')),
                ('total', models.IntegerField(default=0, verbose_name='合計')),
                ('parts_name', models.CharField(blank=True, max_length=256, null=True, verbose_name='部品番')),
                ('parts_delivery_date', models.DateField(blank=True, null=True, verbose_name='納品予定日')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='作成日')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='更新日')),
                ('client', models.ForeignKey(db_column='client_id', default='1', null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.client', verbose_name='仕入先')),
                ('creator', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='create_work_row', to=settings.AUTH_USER_MODEL, verbose_name='作成者')),
                ('modifier', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, on_update=True, related_name='update_work_row', to=settings.AUTH_USER_MODEL, verbose_name='更新者')),
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='work_id', to='main.work')),
            ],
            options={
                'verbose_name': '作業明細',
                'verbose_name_plural': '作業明細',
            },
        ),
    ]
