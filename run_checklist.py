#coding=gbk
import os,unittest,time
from public import Sendmail
from public import HTMLTestRunnerEN
#������Ա�����·��
report_path=os.path.abspath(os.curdir)+'\\report\\'   #��ȡ��Ŀ�ľ���·��
print report_path
#�������������Ŀ¼
case_path=os.path.abspath(os.curdir)+'\\testcase\\'
print case_path
#�����������������ص���������
caselist=unittest.defaultTestLoader.discover(case_path,pattern='check*.py')
print caselist
#������Ա��������
report_name=report_path+str(time.strftime('%Y-%m-%d %H��%M��%S',time.localtime(time.time()))+'.html')
print report_name
#�����ļ����Զ����Ʒ�ʽȥд�ļ�
fp=open(report_name,'wb')
#ʹ��htmltestrunnerȥ������������
HTMLTestRunnerEN.HTMLTestRunner(fp,title="Autotest  Report",description=u"��¼����").run(caselist)
#�ر��ļ�
fp.close()

############�����ʼ�
# Sendmail.send_mail(report_name,"wpl133@163.com")