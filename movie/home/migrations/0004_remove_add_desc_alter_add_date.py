# Generated by Django 4.1.7 on 2023-03-24 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_add'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='add',
            name='desc',
        ),
        migrations.AlterField(
            model_name='add',
            name='date',
            field=models.DateField(),
        ),
    ]