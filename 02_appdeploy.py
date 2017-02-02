from fabric.api import *
import sys

'''
This script will deploy app on remote server using GIT. 
Steps:
(1) Pull from Local Git Server to Sys Admin's System
(2) Push to a Git server on Internet (Bitbucket here)
(3) Run git pull from remote server , which pulls git repos from Bitbucket

NB: Set all git URL's before & need Python3 + fabric3


    Local_Git_Server -------------------
   ____|  |  |____                      |
  |       |       |                     |
  |       |       |                     |
  |       |       |                     V (1) 
 user1	user2	userN             SySAdmin(Running Script) ---------(2)--(3)
								    |     |
								    |     |
								    |	  |							  
 Remote Server <----------- BitBucket(Internet) <--------------------     |
     ^                                                                    |
     |                                                                    |
      --------------------------------------------------------------------

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
print("\n Note: Files will be uploaded on Server.com using GIT \n\n")



'''
Pull from Local Git Server and push to intermediate Git server on Internet
'''

def abc_local():
    code_dir = '/home/Muneeb/pk/abc/'    
    with lcd(code_dir):
        local("git pull origin master")
        local("git push bitbucket master") # bitbucket is the remote url name, can be anything


'''
Pull from Bitbucket or any other intermediate git server to Server
'''


def abc_server():
    env.host_string = 'root@server.com'
    code_dir = '/home/admin/web/abc/'
    with cd(code_dir):
        run("git pull --no-edit origin master")


abc_local()
abc_server()
