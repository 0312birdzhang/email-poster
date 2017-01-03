#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2017年1月3日

@author: debo.zhang
'''

from email import encoders, MIMEMultipart
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
import constant

class Sender():
    def __init__(self,from_addr,password,to_addr,smtp_server,email_type):
        self.constant = constant.Constant()
        if email_type == self.constant.EMAIL_TEXT:
            self.msg = MIMEText()
        elif email_type == self.constant.EMAIL_HTML:
            self.msg = MIMEText()
        elif email_type == self.constant.EMAIL_MULTI:
            self.msg = MIMEMultipart()
        else:
            self.msg = MIMEText()
    
    """
        格式化地址
    """
    def format_addr(self,s):
        name, addr = parseaddr(s)
        return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))
    
    