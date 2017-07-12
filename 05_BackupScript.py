
'''
This script will do 3 functions
1. Backup remote DB to same server then copies to the local server, after that it will remove from the server.
2. Sync  the remote server  project folder to the local server
3. Make a compressed copy of the synced folder

print("######################################")
print("#                                    #")
print("#                                    #")
print("#           Backup Script            #")
print("#     mK - muneeb.k@outlook.com      #")
print("#                                    #")
print("######################################")

'''


from datetime import datetime
from fabric.api import *

date_now = datetime.now()
date_now = date_now.strftime('%d-%m-%y_%I-%M-%p')

env.host_string = 'root@192.168.20.55'

def otsms_db():
    bk_command = 'mysqldump -u villadbuser -ppassword vcsms | xz > vcsms_%s.sql.xz' % (date_now)
    local_dir ='/home/villauser/backup/OTSMS/db/'
    remote_dir ='/backup/'
    with cd(remote_dir):
        run(bk_command)
        get('/backup/*.sql.xz',local_dir)
        run('rm *.sql.xz -f')

def otsms_sync():
    bk_command = 'rsync -avz root@192.168.20.55:/var/www/vcsms /home/villauser/backup/OTSMS/files'
    local(bk_command)

def otsms_zip():
    local_dir = '/home/villauser/backup/OTSMS/files'
    bk_command = 'tar cvJf vcsms_%s.tar.xz vcsms' %(date_now)
    with lcd(local_dir):
        local(bk_command)

otsms_db()
otsms_sync()
otsms_zip()

