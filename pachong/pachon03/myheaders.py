import re
def get_headers(str1):
    str0='^(.*?): (.*?)$'
    result=re.findall(str0,str1,re.M)
    d={}
    for i in result:
        d[i[0]]=i[1]
    return d
def get_cookies(str2):
    new_str=str2.split('; ')
    dict1={}
    for i in new_str:
        new_i=i.split('=',1)
        dict1[new_i[0]]=new_i[1]
    return dict1
