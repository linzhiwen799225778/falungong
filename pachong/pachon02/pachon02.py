# post请求
from urllib import request,parse
# url='https://www.iqianyue.com/mypost'
# data={
#     'name':'linzhiwen',
#     'pass':'123456'
# }
# new_data=bytes(parse.urlencode(data),encoding='utf-8')
# res=request.urlopen(url,new_data).read().decode()

# json格式的装换
# import re,json
# url='http://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E7%99%BE%E5%BA%A6%E5%9B%BE%E7%89%87&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&hd=&latest=&copyright=&word=%E7%99%BE%E5%BA%A6%E5%9B%BE%E7%89%87&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=1&fr=&expermode=&force=&pn=30&rn=30&gsm=1e&1588069460413='
# res=request.urlopen(url).read().decode()
# # print(res)
# # resu=re.findall('"http:(.*?)"',res)
# # print(resu)
# mew_res=json.loads(res)
# num=0
# print(mew_res)
# for i in mew_res['data']:
#     print(i['thumbURL'])
#     result=request.urlopen(i['thumbURL']).read()
#     num+=1
#     with open('png/{}.jpg'.format(num),'wb') as w:
#         w.write(result)



