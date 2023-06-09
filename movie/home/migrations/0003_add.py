# Generated by Django 4.1.7 on 2023-03-24 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_blog_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='add',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('img', models.ImageField(upload_to='picture')),
                ('cate', models.CharField(max_length=50)),
                ('desc', models.TextField()),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
