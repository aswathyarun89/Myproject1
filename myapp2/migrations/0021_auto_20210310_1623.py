# Generated by Django 3.1.2 on 2021-03-10 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp2', '0020_auto_20210310_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_info',
            name='User_Photo',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]
