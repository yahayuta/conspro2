# Generated by Django 4.2.2 on 2024-05-12 02:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_remove_inventory_other_remove_inventory_other_ja_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='pic1',
        ),
        migrations.RemoveField(
            model_name='client',
            name='pic2',
        ),
        migrations.RemoveField(
            model_name='client',
            name='pic3',
        ),
        migrations.RemoveField(
            model_name='client',
            name='pic4',
        ),
        migrations.RemoveField(
            model_name='client',
            name='pic5',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='buyer_name',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='seller_name',
        ),
        migrations.AddField(
            model_name='client',
            name='pic',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='担当'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='condition',
            field=models.CharField(choices=[('5', '5：新車もしくは、新車に近い状態'), ('4', '4：高年式・メーターの少ない極上品'), ('3', '3：現状で使用可能な状態'), ('2', '2：故障はしてないが、使用するには軽微な修理や整備が必要なもの'), ('1', '1：故障はしていないが、摩耗が激しく、使用するには相当の修理や整備が必要なもの'), ('B', 'B：エンジンや油圧系統など重要部品が故障しているもの')], default='5', max_length=2, verbose_name='程度'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='condition_maintenance',
            field=models.CharField(choices=[('1', '1：全塗装整備済み(Painted and Served)'), ('2', '2：整備済み(Served)'), ('3', '3：現状有姿(As is condition)')], default='1', max_length=2, verbose_name='整備状況'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='manufacturer',
            field=models.ForeignKey(db_column='maker_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.maker', verbose_name='メーカー'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='name',
            field=models.CharField(max_length=256, verbose_name='型式'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='price',
            field=models.IntegerField(default=0, verbose_name='表示価格'),
        ),
    ]
