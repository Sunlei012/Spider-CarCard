#!/bin/bash

import requests
import yagmail
import time
from bs4 import BeautifulSoup
import os
def email(subject,contents):
    #链接邮箱服务器
    yag = yagmail.SMTP( user=USERNAME, password=PASSWORD, host=HOST)
    # 发送邮件
    yag.send(RECIVE_MAIL, subject, contents)

if __name__ == "__main__":

    APPLYCODE = os.environ["APPLYCODE"]
    HOST = os.environ["HOST"]
    USERNAME = os.environ["USERNAME"]
    PASSWORD = os.environ["PASSWORD"]
    RECIVE_MAIL = os.environ["RECIVE_MAIL"]

    url = "http://apply.xkctk.jtys.tj.gov.cn/apply/norm/personQuery.html"
    localtime = time.localtime(time.time())
    issueNumber = str(localtime[0])+str(localtime[1])
    applyCode = str(APPLYCODE)
    payload = 'pageNo=1&issueNumber='+'000000'+'&applyCode='+applyCode
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
    'Upgrade-Insecure-Requests': '1',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Content-Length': '51',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'apply.xkctk.jtys.tj.gov.cn',
    'Origin': 'http://apply.xkctk.jtys.tj.gov.cn',
    'Proxy-Connection': 'keep-alive',
    'Referer': 'http://apply.xkctk.jtys.tj.gov.cn/apply/norm/personQuery.html',
    # 'Cookie': 'JSESSIONID=DB7A6BC4342376575C6068EB5C222523-n2.Tomcat1'
    }


    response = requests.request("POST", url, headers=headers, data = payload)
    text = response.text
    #.encode('utf8')
    # print(issueNumber)
    #print(text)
    soup = BeautifulSoup(text,'lxml')
    option = soup.find_all('option')
    #print(option)
    fo = open("CarCardTime.txt","r+")
    print(fo.read())
    print(str(option))
    if fo.read() != str(option):
        print("ttt")
    
        fo.write(str(option))
        if str(issueNumber) in str(option):
            string = "/apply/images/mall/notBallot.png"
            if string in text:
                print("not found")
                email("未中签","抱歉此次摇号没有摇中，申请编号为"+applyCode)
            else:
                email("中签！","恭喜本次摇号您已摇中,申请编号为"+applyCode)
                print("found")

        else :
            print(APPLYCODE,USERNAME,HOST,RECIVE_MAIL)