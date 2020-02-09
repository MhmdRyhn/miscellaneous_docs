# Ansible Playbooks
**Playbooks** are Ansible’s configuration, deployment, and orchestration **language**. Playbooks are the building blocks for all the use cases of Ansible. Playbooks are expressed in **YAML** format. Playbooks contain the steps which the user wants to execute on a particular machine. Playbooks are run sequentially.



# Table of Contents
- [Resources](#resources)
- [Basic structure of ansible playbooks](#basic-structure-of-ansible-playbooks)
- [A Simple Example to Run a Playbook](#a-simple-example-to-run-a-playbook)
- [Running Playbook Without Ansible Default Hosts and Config File](#running-playbook-without-ansible-default-hosts-and-config-file)



## Resources
- [Ansible playbooks docs (official)](https://docs.ansible.com/ansible/latest/user_guide/playbooks.html)
- [Using **YAML** file as inventory](https://docs.ansible.com/ansible/latest/plugins/inventory/yaml.html)

<br> [**Return to Table of Contents**](#table-of-contents)



## Basic Structure of Ansible Playbooks
Playbook is written in **YAML** format with a **.yml** file extension. One needs to be very careful with the format and alignment which makes it very sensitive. Each playbook is an aggregation of one or more plays in it. Playbooks are structured using **Plays**. **A Playbooks can contain multiple plays**. <br><br>

**A Playbook contains the following sections:** <br>
1. Every playbook starts with 3 hyphens (`-`) like `---`
2. **Host section** – Defines the target machines on which the playbook should run. This is based on the Ansible inventory file.
3. **Variable section** – This section is **optional** and can declare all the variables needed in the playbook.
4. **Tasks section** – This section lists out all the tasks that should be executed on the target machine. **It specifies the use of Modules**. Every task has a name which is a small description of what the task will do and will be listed while the playbook is run.
5. **Handlers** - This section is **optional**. Handlers are just like regular tasks in an Ansible playbook, but are only run if a task contains a **notify** directive and also indicates that it changed something. A handler can be **re-used multiple times** whilst our Playbook runs.

<br> [**Return to Table of Contents**](#table-of-contents)



## A Simple Example to Run a Playbook
Lets say, I have an **AWS EC2** machine and its `Public IP`: `6.61.103.114`, `Username` : `ubuntu` and the `Private key file` : `playing-with-ansible-ec2-keypair.pem`. In this machine (the host), a public repository from github will be cloned inside the `/home/ubuntu/docs/` directory (make sure the directory is empty). <br><br> 

First, configure the **hosts** file `/etc/ansible/hosts`. Open the hosts file using `sudo` privileges like `sudo nano /etc/ansible/hosts` and write the following:
```
learning-ansible ansible_host=6.61.103.114 ansible_user=ubuntu ansible_private_key_file=/home/local_machine_username/Desktop/playing-with-ansible-ec2-keypair.pem
```
Here, **learning-ansible** is the alias for your host machine. <br><br>

Then, include the `hosts` file in `/etc/ansible/ansible.cfg` file. Open the config file using `sudo` privileges and write the following under `[defaults]` section, which then look like:
```
[defaults]
hostfile = hosts
```
Then, create a playbook named `clone_repo.yml` and write the following instructions inside the playbook.
```yml
---

- hosts: learning-ansible
  
  tasks:
    - name: Clone git repo
      git:
        repo: https://github.com/MhmdRyhn/miscellaneous_docs.git
        dest: /home/ubuntu/docs/
        clone: yes
```
Now, run the playbook using the following command.
```cmd
ansible-playbook clone_repo.yml
```
When the playbook is finished executing successfully, the repository will be seen in the host machine (AWS EC2 Instance). <br>

<br> [**Return to Table of Contents**](#table-of-contents)



## Running Playbook Without Ansible Default Hosts and Config File
Create a file, say, **my_hosts** and write the following in the file. In this case we **don't** need to configure the `/etc/ansible/hosts` or `/etc/ansible/ansible.cfg` file.
```
learning-ansible ansible_host=6.61.103.114 ansible_user=ubuntu ansible_private_key_file=/home/local_machine_username/Desktop/playing-with-ansible-ec2-keypair.pem
```
Now, run the above playbook using the following command
```cmd
ansible-playbook -i /path/to/my_hosts /path/to/clone_repo.yml
```




