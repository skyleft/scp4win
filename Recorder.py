#-*- coding:utf-8 -*-
#!/usr/bin/python

import sqlite3
import os

class Recorder(object):
    def __init__(self):
        if os.path.exists('.record.db'):
            self.cx = sqlite3.connect('.record.db')
            self.cu = self.cx.cursor()
        else:
            self.cx = sqlite3.connect('.record.db')
            self.cu = self.cx.cursor()
            #create table
            self.cu.execute('create table sync_record(id integer primary key autoincrement,file_name varchar(255) not null,sync_time datetime not null,modify_time datetime not null')

    def record(self,file_name,file_modify_time):
        self.cu.execute("insert into sync_record(file_name,sync_time,modify_time) values('%s','%s','%s')" % (file_name,time.strftime('%Y-%m-%d',time.localtime()),file_modify_time))
        self.cx.commit()

    def isSynced(self,file_name,file_modify_time):
        self.cu.execute("select 1 from sync_record where file_name='%s' and sync_time>='%s'" % (file_name,file_modify_time))
        if self.cu.fetchall():
            return True
        else:
            return False
        
