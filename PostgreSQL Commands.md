# PostgreSQL Commands
**PosrgreSQL** is a open source **Relational Database Management System (RDBMS)**. A list of **Linux** terminal commands to play with **PostgreSQL** has been listed below. <br>
**Get more commands** [**Here**](https://gist.github.com/Kartones/dd3ff5ec5ea238d4c546) & [**Here**](https://www.postgresql.org/docs/9.1/static/sql-commands.html) <br>



## Index
- [Installation](#installation) <br>
- [Set Password after installation (It is a MUST)](#set-password-after-installation-it-is-a-must) <br>
- [View services](#view-services) <br>
- [To Apply Services](#to-apply-services) <br>
- [Log In](#log-in) <br>
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



## Log In
**To play with Databases, you must have to Log In** <br>
```cmd
sudo -i -u postgres
psql
```
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









