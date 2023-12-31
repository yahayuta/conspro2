# Generated by Django 3.2.19 on 2023-06-18 12:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_currentuser.db.models.fields
import django_currentuser.middleware


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Type_Machine',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='機械分類ID')),
                ('name', models.CharField(max_length=256, verbose_name='機械分類名')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='作成日')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='更新日')),
                ('creator', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='create_type_machine', to=settings.AUTH_USER_MODEL, verbose_name='作成者')),
                ('modifier', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, on_update=True, related_name='update_type_machine', to=settings.AUTH_USER_MODEL, verbose_name='更新者')),
            ],
            options={
                'verbose_name': '機械分類',
                'verbose_name_plural': '機械分類',
            },
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='お知らせID')),
                ('notice', models.TextField(max_length=1000, verbose_name='お知らせ内容')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='作成日')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='更新日')),
                ('creator', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='create_notice', to=settings.AUTH_USER_MODEL, verbose_name='作成者')),
                ('modifier', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, on_update=True, related_name='update_notice', to=settings.AUTH_USER_MODEL, verbose_name='更新者')),
            ],
            options={
                'verbose_name': 'お知らせ',
                'verbose_name_plural': 'お知らせ',
            },
        ),
        migrations.CreateModel(
            name='Maker',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='メーカーID')),
                ('name', models.CharField(max_length=256, verbose_name='メーカー名')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='作成日')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='更新日')),
                ('creator', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='create_maker', to=settings.AUTH_USER_MODEL, verbose_name='作成者')),
                ('modifier', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, on_update=True, related_name='update_maker', to=settings.AUTH_USER_MODEL, verbose_name='更新者')),
            ],
            options={
                'verbose_name': 'メーカー',
                'verbose_name_plural': 'メーカー',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='会社ID')),
                ('name', models.CharField(max_length=256, verbose_name='会社名')),
                ('zip', models.CharField(max_length=7, verbose_name='郵便番号')),
                ('address', models.CharField(max_length=256, verbose_name='住所')),
                ('tel', models.CharField(max_length=16, verbose_name='電話番号')),
                ('fax', models.CharField(blank=True, max_length=16, null=True, verbose_name='FAX番号')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='メールアドレス')),
                ('ceo_name', models.CharField(blank=True, max_length=256, null=True, verbose_name='代表名')),
                ('registration_number', models.CharField(blank=True, max_length=256, null=True, verbose_name='インボイス登録番号')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='作成日')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='更新日')),
                ('creator', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='create_company', to=settings.AUTH_USER_MODEL, verbose_name='作成者')),
                ('modifier', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, on_update=True, related_name='update_company', to=settings.AUTH_USER_MODEL, verbose_name='更新者')),
            ],
            options={
                'verbose_name': '会社',
                'verbose_name_plural': '会社',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='顧客ID')),
                ('client_type', models.CharField(blank=True, choices=[('1', '1：貿易'), ('2', '2：オークション'), ('3', '3：個人ブローカー'), ('4', '4：新車ディーラー'), ('5', '5：中古車ディーラー'), ('6', '6：レンタル'), ('7', '7：修理'), ('8', '8：エンドユーザー'), ('9', '9：その他')], max_length=3, null=True, verbose_name='業種')),
                ('credit_type', models.CharField(blank=True, choices=[('A', 'A：入金前引渡OK'), ('B', 'B：入金後引渡'), ('C', 'C：問題あり')], max_length=3, null=True, verbose_name='与信管理')),
                ('name', models.CharField(max_length=256, verbose_name='会社名')),
                ('country_code', models.CharField(blank=True, default='81', max_length=16, null=True, verbose_name='国番号')),
                ('zip', models.CharField(max_length=7, verbose_name='郵便番号')),
                ('address', models.CharField(max_length=256, verbose_name='住所')),
                ('tel', models.CharField(max_length=16, verbose_name='電話番号')),
                ('fax', models.CharField(blank=True, max_length=16, null=True, verbose_name='FAX番号')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='メールアドレス')),
                ('office', models.CharField(blank=True, max_length=256, null=True, verbose_name='支店営業所名')),
                ('pic1', models.CharField(blank=True, max_length=256, null=True, verbose_name='担当者1')),
                ('pic2', models.CharField(blank=True, max_length=256, null=True, verbose_name='担当者2')),
                ('pic3', models.CharField(blank=True, max_length=256, null=True, verbose_name='担当者3')),
                ('pic4', models.CharField(blank=True, max_length=256, null=True, verbose_name='担当者4')),
                ('pic5', models.CharField(blank=True, max_length=256, null=True, verbose_name='担当者5')),
                ('memo', models.TextField(blank=True, null=True, verbose_name='メモ')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='作成日')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='更新日')),
                ('creator', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='create_client', to=settings.AUTH_USER_MODEL, verbose_name='作成者')),
                ('modifier', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, on_update=True, related_name='update_client', to=settings.AUTH_USER_MODEL, verbose_name='更新者')),
            ],
            options={
                'verbose_name': '顧客',
                'verbose_name_plural': '顧客',
            },
        ),
    ]
