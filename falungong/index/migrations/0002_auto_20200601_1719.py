# Generated by Django 2.0.6 on 2020-06-01 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lunbo_picture',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]