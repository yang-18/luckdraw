# Generated by Django 3.2.9 on 2023-01-25 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_admintablemodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='balance',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='余额'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='consumption',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='消费'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='level',
            field=models.IntegerField(default=1, null=True, verbose_name='等级'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='recharge',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='充值'),
        ),
    ]