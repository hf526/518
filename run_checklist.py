#coding=gbk
import os,unittest,time
from public import Sendmail
from public import HTMLTestRunnerEN
#定义测试报告存放路径
report_path=os.path.abspath(os.curdir)+'\\report\\'   #获取项目的绝对路径
print report_path
#定义测试用例的目录
case_path=os.path.abspath(os.curdir)+'\\testcase\\'
print case_path
#搜索测试用例，加载到用例集合
caselist=unittest.defaultTestLoader.discover(case_path,pattern='check*.py')
print caselist
#定义测试报告的名字
report_name=report_path+str(time.strftime('%Y-%m-%d %H：%M：%S',time.localtime(time.time()))+'.html')
print report_name
#创建文件，以二进制方式去写文件
fp=open(report_name,'wb')
#使用htmltestrunner去运行用例集合
HTMLTestRunnerEN.HTMLTestRunner(fp,title="Autotest  Report",description=u"登录测试").run(caselist)
#关闭文件
fp.close()

############发送邮件
# Sendmail.send_mail(report_name,"wpl133@163.com")