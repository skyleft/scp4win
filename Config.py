#-*- coding:utf-8 -*-
#!/usr/bin/python

import sys
import ConfigParser

class Config(object):
    def __init__(self,config_file='config.ini'):
        if len(config_file)>0:
            self.config_file = config_file
        else:
            print 'No valid config file given.'
            sys.exit(-1)
        #parse the config file
        self.configuration = {}
        configer = ConfigParser.SafeConfigParser()
        configer.read(self.config_file)
        if 'dest' not in configer.sections() or 'from' not in configer.sections():
            print 'invalid config file.'
            sys.exit(-1)
        self.configuration['server'] = configer.get('dest','server')
        self.configuration['username'] = configer.get('dest','username')
        self.configuration['password'] = configer.get('dest','password')
        self.configuration['dest_path'] = configer.get('dest','path')
        self.configuration['from_path'] = configer.get('from','path')
        self.configuration['from_exclude'] = configer.get('from','exclude')

    def getConfig(self,config_name):
        if config_name in self.configuration.keys():
            return self.configuration[config_name]
        else:
            return None

def test():
    c = Config()
    print c.getConfig('password')
    print c.getConfig('ddd')

if __name__=='__main__':
    test()
