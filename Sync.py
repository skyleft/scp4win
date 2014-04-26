#-*- coding:utf-8 -*-
#!/usr/bin/python

from Config import Config
def sync():
    #get the config for destination
    config = Config()
    server =  config.getConfig('server')
    username = config.getConfig('username')
    password = config.getConfig('password')
    dest_path = config.getConfig('dest_path')
    from_path = config.getConfig('from_path')
    from_exclude = config.getConfig('from_exclude')
    #print dest_path,from_path,from_exclude

    
def main():
    sync()

if __name__ == '__main__':
    main()
