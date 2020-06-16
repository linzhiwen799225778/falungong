# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
class TaobaoPipeline:
    def process_item(self, item, spider):
        print(3213211312)
        conn=pymongo.MongoClient('mongodb://127.0.0.1:27017')
        mydb = conn['lin']
        myset = mydb['taobao']
        myset.insert({'name':item['name'],'price':item['price']})
        res=myset.find()
        print(res)
        return item
