# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ShopCart(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey('TUser', models.DO_NOTHING, blank=True, null=True)
    shop = models.ForeignKey('TBook', models.DO_NOTHING, blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_cart'


class TAddress(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    detail_address = models.CharField(max_length=100, blank=True, null=True)
    postalcode = models.CharField(max_length=10, blank=True, null=True)
    cell_phone_number = models.CharField(max_length=20, blank=True, null=True)
    fixed_line_telephone = models.CharField(max_length=20, blank=True, null=True)
    user = models.ForeignKey('TUser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_address'


class TBook(models.Model):
    book_name = models.CharField(max_length=30, blank=True, null=True)
    author = models.CharField(max_length=30, blank=True, null=True)
    press = models.CharField(max_length=100, blank=True, null=True)
    publication_date = models.DateField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    book_number = models.CharField(max_length=50, blank=True, null=True)
    dd_price = models.FloatField(blank=True, null=True)
    disscuss = models.CharField(max_length=100, blank=True, null=True)
    editors_recommend = models.CharField(max_length=100, blank=True, null=True)
    content_recom = models.CharField(max_length=100, blank=True, null=True)
    about_author = models.CharField(max_length=100, blank=True, null=True)
    catalogue = models.CharField(max_length=100, blank=True, null=True)
    media_comments = models.CharField(max_length=100, blank=True, null=True)
    read_online = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    classify = models.ForeignKey('TSorted', models.DO_NOTHING, blank=True, null=True)
    edition = models.IntegerField(blank=True, null=True)
    printing_time = models.DateTimeField(blank=True, null=True)
    category = models.CharField(max_length=50, blank=True, null=True)
    pages_number = models.IntegerField(blank=True, null=True)
    word_count = models.IntegerField(blank=True, null=True)
    book_size = models.CharField(max_length=100, blank=True, null=True)
    paper = models.CharField(max_length=50, blank=True, null=True)
    packaging = models.CharField(max_length=50, blank=True, null=True)
    whether_suit = models.IntegerField(blank=True, null=True)
    shelves_date = models.DateTimeField(blank=True, null=True)
    sales = models.IntegerField(blank=True, null=True)
    comment_number = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_book'


class TOrder(models.Model):
    order_number = models.CharField(max_length=50, blank=True, null=True)
    user = models.ForeignKey('TUser', models.DO_NOTHING, blank=True, null=True)
    address = models.ForeignKey(TAddress, models.DO_NOTHING, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    all_price = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_order'


class TOrderiterm(models.Model):
    shop = models.ForeignKey(TBook, models.DO_NOTHING, blank=True, null=True)
    order = models.ForeignKey(TOrder, models.DO_NOTHING, blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_orderiterm'


class TSorted(models.Model):
    tason = models.CharField(max_length=30, blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_sorted'


class TUser(models.Model):
    username = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    salt=models.CharField(max_length=255,blank=True, null=True)
    is_active=models.BooleanField(default=False)
    class Meta:
        managed = False
        db_table = 't_user'
