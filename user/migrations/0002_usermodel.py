# Generated by Django 3.2.9 on 2023-01-20 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now_add=True, verbose_name='更改时间')),
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True, unique=True, verbose_name='昵称')),
                ('head_portrait', models.ImageField(null=True, upload_to='img', verbose_name='头像')),
                ('password', models.CharField(max_length=255, verbose_name='密码')),
                ('telephone', models.CharField(max_length=22, unique=True, verbose_name='手机号码')),
                ('email', models.CharField(max_length=255, null=True, unique=True, verbose_name='邮箱')),
                ('level', models.IntegerField(default=1, verbose_name='等级')),
                ('balance', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='余额')),
                ('consumption', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='消费')),
                ('recharge', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='充值')),
                ('token', models.CharField(max_length=225)),
            ],
            options={
                'verbose_name_plural': '用户',
                'db_table': 'usermodel',
            },
        ),
    ]
