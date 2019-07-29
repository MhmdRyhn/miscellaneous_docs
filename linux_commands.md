# List of Useful LINUX Commands



## Table of Contents
- [Copy File or Folder to and from Server](copy-file-or-folder-to-and-rom-server)
- [Create New User](create-new-user)
- Alias
- Apache web server
- Directory related operation
- File related operation
- Hidden files'/directorys' name view
- LAMPP/XAMPP
- MySQL
- System Information



## Copy File or Folder to and from Server
**To Copy file from local machine to server**
- Using public key authentication
```
scp -i <public_key_file> /path/to/file/source user@ip:/path/to/the/destination
```



## Create New User
```
sudo adduser <username>
```
This'll add the user to a group named same as the username. To add the user to **sudo** group use following command
```
sudo usermod -aG sudo username
```
<br>[***Return to Table of Contents***](table-of-contents)



## Alias<br>
`alias short_name="long_name"`<br><br>
Meaning: After applying alias `short_name` can be used insted of `long_name`<br>
**Note:** There is no <kbd>Space</kbd> around `=` and `long_name` is enclosed in `""`
<br>


## Apache web server<br>
Start: ```sudo /etc/init.d/apache2 start```<br>
Stop: ```sudo /etc/init.d/apache2 stop```
<br>


## Directory related operation<br>
View contents: `ls`<br>
Change directory: `cd`<br>
Go one directory back: `cd ..`<br>
Go to root directory: `cd`
<br>


## File related operation<br>
At first, go to the file's directory using `cd path/to/your/file/directory/` and then apply the following commands.<br><br>
Create: `touch Fil_Name_With_Extension`<br>
Open: `xdg-open Fil_Name_With_Extension`<br>
View content in terminal: `cat Fil_Name_With_Extension`<br>
Edit in terminal: `nano Fil_Name_With_Extension`
<br>


## Hidden files'/directorys' name view<br>
```command
cd path/to/your/preferred/directory/
ls -ld .?*
```
[**View Explanation**](https://askubuntu.com/questions/468901/how-to-show-only-hidden-files-in-terminal)
<br>


## LAMPP/XAMPP<br>
Open Control Panel
```cmd
cd /opt/lampp/
sudo chmod 755 manager-linux-x64.run
sudo ./manager-linux-x64.run
```
Start: `sudo /opt/lampp/lampp start`<br>
Stop: `sudo /opt/lampp/lampp stop`
<br>


## MySQL<br>
Start: `sudo /etc/init.d/mysql start`<br>
Stop: `sudo /etc/init.d/mysql stop`
<br>


## System Information<br>
Info about all installed packages: `dpkg -l` or apt `list --installed` [[More]](https://askubuntu.com/questions/17823/how-to-list-all-installed-packages)<br>
Package Information: [Go Here](https://www.howtogeek.com/229682/how-to-find-out-exact-package-names-for-applications-in-linux/)<br>
Package version: If you installed any package using `apt`, to see the version you can try `apt-cache policy package_name
` [[More]](https://askubuntu.com/questions/440982/how-to-check-installed-program-version)<br> 
System Configuration And Hadware Information: [Go Here](https://www.cyberciti.biz/faq/linux-command-to-find-the-system-configuration-and-hardware-information/)<br>
Find Out Last System Reboot Time and Date: [Go Here](https://www.cyberciti.biz/tips/linux-last-reboot-time-and-date-find-out.html)<br>



