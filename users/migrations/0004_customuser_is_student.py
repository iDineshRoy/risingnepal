# Generated by Django 3.2.7 on 2023-04-28 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20230427_1325'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_student',
            field=models.BooleanField(default=False),
        ),
    ]
