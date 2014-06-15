#-*- coding:utf-8 -*-
#!/usr/bin/python

import sys
import ConfigParser
import Crypt
import os

class Config(object):
    def __init__(self,config_file='config.ini'):
        self.config_file = config_file
        self.configuration = {}
        self.crypt = Crypt.Crypt()
        self.configer = ConfigParser.SafeConfigParser()
        if not os.path.exists(self.config_file):
            print 'invalid config file'
            return
        
        #parse the config file
        
        self.configer.read(self.config_file)
        if 'dest' not in self.configer.sections() or 'from' not in self.configer.sections():
            print 'invalid config file.'
            return
        self.configuration['server'] = self.crypt.decode(self.configer.get('dest','server'))
        self.configuration['username'] = self.crypt.decode(self.configer.get('dest','username'))
        self.configuration['password'] = self.crypt.decode(self.configer.get('dest','password'))
        self.configuration['dest_path'] = self.configer.get('dest','path')
        self.configuration['from_path'] = self.configer.get('from','path')
        self.configuration['from_exclude'] = self.configer.get('from','exclude')

    def getConfig(self,config_name):
        if config_name in self.configuration.keys():
            return self.configuration[config_name]
        else:
            return None
    
    def clearConfig(self):
        if self.configer is not None:
            self.configer.set('dest','server','')
            self.configer.set('dest','username','')
            self.configer.set('dest','password','')
            self.configer.set('dest','path','')
            self.configer.set('from','path','')
            self.configer.set('from','exclude','')
            self.configer.write(file(self.config_file,'w+'));
    
    def saveConfig(self,*l,**cs):
        if self.configer is not None:
            if 'dest' not in self.configer.sections():
                self.configer.add_section('dest')
            if 'from' not in self.configer.sections():
                self.configer.add_section('from')
            if 'server' in cs.keys():
                self.configer.set('dest','server',self.crypt.encode(str(cs['server'])))
            if 'username' in cs.keys():
                self.configer.set('dest','username',self.crypt.encode(str(cs['username'])))
            if 'password' in cs.keys():
                self.configer.set('dest','password',self.crypt.encode(str(cs['password'])))
            if 'destpath' in cs.keys():
                self.configer.set('dest','path',str(cs['destpath']))
            if 'frompath' in cs.keys():
                self.configer.set('from','path',str(cs['frompath']))
            if 'fromexclude' in cs.keys():
                self.configer.set('from','exclude',str(cs['fromexclude']))
            self.configer.write(file(self.config_file,'w+'));
            

def test():
    c = Config()
    print c.getConfig('password')
    print c.getConfig('ddd')

if __name__=='__main__':
    test()
