# Generated by Django 4.2.2 on 2024-05-19 01:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_currentuser.db.models.fields
import django_currentuser.middleware


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0011_remove_client_pic1_remove_client_pic2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RentalOrder',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='レンタル注文ID')),
                ('hours_start', models.IntegerField(verbose_name='稼動時間開始時')),
                ('enrollment', models.CharField(max_length=256, verbose_name='在籍')),
                ('order_type', models.CharField(max_length=256, verbose_name='注文区分')),
                ('close_date', models.DateField(verbose_name='締め日')),
                ('out_date', models.DateField(verbose_name='出庫日')),
                ('in_date', models.DateField(verbose_name='返却日')),
                ('start_date', models.DateField(verbose_name='レンタル開始日')),
                ('end_date', models.DateField(verbose_name='レンタル終了日')),
                ('hours_end', models.IntegerField(verbose_name='稼動時間終了時')),
                ('memo', models.TextField(max_length=256, verbose_name='備考欄')),
                ('sum', models.IntegerField(default=0, verbose_name='明細計')),
                ('adjust', models.IntegerField(default=0, verbose_name='調整額')),
                ('total', models.IntegerField(default=0, verbose_name='総合計')),
                ('order_name', models.CharField(max_length=256, verbose_name='ユーザー名')),
                ('order_place', models.CharField(max_length=256, verbose_name='搬入先')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='作成日')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='更新日')),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='client', to='main.client', verbose_name='顧客')),
                ('company', models.ForeignKey(db_column='company_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.company', verbose_name='会社')),
                ('creator', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='create_rental_order', to=settings.AUTH_USER_MODEL, verbose_name='作成者')),
                ('modifier', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, on_update=True, related_name='update_rental_order', to=settings.AUTH_USER_MODEL, verbose_name='更新者')),
            ],
        ),
        migrations.AlterField(
            model_name='inventory',
            name='year',
            field=models.CharField(blank=True, max_length=16, null=True, verbose_name='年式'),
        ),
        migrations.AlterField(
            model_name='workrow',
            name='name',
            field=models.CharField(max_length=256, verbose_name='品目'),
        ),
        migrations.CreateModel(
            name='RentalOrderRow',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='明細ID')),
                ('name', models.CharField(max_length=256, verbose_name='品目')),
                ('count', models.IntegerField(default=1, verbose_name='数量')),
                ('price', models.IntegerField(default=0, verbose_name='単価')),
                ('total', models.IntegerField(default=0, verbose_name='合計')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='作成日')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='更新日')),
                ('creator', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='create_rental_order_row', to=settings.AUTH_USER_MODEL, verbose_name='作成者')),
                ('modifier', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, on_update=True, related_name='update_rental_order_row', to=settings.AUTH_USER_MODEL, verbose_name='更新者')),
                ('rental_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rental_order_id', to='main.rentalorder')),
            ],
            options={
                'verbose_name': '作業明細',
                'verbose_name_plural': '作業明細',
            },
        ),
        migrations.AddField(
            model_name='rentalorder',
            name='rental_inventory',
            field=models.ForeignKey(db_column='inventory_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.inventory', verbose_name='レンタル在庫'),
        ),
    ]