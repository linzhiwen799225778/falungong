# from multiprocessing import Pool
import time
import os
# import requests
# def get(i):
#     url='http://you.tube-kuyun.com/20200208/918_15a715a1/1000k/hls/e8ace89ec46000%03d.ts'%i
#     a=url.split('/')[-1]
#     print('开始下载%s'%a)
#     res=requests.get(url).content
#     with open('yewen/{}'.format(a),'wb') as w:
#         w.write(res)
# def hebin():
#     print('开始合并')
#     time.sleep(5)
#     res=os.popen('copy /b yewen\\*.ts yewen\\叶问.mp4')
#     res.read()
# if __name__ == '__main__':
#     pool=Pool(15)
#     for i in range(0,400):
#         pool.apply_async(get,args=(i,))
#     pool.close()
#     pool.join()
#     hebin()
print('开始合并')
# time.sleep(5)
res=os.popen('copy /b yewen\\*.ts yewen\\叶问.mp4')
print(res.read())
print('合并完成')











