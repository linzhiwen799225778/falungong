# Generated by Django 2.0.6 on 2020-04-14 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShopCart',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('number', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'shop_cart',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('detail_address', models.CharField(blank=True, max_length=100, null=True)),
                ('postalcode', models.CharField(blank=True, max_length=10, null=True)),
                ('cell_phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('fixed_line_telephone', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 't_address',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(blank=True, max_length=30, null=True)),
                ('author', models.CharField(blank=True, max_length=30, null=True)),
                ('press', models.CharField(blank=True, max_length=100, null=True)),
                ('publication_date', models.DateField(blank=True, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('book_number', models.CharField(blank=True, max_length=50, null=True)),
                ('dd_price', models.FloatField(blank=True, null=True)),
                ('disscuss', models.CharField(blank=True, max_length=100, null=True)),
                ('editors_recommend', models.CharField(blank=True, max_length=100, null=True)),
                ('content_recom', models.CharField(blank=True, max_length=100, null=True)),
                ('about_author', models.CharField(blank=True, max_length=100, null=True)),
                ('catalogue', models.CharField(blank=True, max_length=100, null=True)),
                ('media_comments', models.CharField(blank=True, max_length=100, null=True)),
                ('read_online', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=100, null=True)),
                ('edition', models.IntegerField(blank=True, null=True)),
                ('printing_time', models.DateTimeField(blank=True, null=True)),
                ('category', models.CharField(blank=True, max_length=50, null=True)),
                ('pages_number', models.IntegerField(blank=True, null=True)),
                ('word_count', models.IntegerField(blank=True, null=True)),
                ('book_size', models.CharField(blank=True, max_length=100, null=True)),
                ('paper', models.CharField(blank=True, max_length=50, null=True)),
                ('packaging', models.CharField(blank=True, max_length=50, null=True)),
                ('whether_suit', models.IntegerField(blank=True, null=True)),
                ('shelves_date', models.DateTimeField(blank=True, null=True)),
                ('sales', models.IntegerField(blank=True, null=True)),
                ('comment_number', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 't_book',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(blank=True, max_length=50, null=True)),
                ('status', models.IntegerField(blank=True, null=True)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('all_price', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 't_order',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TOrderiterm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 't_orderiterm',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TSorted',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tason', models.CharField(blank=True, max_length=30, null=True)),
                ('parent_id', models.IntegerField(blank=True, null=True)),
                ('level', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 't_sorted',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=20, null=True)),
                ('password', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 't_user',
                'managed': False,
            },
        ),
    ]