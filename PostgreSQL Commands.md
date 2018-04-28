# PostgreSQL Commands
**PosrgreSQL** is a open source **Relational Database Management System (RDBMS)**. A list of **Linux** terminal commands to play with **PostgreSQL** has been listed below. <br><br>
**Get more commands** [**Here**](https://gist.github.com/Kartones/dd3ff5ec5ea238d4c546) & [**Here**](https://www.postgresql.org/docs/9.1/static/sql-commands.html) <br>
**Learn PostgreSQL Query from** [**This Tutorial**](http://www.postgresqltutorial.com/) <br>




## Index
- [Installation](#installation) <br>
- [Set Password after installation (It is a MUST)](#set-password-after-installation-it-is-a-must) <br>
- [Check PostgreSQL version](#check-postgresql-version) <br>
- [View services](#view-services) <br>
- [To Apply Services](#to-apply-services) <br>
- [Log In To PostgreSQL](#log-in-to-postgresql) <br>
- [Log Out from POstgreSQL](#log-out-from-postgresql) <br>
- [Create a Database and Database User](#create-a-database-and-database-user) <br>
- [View list of Databases](#view-list-of-databases) <br>
- [Switching Databases](#switching-databases) <br>
- [View Tables names in a Database](#view-tables-names-in-a-database) <br>




## Installation
```cmd
sudo apt-get update
sudo apt-get install postgresql postgresql-contrib
```
[Return to Index](#index)



## Set Password after installation (It is a MUST)
```cmd
sudo -u postgres psql
\password
```
[Return to Index](#index)



## Check PostgreSQL version
**Run following command from terminal**
```cmd
psql --version
```
**Or, simply run query from PostgreSQL**
```cmd
SELECT version();
```
[Return to Index](#index)




## View services
```cmd
service postgresql
```
[Return to Index](#index)



## To Apply Services
- **To start:** `service postgresql start` or `sudo /etc/init.d/postgresql start` <br>
- **To stop:** `service postgresql stop` or `sudo /etc/init.d/postgresql stop` <br>
- **To restart:** `service postgresql restart` or `sudo /etc/init.d/postgresql restart` <br>
- **To reload:** `service postgresql reload` or `sudo /etc/init.d/postgresql reload` <br>
- **To force reload:** `service postgresql force-reload` or `sudo /etc/init.d/postgresql force-reload` <br>
- **To get current status:** `service postgresql status` or `sudo /etc/init.d/postgresql status` <br><br>
[Return to Index](#index)



## Log In To PostgreSQL
**To play with Databases, you must have to Log In** <br>
```cmd
sudo -i -u postgres
psql
```
[Return to Index](#index)



## Log Out from POstgreSQL
```cmd
\q
logout
```
Or run `\q` & then press <kbd>CTRL</kbd>+<kbd>D</kbd> <br>
[Return to Index](#index)



## Create a Database and Database User
During the Postgres installation, an operating system user named postgres was created to correspond to the postgres PostgreSQL administrative user. We need to change to this user to perform administrative tasks <br>
```cmd
sudo su - postgres
```
You should now be in a shell session for the postgres user. Log into a Postgres session by typing
```cmd
psql
```
First, we will create a database for our project. Each project should have its own isolated database for security reasons.
```cmd
CREATE DATABASE myproject;
```
Remember to end all commands at an SQL prompt with a semicolon. <br><br>
Next, we will create a database user with password
```cmd
CREATE USER myprojectuser WITH PASSWORD 'password';
```
Afterwards, we'll modify a few of the connection parameters for the user we just created. This will speed up database operations so that the correct values do not have to be queried and set each time a connection is established.
```cmd
ALTER ROLE myprojectuser SET client_encoding TO 'utf8';
ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE myprojectuser SET timezone TO <'UTC+6' or 'Your_Timezone>;
```
Now, all we need to do is give our database user access rights to the database we created
```cmd
GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;
```
Exit the SQL prompt to get back to the postgres user's shell session. <br><br>
[Return to Index](#index)



## View list of Databases
```cmd
\list
```
Or simply
```cmd
\l
```
[Return to Index](#index)



## Switching Databases
```cmd
\connect <DB_Name>
```
Or simply
```cmd
\c <DB_Name>
```
[Return to Index](#index)



## View Tables names in a Database
At first connect to Database using `\c <DB_Name>` and then run
```cmd
\dt
```
[Return to Index](#index)









