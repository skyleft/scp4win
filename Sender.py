#-*- coding:utf-8 -*-
#!/usr/bin/python

from paramiko import SSHClient
from scp import SCPClient
import os
import os.path as op
import time
import Recorder

class Sender(object):
    def __init__(self,server,username,password,dest_path,from_path):
        self.dest_path = dest_path
        self.from_path = from_path
        self.recorder = Recorder.Recorder()
        self.ssh = SSHClient()
        self.ssh.load_system_host_keys()
        self.ssh.connect(server,username=username,password=password)
        self.sftp = self.ssh.open_sftp()
        self.scp = SCPClient(self.ssh.get_transport())

    def send(self,file_path):
        if op.exists(file_path):
            file_modify_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(os.stat(file_path).st_mtime))
            if not self.recorder.isSynced(file_path,file_modify_time):
                new_file_path = self.dest_path+file_path.split(self.from_path)[1]
                new_file_dir,new_file = op.split(new_file_path)
                if not rexists(self.sftp,new_file_dir):
                    rmkdir(self.sftp,new_file_dir)
                self.scp.put(file_path,new_file_path)
                self.recorder.record(file_path,file_modify_time)
            else:
                pass

def rexists(sftp, path):
    try:
        sftp.stat(path)
    except IOError, e:
        if e[0] == 2:
            return False
        else:
            return True
    return True

def rmkdir(sftp,path):
    if rexists(sftp,op.split(path)[0]):
        sftp.mkdir(path)
    else:
        rmkdir(sftp,op.split(path)[0])
        sftp.mkdir(path)
