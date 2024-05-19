# Generated by Django 4.2.2 on 2024-05-19 01:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0013_alter_rentalorderrow_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='仕入担当'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='buyer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='buyer_client', to='main.client', verbose_name='販売先'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='seller',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='seller_client', to='main.client', verbose_name='仕入先'),
        ),
        migrations.AlterField(
            model_name='workrow',
            name='client',
            field=models.ForeignKey(blank=True, db_column='client_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.client', verbose_name='仕入先'),
        ),
    ]