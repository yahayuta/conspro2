# Generated by Django 4.2.2 on 2024-05-19 01:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_rentalorder_alter_inventory_year_alter_workrow_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rentalorderrow',
            options={'verbose_name': 'レンタル注文明細', 'verbose_name_plural': 'レンタル注文明細'},
        ),
        migrations.AlterField(
            model_name='rentalorder',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='client', to='main.client', verbose_name='顧客'),
        ),
        migrations.AlterField(
            model_name='rentalorder',
            name='close_date',
            field=models.DateField(blank=True, null=True, verbose_name='締め日'),
        ),
        migrations.AlterField(
            model_name='rentalorder',
            name='end_date',
            field=models.DateField(blank=True, null=True, verbose_name='レンタル終了日'),
        ),
        migrations.AlterField(
            model_name='rentalorder',
            name='enrollment',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='在籍'),
        ),
        migrations.AlterField(
            model_name='rentalorder',
            name='hours_end',
            field=models.IntegerField(blank=True, null=True, verbose_name='稼動時間終了時'),
        ),
        migrations.AlterField(
            model_name='rentalorder',
            name='hours_start',
            field=models.IntegerField(blank=True, null=True, verbose_name='稼動時間開始時'),
        ),
        migrations.AlterField(
            model_name='rentalorder',
            name='in_date',
            field=models.DateField(blank=True, null=True, verbose_name='返却日'),
        ),
        migrations.AlterField(
            model_name='rentalorder',
            name='memo',
            field=models.TextField(blank=True, max_length=256, null=True, verbose_name='備考欄'),
        ),
        migrations.AlterField(
            model_name='rentalorder',
            name='order_name',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='ユーザー名'),
        ),
        migrations.AlterField(
            model_name='rentalorder',
            name='order_place',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='搬入先'),
        ),
        migrations.AlterField(
            model_name='rentalorder',
            name='order_type',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='注文区分'),
        ),
        migrations.AlterField(
            model_name='rentalorder',
            name='out_date',
            field=models.DateField(blank=True, null=True, verbose_name='出庫日'),
        ),
        migrations.AlterField(
            model_name='rentalorder',
            name='start_date',
            field=models.DateField(blank=True, null=True, verbose_name='レンタル開始日'),
        ),
    ]