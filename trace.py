#!/usr/bin/python
#coding=utf-8
import pexpect
import os
import sys
import time
import re
import datetime
yuanip = raw_input('输入源ip地址:')
destip = raw_input('输入目的ip地址:')
panduan = str(yuanip.split('.')[3])
mudi = str(destip.split('.')[3])
#print panduan
def houzhui(panduan):
    if panduan<62:
        houzhui = '62'
        return houzhui
    elif 62<panduan<190:
        houzhui = '190'
        return houzhui
    elif 190<panduan<252:
        houzhui = '252'
        return houzhui
host = re.findall(r'\d+\.\d+\.\d+\.',str(yuanip))[0]+ houzhui(int(panduan))
mudiwangguan = re.findall(r'\d+\.\d+\.\d+\.',str(destip))[0]+ houzhui(int(mudi))
#print mudiwangguan
#print host
user = 'xxxx'
password = 'xxxx'
starttime = datetime.datetime.now()
c = pexpect.spawn('ssh %s@%s' % (user, host))
i = c.expect(['password: ', pexpect.EOF, pexpect.TIMEOUT])
c.sendline(password)
c.sendline('\n')
#endtime = datetime.datetime.now()
#print (endtime - starttime).seconds
time.sleep(1)
c.sendline('super')
time.sleep(0.2)
c.expect(['Password', pexpect.EOF, pexpect.TIMEOUT])
c.sendline('xxxxxx')
endtime = datetime.datetime.now()
#print (endtime - starttime).seconds
c.sendline('tracert -m 6 -q 1 -a '+ host +' '+ destip)
c.sendline('ping -q -a ' + host +' ' + destip )
c.sendline('ping -q -a ' + host +' ' + mudiwangguan )
time.sleep(0.5) 
c.sendline('quit')
c.sendline('quit')
c.expect(['break',pexpect.EOF, pexpect.TIMEOUT])

c.expect(['<', pexpect.EOF, pexpect.TIMEOUT])
trace =  c.before
print trace
c.expect(['break',pexpect.EOF, pexpect.TIMEOUT])
c.expect(['<', pexpect.EOF, pexpect.TIMEOUT])

ping = c.before
print ("交换机网关到目的主机ip测试结果:%s"%ping)
c.expect(['break', pexpect.EOF, pexpect.TIMEOUT])
c.expect(['<', pexpect.EOF, pexpect.TIMEOUT])
print ("交换机网关到目的主机网关测试结果:%s"% c.before)
