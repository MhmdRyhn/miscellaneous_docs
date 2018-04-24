# List of Useful LINUX Commands
<br>


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
Start: `sudo /opt/lampp/lampp start`<br>
Stop: `sudo /opt/lampp/lampp stop`<br><br>
Open Control Panel
```cmd
cd /opt/lampp/
sudo chmod 755 manager-linux-x64.run
sudo ./manager-linux-x64.run
```
<br>


## MySQL<br>
Start: `sudo /etc/init.d/mysql start`<br>
Stop: `sudo /etc/init.d/mysql stop`
<br>



