# Generated by Django 2.0.6 on 2020-06-01 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='headpic',
            field=models.CharField(max_length=20),
        ),
    ]