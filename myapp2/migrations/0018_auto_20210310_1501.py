# Generated by Django 3.1.2 on 2021-03-10 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp2', '0017_course_student_map'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_info',
            name='User_Photo',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]