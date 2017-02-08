from fabric.api import *
import sys

'''
This script will run a command on server1. This script does not use any error catching.
'''

print("######################################")
print("#                                    #")
print("#                                    #")
print("#         Run Command                #")
print("#     Script by mK - N/w  Eng        #")
print("#                                    #")
print("######################################")

print("######################################")
print("#                                    #")
print("\n Note: Commands Executed here will be run on Server1\n\n")


def run_server1(comnd):
    env.host_string = 'root@server1.com'
    code_dir = '/home/admin/web/server1'
    with cd(code_dir):
        run(comnd)
        
run_server1("ls") # ls is the command used to execute on server1 in the folder /home/admin/web/server1
    






