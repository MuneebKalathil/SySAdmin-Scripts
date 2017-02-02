# SySAdmin-Scripts

<b>01. FileUploader.py</b><br>
This script will download the tar.gz file from Gitlab to local directory and extract it, then compress again with zip & tar.xz without including root folder. After compressing in .zip.tar.xz, It will upload to server. Then extract all the files, Overwrites.
After extracting, It will remove compressed files from server & Local system. <br>
<i>Note: This script is usefull when there is no git.</i>


<b>02. AppDeploy.py</b><br>
This script will deploy app on remote server using GIT. <br>
Steps:<br>
(1) Pull from Local Git Server to Sys Admin's System<br>
(2) Push to a Git server on Internet (Bitbucket here)<br>
(3) Run git pull from remote server , which pulls git repos from Bitbucket<br>

<i>Note: Set all git URL's before .</i>

```
    Local_Git_Server -------------------
   ____|  |  |____                      |
  |       |       |                     |
  |       |       |                     |
  |       |       |                     V (1) 
 user1	user2	userN             SySAdmin(Running Script) ---------(2)--(3)
                                                                    |     |
                                                                    |     |
                                                                    |     |
 Remote Server <----------- BitBucket(Internet) <--------------------     |
     ^                                                                    |
     |                                                                    |
      --------------------------------------------------------------------
```

<b>03. AppDeployMulti.py</b><br>
This script will deploy app on 2 servers using GIT. <br>
Steps:<br>
(1) Pull from Local Git Server to Sys Admin's System<br>
(2) Push to a Git server on Internet (Bitbucket here)<br>
(3) Run git pull from Server1 , which pulls git repos from Bitbucket<br>
(4) Run git pull from Server2 , which pulls git repos from Bitbucket<br>

This code can be used with multiple server deploying with minor edits.<br>

```

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
```
