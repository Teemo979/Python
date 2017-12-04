#_*_ coding:utf-8 _*_
#引入模块
import re
from urllib import request
from bs4 import BeautifulSoup
from urllib.request import urlretrieve

#从Num.txt文件中读取并依次获取图片
file = open("Num.txt",'r+')
for fund in file.readlines():
    string = fund.strip('\n')
    url = 'http://fund.eastmoney.com/'+string+'.html?spm=search'
    response = request.urlopen(url)
    Page = response.read()      #type(Page)=<class 'bytes'>
    soup = BeautifulSoup(Page,'lxml')  #type(soup)=<class 'bs4.BeautifulSoup'>
    # print(soup)  -->  一个没有格式的文本
    # print(soup.prettify())  获取格式完美的Html内容

    img=soup.select('img')     #提取出<img> </img> 类型为：list
    num = len(img)
    flag = 0
    rule = r'(?<=src=").+?[jp][pn]g'
    while num >1 :
        txt = str(img[flag])
        num = num - 1
        flag = flag + 1
        
        emm = re.compile(rule)  #编译
        err = re.search(emm,txt)#匹配
        txt_test = err.group(0)

        if num == 2:
           pic = txt_test.rsplit('/',1)[1] #以"/"为标志进行分割
           urlretrieve(txt_test,pic)        # 把URL的图片保存到当前目录下，命名为pic
file.close()


'''
#创建列表,获取列表长度并依次获取其图片
fund= ['110022','000878','100032','002851','001048','001616','180012','001986','161017','161725',
       '001513','003670','001195','000409','165524','001230','000603','000409']

coun = len(fund)
i = 0
while coun> 0:
    string = fund[i]
    coun = coun -1
    i = i+1
'''
'''
  rule_1 = r'(?<=<img).*(?<=")'
  rule_2 = r'(src=").+(?<=")'
  rule_3 = r'(?<=src=").+?[jp][pn]g'
  '''
'''
emm_1 = re.compile(rule_1)
err_1 = re.search(emm_1,txt)
txt_1 = err_1.group(0)

emm_2 = re.compile(rule_2)
err_2 = re.search(emm_2, txt_1)
txt_2 = err_2.group(0)

emm_3 = re.compile(rule_3)
err_3 = re.search(emm_3,txt_2)
txt_3 = err_3.group(0)
'''