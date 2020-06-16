import re

lst = [6,5,2,6,9,8,1,4]
# 选择排序
l=len(lst)
# for i in range(l):
#     for j in range(i+1,l):
#         if lst[i]>lst[j]:
#             lst[i],lst[j]=lst[j],lst[i]
# print(lst)
# 冒泡排序
# for i in range(l):
#     for j in range(1,l-i):
#         if lst[j]<lst[j-1]:
#             lst[j],lst[j - 1]=lst[j- 1],lst[j]
# print(lst)

# 直接插入排序
# def insert_sort(lists):
#     count = len(lists)
#     for i in range(1, count):
#         key = lists[i]
#         j = i - 1
#         while j >= 0:
#             if lists[j] > key:
#                 lists[j + 1] = lists[j]
#                 lists[j] = key
#             j -= 1
#     return lists
# insert_sort(lst)
# print(lst)
# a="13123456789"
# b=re.findall(r'^1[3,4,5,6,7,8,9]\d{9}$',a)
# print(b)