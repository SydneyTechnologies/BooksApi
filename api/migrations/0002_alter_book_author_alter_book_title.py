# Generated by Django 4.1.1 on 2022-09-18 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
