# Ansible Playbooks
**Playbooks** are Ansible’s configuration, deployment, and orchestration **language**. Playbooks are the building blocks for all the use cases of Ansible. Playbooks are expressed in **YAML** format. Playbooks contain the steps which the user wants to execute on a particular machine. Playbooks are run sequentially.



# Table of Contents
- [Resources](#resources)
- [Basic structure of ansible playbooks](#basic-structure-of-ansible-playbooks)



## Resources
- [Ansible playbooks docs (official)](https://docs.ansible.com/ansible/latest/user_guide/playbooks.html)

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




