#-*- coding:utf-8 -*-
#!/usr/bin/python

from Config import Config
import os
import Sender

#get the config for destination
config = Config()
server =  config.getConfig('server')
username = config.getConfig('username')
password = config.getConfig('password')
dest_path = config.getConfig('dest_path')
from_path = config.getConfig('from_path')
from_exclude = config.getConfig('from_exclude')
#print dest_path,from_path,from_exclude

sender = Sender.Sender(server,username,password,dest_path,from_path)

def sync(fp):    
    if os.path.isdir(fp):
        list_dirs = os.walk(fp)
        for root,dirs,files in list_dirs:
            for d in dirs:
                sync(os.path.join(root,d))
            for f in files:
                if root in from_exclude or os.path.join(root,f) in from_exclude:
                    pass
                else:
                    sender.send(os.path.join(root,f))

def main():
    sync(from_path)

if __name__ == '__main__':
    main()
