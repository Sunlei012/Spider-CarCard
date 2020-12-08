import requests
import yagmail
import time
from bs4 import BeautifulSoup
def email(subject,contents):
    #链接邮箱服务器
    yag = yagmail.SMTP( user="973628385@qq.com", password="apnzyguxlrqcbfdd", host='smtp.qq.com')
    # 发送邮件
    yag.send('sunlei012@outlook.com', subject, contents)


url = "http://apply.xkctk.jtys.tj.gov.cn/apply/norm/personQuery.html"
localtime = time.localtime(time.time())
issueNumber = str(localtime[0])+str(localtime[1])
applyCode = str(8479102777306)
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
# fo = open("CarCardTime.txt","r+")
# print(fo.read())
# print(str(option))
# if fo.read() != str(option):
#     print("ttt")
#
#     fo.write(str(option))
if str(issueNumber) in str(option):
    string = "/apply/images/mall/notBallot.png"
    if string in text:
        print("not found")
        email("未中签","抱歉此次摇号没有摇中，申请编号为"+applyCode)
    else:
        email("中签！","恭喜本次摇号您已摇中,申请编号为"+applyCode)
        print("found")