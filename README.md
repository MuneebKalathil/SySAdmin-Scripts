# SySAdmin-Scripts

<b>1. fileuploader_01.py</b><br>
This script will download the tar.gz file from Gitlab to local directory and extract it, then compress again with zip & tar.xz without including root folder. After compressing in .zip.tar.xz, It will upload to server. Then extract all the files, Overwrites.
After extracting, It will remove compressed files from server & Local system. <br>
<i>NB: Need Python3 + fabric3 <br> This script is usefull when there is no git.</i>

