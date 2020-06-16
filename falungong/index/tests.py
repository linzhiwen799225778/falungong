from django.test import TestCase

# Create your tests here.
import redis

my_redis=redis.Redis(host='127.0.0.1',port=6379)

my_redis.set('name','linzhiwen')
name=my_redis.get('name')

print(name)
