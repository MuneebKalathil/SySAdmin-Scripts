from fabric.api import *
import urllib.request
import os

'''
This script will download the tar.gz file from Gitlab to local directory and extract it, then compress again with zip & tar.xz without including root folder. After compressing in .zip.tar.xz, It will upload to server. Then extract all the files, Overwrites.

After extracting, It will remove compressed files from server & Local system 

NB: Need Python3 + fabric3 
'''

env.host_string = 'root@server.com'
print("######################################")
print("#                                    #")
print("#                                    #")
print("#         App Deployer               #")
print("#     Script by mK - N/w  Eng        #")
print("#                                    #")
print("######################################")

print("######################################")
print("#                                    #")
print ("     File Uploader            \n")



# Download Repo in tar.gz format from gitlab using token. Then extracts and compress without root folder.
def extract():
    code_dir ='~/Muneeb/br'
    url="http://192.168.1.15/muneebkalathil/br/repository/archive.tar.gz?ref=dev&&private_token=npCVGzBfks6ASsqX1-ss"
    urllib.request.urlretrieve(url,"brownrice.tar.gz")
    with lcd(code_dir):
        local("tar xvzf brownrice.tar.gz")
        local("cd brown-rice*/ && zip -r brownrice.zip ./. && tar cvJf brownrice.tar.xz brownrice.zip && scp brownrice.tar.xz root@server.com:/home/admin/web/br")
    
# Upload the Compresed folder to server and extracts. Then, removed compressed files. 
def upload():
    code_dir1 ='/home/admin/web/br/'
    with cd(code_dir1):
        run("tar xvJf brownrice.tar.xz")
        run("unzip -o brownrice.zip")
        run("rm brownrice.tar.xz -f")
        run("rm brownrice.zip -f") 

# Remove Zip & Extracted files from  Local system
def destroy():
    code_dir2 ='~/Muneeb/brownrice'
    with lcd(code_dir2):
        local("rm brownrice.tar.gz -f")
        local("rm brown-rice-dev* -rf") # Be Careful :)


extract()
upload()
destroy()



