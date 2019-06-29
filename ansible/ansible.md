# Ansible

Ansible is an open source **IT Configuration Management**, **Deployment** & **Provisioning** tool. <br><br>



# Table of contents
- [Resources (Docs/articles/blogs)](#resources)
- [Ansible Installation](#ansible-installation)
- [Basic configuration](#basic-configuration)
- [Check connection](#check-connection)



## Resources
- Configuration: [Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-ansible-on-ubuntu-18-04)

<br> [**Return to Table of Contents**](#table-of-contents)



## Ansible installation
Run following commands one by one. (for **Debian** distribution of Linux)
```
sudo apt-add-repository ppa:ansible/ansible
sudo apt-get update
sudo apt-get install ansible -y
```
Ansible is now installed in your system. <br> <br>
**Note:** Make sure **Python** (version 2.6 or later for Python 2 or version 3.5 or later for Python 3) is installed in your system. Because Ansible requires a Python interpreter in order to run its modules. <br>

<br> [**Return to Table of Contents**](#table-of-contents)



## Basic configuration
Usually configuration files lies in `/etc/ansible/` directory. Ansible keeps track of all of the servers that it knows about through a hosts file (`/etc/ansible/hosts`). We need to set up this file first before we can begin to communicate with other computers. <br>

Open config file (`/etc/ansible/ansible.cfg`) with `sudo` privileges: `sudo nano /etc/ansible/ansible.cfg`. Find `[defaults]` and add the host file under this, which looks like following:
```
[defaults]
hostfile = hosts
```
**Note**: Line that starts with `#` are considered commented both in config and host file. <br><br>

Now, open the host file with `sudo` privileges: `sudo nano /etc/ansible/hosts`. This file contains the hosts (servers) information. Hosts can be specified as **ungrouped hosts** and **grouped hosts**. Ungrouped hosts are defined before the grouped hosts. <br>
**Grouped hosts** are defined under a **group header** like below format:
```
[group_name]
host required information
```
<br> **Host information is declared in the following way (for both ungrouped and grouped hosts):** <br>
- If host machine is reached using **public key authentication**, then
```
<host's_ip> ansible_user=<host_machine's_username> ansible_private_key_file=/path/to/the/private/file
```
Or, an **alias** can also be used
```
<alias> ansible_host=<host's_ip> ansible_user=<host_machine's_username> ansible_private_key_file=/path/to/the/private/file
```
**Note:** Make sure that **others** don't have any accesss permission to the **private key file**. Minimal required access permission is **Read Access for the Owner**. To procees with minimal requirements, you can do like `sudo chmod 400 <private_key_file_name>`

- If host machine is reached using **username** and **password**, then
```
<host's_ip> ansible_user=<host_machine's_username> ansible_pass=<host's password>
```
Or, an **alias** can also be used
```
<alias> ansible_host=<host's_ip> ansible_user=<host_machine's_username> ansible_pass=<host's password>
```

<br> [**Return to Table of Contents**](#table-of-contents)



## Check connection
<br> **Test whether the host are reachable or not by the ansible** <br>

- To check for all the hosts:
```
ansible -m ping all
```
- To check for all a group of hosts:
```
ansible -m ping <host_group_name>
```
- To check for individual host:
```
ansible -m ping <host_IP__or__host_alias>
```
To check for several individual hosts (separate hosts using colon(`:`)):
```
ansible -m ping <hist1:host3....:hostn>
```
**In response of PING**, for **each successfully reachable** hosts, there will be a response like following format:
```
<host_IP__or__alias> | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python3"
    }, 
    "changed": false, 
    "ping": "pong"
}
```

<br> [**Return to Table of Contents**](#table-of-contents)









