# Django - Python Web Framework



## Table of Content
- [Database Settings](#database-settings) <br>
   - [For PostgreSQL](#for-postgresql) , or <br>
   - [For MySQL](#for-mysql) , and then <br>
   - [Database Migration](#database-migration) <br>




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









