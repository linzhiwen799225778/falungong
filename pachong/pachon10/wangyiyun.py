# import requests
# from pachon03.myheaders import get_cookies
# url='https://music.163.com/weapi/v1/resource/comments/R_SO_4_1436709403?csrf_token='
# hreader={
# ':authority':'music.163.com',
# ':method':'POST',
# ':path':'/weapi/v1/resource/comments/R_SO_4_1436709403?csrf_token=',
# ':scheme':'https',
# 'accept':'*/*',
# 'accept-encoding':'gzip, deflate, br',
# 'accept-language':'zh-CN,zh;q=0.9',
# 'content-length':'482',
# 'content-type':'application/x-www-form-urlencoded',
# 'origin':'https://music.163.com',
# 'referer':'https://music.163.com/song?id=1436709403',
# 'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
# }
# str1='JSESSIONID-WYYY=sVjtJYMxWMiOqjiBC8Hr5rAs9BzVSyofZTrAugIURt%5CB0Ri1wVg22FVJormW%5CdsznAcu4f9x%2F7iwjA%2BIkGA4qDdCmeub1qgWhBFYagfwImBA8XW3wIu71Jzt2b4rmrD1c4he%2BbgzqnnDTDoW%5C250nm2Bi441Unq%5CA%5CgfJf7FtfreC0BN%3A1589373261558; _iuqxldmzr_=32; _ntes_nnid=5a53f9493c232c563b9a4aeb9a9769b8,1589371461702; _ntes_nuid=5a53f9493c232c563b9a4aeb9a9769b8; WM_NI=NVkqyh4aQ6pcMaSKUDyS8BkKhHWY8UBtbW8XQmAVJJp%2FFY3OLlQOcW1BiE%2Bq7IyhmXftXoMFUMEgpyBzUiMEoh6b9p%2FU3iQkeujQSK7V1CbVgcw9K%2Fr2G5CJIuoQAZRpNE4%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eea7e221a1bca1d4ce6b98ac8fb7c55e928a8fafae549789a6d7ca4b97ea98b1e62af0fea7c3b92a8e8aa592fc64f8bf9fd7f3698fbf9dacd850bb8df8a3ea41ac9899babb5f82acaeb8bb5493b38fb7c942b4f18abab24590b49fb0e25df39ea7a6aa7bf597b789f054a6ac9890d04e97938b88f37382a69b8ad04fadb8fa83bc7ced8bfd8ad461a7aba6b2d241f58affa4e15ea5bdb9daca25b2ee89d6c2428baba1b2c45292b082a6b737e2a3; WM_TID=%2BvArkZuJ5BNAURRRFBJ6HFDj7aEUqHb0; playerid=57228020'
# cookies=get_cookies(str1)
# data={
# 'params': 'xp30Mu1iIWVjUyRHeN//9kJH6X7g3E304h2lJbGE0tThDk9fyhF+EZNXYShBdMHa5fAt4+etBP+Wu9S/Qyy5PIwNYXYM8zqA6mP0KSIcJEp3p0MHUSobKWd8zDk8JN1FvsD4Nkn1oHhefdvhZU9pz/4cMlxjsi7LUZLuIyCw2jt2x1AxJU5ea6meH/Z7J4JX',
# 'encSecKey': '26960cc24c06ce3aef47ec8e6743c196058d34fc809c6675b35fc25abac9ce99e413281c3176890dcfc5a14840c33f0388e657b53d9fe8d3609dd55c6c3ef338953cde03b78a50fd1a837518073ac1b6da7655238947c4d53e5b6dface218fe5b801f1839541f0dc0e72cec6122c3a1187e9fbe9fa05e6c8aa00eaae09a6bf90'
# }
# res=requests.post(url,data=data).json()
# for i in res['hotComments']:
#     print(i['content'])
from selenium import webdriver
import time
url='https://music.163.com/#/song?id=1436709403'
diver=webdriver.Chrome('chromedriver.exe')
diver.get(url=url)
diver.switch_to_frame('g_iframe')
diver.execute_script('var q=document.documentElement.scrollTop=900')









