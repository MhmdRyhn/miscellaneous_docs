# Most used Python3 commands



## Index
- [Create and use virtual environment](#create-and-use-virtual-environment) <br>
- [Install and Uninstall Python3 Packages](#install-and-uninstall-python3-packages) <br>



## Create and use virtual environment
**1. Check if you have virtual environment `virtualenv` installed**
```cmd
pip3 list
```
**2. If `virtualenv` isn't installed, install it**
```cmd
pip3 install virtualenv
```
**3. Enter into your desired directory where you want to create Virtual Environment.** <br>
```cmd
cd path/to/your/desired/directory
```
**4. Create `virtualenv`**
```cmd
virtualenv -p python3 <virtualenv_dir_name>
```
**5. To activate virtual environment**
```cmd
cd <virtualenv_dir_name>
source bin/activate
```
**6. Install or uninstall packages in virtual environment**
```cmd
pip3 install <package_name>
```
Or
```cmd
pip3 uninstall <package_name>
```
**7. To deactivate virtual environment**
```cmd
deactivate
```
[Return to Index](#index) <br>




## Install and Uninstall Python3 Packages
**To Install**
```
pip3 install <package-name>
```
Or
```
sudo pip3 install <package-name>
```
**To Uninstall**
```
pip3 ununstall <package-name>
```
Or
```
sudo pip3 uninstall <package-name>
```
[Return to Index](#index) <br>









