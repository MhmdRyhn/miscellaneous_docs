# Ansible

Ansible is an open source **IT Configuration Management**, **Deployment** & **Provisioning tool**.


# Table of content
- [Ansible Installation](#ansible-installation)
- [Basic configuration](#basic-configuration)



## Ansible installation
Run following commands one by one. (for **Debian** distribution of Linux)
```
sudo apt-add-repository ppa:ansible/ansible
sudo apt-get update
udo apt-get install ansible -y
```
Ansible is now installed in your system. <br> <br>
**Note:** Make sure **Python** (version 2.6 or later for Python 2 or version 3.5 or later for Python 3) is installed in your system. Because Ansible requires a Python interpreter in order to run its modules. <br>

<br> [**Return to Table of Content**](table-of-content)



## Basic configuration
Usually configuration files lies in `/etc/ansible/` directory. Ansible keeps track of all of the servers that it knows about through a hosts file (`/etc/ansible/hosts`). We need to set up this file first before we can begin to communicate with other computers. <br>

Open config file (`/etc/ansible/ansible.cfg`) with `sudo` privileges: `sudo nano /etc/ansible/ansible.cfg`. Find `[defaults]` and add the host file under this, which looks like following:
```
[defaults]
hostfile = hosts
```
***Note***: Line that starts with `#` are considered commented both in config and host file. <br><br>

Now, open the host file with `sudo` privileges: `sudo nano /etc/ansible/hosts`. This file contains the host (server) information. <br>
Hosts can be specified as **ungrouped hosts** and **grouped hosts**. Ungrouped hosts are defined before the grouped hosts. <br>
**Grouped hosts** are defined under a **group header** like below format:
```
[group_name]
host required information
```









