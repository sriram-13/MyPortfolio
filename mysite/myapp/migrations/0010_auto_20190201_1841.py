# Generated by Django 2.1.5 on 2019-02-01 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_auto_20190201_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='from_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='experience',
            name='to_date',
            field=models.DateField(),
        ),
    ]
