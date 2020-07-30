# Serve A Flask App Using Apache 2
Here we will discuss about the steps of configuring a Flask app and Apache2 server so that the flask app can be 
served using the Apache2 server. Follow the steps and get your flask served by apache2. It is assumed that you 
are developing you application using `python3.6`. If your version is other than this, then edit commands accordingly.


### Project structure
- It is assumed that your project structure is as follows.
```text
flask-apache2-demo/
    app1/
        __init__.py
        ...
        ...
    app2/
        __init__.py
        ...
        ...
    ...
    ...
    appn/
        __init__.py
        ...
        ...
    flask_demo/
        __init__.py
        main.py
        ...
        ...
    venv/
        bin/
        lib/
        pyenv.cfg
    .gitignore
    flask-demo.apache2.conf
    gateway.wsgi
    requirements.txt
    ...
    ...
```


### Install Apache2
```shell script
sudo apt-get update -y
sudo apt-get install -y apache2
```


### Install required packages
```shell script
# vim is optional
sudo apt-get install -y libapache2-mod-wsgi-py3 python3-dev git vim
```


### Enable mod_wsgi
- Enable mod_wsgi if it is not enabled automatically.
```shell script
sudo a2enmod wsgi
```


### Clone your project
- Clone the project from git server.
```shell script
git clone <git-repositoy-url-to-clone>
```


### Move your project directory to /var/www/
```shell script
sudo cp -r flask-apache2-demo /var/www/
```
- In you project root directory, make sure you have the desired **WSGI** script. The wsgi script is `gateway.wsgi`. 
It's something like as following. 
```python
activate_this = '/var/www/flask-apache2-demo/venv/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, "/var/www/flask-apache2-demo/")
# This is where your app resides
from flask_demo.main import app
application = app
```


### Create virtual environment
- Install `pip`, if not installed already.
```shell script
sudo apt-get install -y python3-pip
```
- Update `pip` if required.
```shell script
pip3 install --upgrade pip
```
- Install `virtualenv`, if not installed already.
```shell script
pip3 install virtualenv
```
- Create virtual environment.
```shell script
virtualenv -p python3.6 venv
```


### Install project dependencies
- Install project dependencies using `requirements.txt`
```shell script
venv/bin/pip install -r requirements.txt
```


### Move apache2 configuration file to /etc/apache2/sites-available/
- Copy the conf file from your project root directory to `/etc/apache2/sites-available/`. You can move too instead.
```shell script
cp flask-demo.apache2.conf /etc/apache2/sites-available/flask-demo.apache2.conf
```
- Make sure the conf file name is `flask-demo.apache2.conf` and the content of the file is as follows.
```editorconfig
<VirtualHost *:80>
    ServerName <you-ip-here>
    ServerAdmin <admin@mail.com>
    WSGIScriptAlias / /var/www/flask-apache2-demo/gateway.wsgi
    <Directory /var/www/flask-apache2-demo/fake_api_gateway>
        Order allow,deny
        Allow from all
    </Directory>
    ErrorLog ${APACHE_LOG_DIR}/error.log
    LogLevel warn
    CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
```


### Enable configuration
- Enable the configurations that you made.
```shell script
sudo a2ensite flask-demo.apache2.conf
```


### Reload apache2
- Start/reload/restart apache2 to apply the changes made in configuration and/or project source code.
```shell script
sudo systemctl reload apache2
```
If this command doesn't work for you, then find for you the correct one to start/reload/restart apache2.

