from fabric.api import *
import sys
from multiprocessing import Process

'''
This script will deploy app on 2 Servers using GIT. 
Steps:
(1) Pull from Local Git Server to Sys Admin's System
(2) Push to a Git server on Internet (Bitbucket here)
(3) Run git pull from Server1 , which pulls git repos from Bitbucket
(4) Run git pull from Server2 , which pulls git repos from Bitbucket

This code can be used with multiple server deploying with minor edits.
NB: Set all git URL's before & need Python3 + fabric3


    Local_Git_Server --------------------
   ____|  |  |____                      |
  |       |       |                     |
  |       |       |                     |
  |       |       |                     v(1) 
 user1	user2	userN             SySAdmin(Running Script) ---------(2)--(3)--(4)
								    |     |    |
								    |     |    |
								    |	  |    |							  
                            BitBucket(Internet) <--------------------     |    | 
                               |        |                                 |    |
                               |        v                                 |    |
                               |      Server1 -----------------------------    |
                               v                                               |
                           Server2 ---------------------------------------------
'''



print("######################################")
print("#                                    #")
print("#                                    #")
print("#         App Deployer               #")
print("#     Script by mK - N/w  Eng        #")
print("#                                    #")
print("######################################")

print("######################################")
print("#                                    #")
print("\n Note: Files will be uploaded on both Server1 & Server2 using Git\n\n")


'''
Pull from Gitlab Server & Push to Bitbucket server
'''

def abc_local():
    code_dir = '/home/Muneeb/abc/'    
    with lcd(code_dir):
        local("git pull origin master")
        local("git push bitbucket master")


'''
Pull from bitbucket in to Server1
'''


def abc_server1():
    env.host_string = 'root@server1'
    code_dir = '/home/admin/web/abc/'
    with cd(code_dir):
        run("git pull --no-edit origin master")

'''
Pull from bitbucket in to Server2
'''



def ams_server2():
    env.host_string = 'root@server2'
    code_dir = '/home/admin/web/abc/'
    with cd(code_dir):
        run("git pull --no-edit origin master")


abc_local()
abc_server1()
ams_server2()

