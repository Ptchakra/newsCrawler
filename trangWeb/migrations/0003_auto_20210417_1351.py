# Generated by Django 3.1.7 on 2021-04-17 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trangWeb', '0002_auto_20210417_0143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tong_bai_hang_ngay',
            name='ngay_them',
            field=models.DateTimeField(default='2021-04-17'),
        ),
        migrations.AlterField(
            model_name='trangweb',
            name='ngay_them',
            field=models.DateTimeField(default='17-04-2021 13:51:23'),
        ),
    ]