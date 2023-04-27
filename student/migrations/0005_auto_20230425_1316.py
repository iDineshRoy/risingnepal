# Generated by Django 3.2.7 on 2023-04-25 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_remove_student_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='billfeetypemodel',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='billmodel',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='parent',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='student',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='studentparent',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='yeargradesection',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='yeargradesectionstudent',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]