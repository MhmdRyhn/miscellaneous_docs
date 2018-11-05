# Django - Python Web Framework



## Table of Content
- [Start a Django Project](#start-a-django-project) <br>
- [Create an App](#create-an-app)
- [Database Settings](#database-settings) <br>
   - [For PostgreSQL](#for-postgresql) , or <br>
   - [For MySQL](#for-mysql) , and then <br>
   - [Database Migration](#database-migration) <br>
   - [Create Models From DB Table](create-models-from-db-table) <br>



## Start a Django Project
At first create and prepare [Virtual environment](https://github.com/MhmdRyhn/Miscellaneous-Code/blob/master/Python3.md#create-and-use-virtual-environment) in your desired disired directory, then enter into virtualenv using `cd` command and install required packages inside virtualenv. <br><br>
**To start a django project enter the folloing command:**
```cmd
django-admin startproject banglaidj
```
Now, run the server using following command to check whether the project is working or not.
```cmd
python3 manage.py runserver
```
Then, enter `127.0.0.1:8000` in your brouser's address bar & see the magic. <br><br>
[Return to Table of Content](#table-of-content)



## Create an App
Enter the directory where the `manage.py` file is, using `cd` command. Then enter following command:
```cmd
python3 manage.py startapp blog_post
```
After creating app, include the app in `INSTALLED_APPS` section in `settings.py` file. <br><br>
[Return to Table of Content](#table-of-content)



## Database Settings
**Note:** You have to do nothing to use **sqlite3** database. This is configured by default. You can just use it.
### For PostgreSQL
**Include following code into `<project>/<project>/settings.py` file**
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'Your_Database_Name',
        'USER': 'Your_User_Name_for_corresponding_Database',
        'PASSWORD': 'Your_Password_for_corresponding_Database',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
**Note:** Default **port** for PostgreSQL is **5432** <br>
Now, using `pip3`(pip3 is for Python3, pip is for python2) command install `psycopg2`, the PostgreSQL database connector for Django
```cmd
sudo pip3 install psycopg2
```
[Return to Table of Content](#table-of-content)

### For MySQL
**Include following code into `<project>/<project>/settings.py` file**
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Your_Database_Name',
        'USER': 'Your_User_Name_for_corresponding_Database',
        'PASSWORD': 'Your_Password_for_corresponding_Database',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```
**Note:** Default **port** for MySQL is **3306** <br>
Now, using `pip3`(pip3 is for Python3, pip is for python2) command install `mysqlclient`, the MySQL database connector for Django
```cmd
pip3 install mysqlcient
```
[Return to Table of Content](#table-of-content)

### Database Migration
At first, enter your project directory using `cd path/to/your/project` in your terminal. <br>
Now, migrate the databse
```cmd
python3 manage.py makemigrations
python3 manage.py migrate
```
Next, create **Super User**. After running the following command, it will prompt to enter **Username, Email and Password** for the **Admin** of the project or the website
```cmd
pyhton3 manage.py createsuperuser
```
Next, **run the server** and enjoy
```cmd
python3 manage.py runserver
```
[Return to Table of Content](#table-of-content)

### Create Models From DB Table
Follow the steps below
1. Login to PostgreSQL
```cmd
sudo -i -u postgres
psql
```
2. Connect to your desired DB
```cmd
\c <DB_Name>
```
3. Grant all permission to DB
```cmd
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO db_username;
```
4. Now, enter following command & get a `filename.py` file in your working directory
```cmd
python3 manage.py inspectdb > filename.py
```
[Return to Table of Content](#table-of-content)








