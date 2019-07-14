# Ansible Inventory
Ansible inventory can be defined in two ways - **INI** like format and **YAML** format. <br>
**Note**: **Indentation** is important in **YAML** file. Use **2 spaces** for indentation. 



## Table of Contents
- [The **INI** Inventory](#the-ini-inventory)
- [Equivalent **YAML** format of above **INI** like inventory](#equivalent-yaml-format-of-above-ini-like-inventory)
- [Equivalent **YAML** format of above **INI** like inventory **2**](#equivalent-yaml-format-of-above-ini-like-inventory-2)



## The INI Inventory
Bellow is a sample **INI** like inventory file. Lets say, name of the file is `my_hosts`:

```
green.example.com ansible_host=10.0.101.100
blue.example.com
192.168.100.1
192.168.100.10

[webservers]
alpha.example.org
beta.example.org ansible_host=192.168.200.122
192.168.1.100
192.168.1.110
www[001:006].example.com

[webservers:vars]
nginx_http_port=80
nginx_https_port=443

[dbservers]
db01.intranet.mydomain.net
db02.intranet.mydomain.net
10.25.1.56
10.25.1.57
db-[99:101]-node.example.com
```
[**Return to Table of Contents**](#table-of-contents)



## Equivalent YAML Format of Above INI Like Inventory
Bellow is the **YAML** eqivalent of the above **INI** like file. Lets say, the name of file is `inv.yml`

```
---

all:
  hosts:
    green.example.com:
      ansible_host: 10.0.101.100
    blue.example.com:
    192.168.100.1:
    192.168.100.10:
  children:
    webservers:
      hosts:
        alpha.example.org:
        beta.example.org:
          ansible_host: 192.168.200.122
        192.168.1.100:
        192.168.1.110:
        www[001:006].example.com:
      vars:
        nginx_http_port: 80
        nginx_https_port: 443
    dbservers:
      hosts:
        db01.intranet.mydomain.net:
        db02.intranet.mydomain.net:
        10.25.1.56:
        10.25.1.57:
        db-[99:101]-node.example.com:
```
[**Return to Table of Contents**](#table-of-contents)



## Equivalent YAML Format of Above INI Like Inventory 2
Bellow is another way of representing the **YAML** format inventory of the above **INI** like inventory. Lets say, the name of file is `inv.yml`

```
---

ungrouped:
  hosts:
    green.example.com:
      ansible_host: 10.0.101.100
    blue.example.com:
    192.168.100.1:
    192.168.100.10:

webservers:
  hosts:
    alpha.example.org:
    beta.example.org:
      ansible_host: 192.168.200.122
    192.168.1.100:
    192.168.1.110:
    www[001:006].example.com:
  vars:
    nginx_http_port: 80
    nginx_https_port: 443

dbservers:
  hosts:
    db01.intranet.mydomain.net:
    db02.intranet.mydomain.net:
    10.25.1.56:
    10.25.1.57:
    db-[99:101]-node.example.com:
```
[**Return to Table of Contents**](#table-of-contents)



