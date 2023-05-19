quick note

use greater than symbol
ansible with items
ansible-playbook playbook --list-host


# Training Ansible

Create a python virtual environment.

<code> python3 -m venv venv </code>

Switch to environment.

<code> source venv/bin/active </code>

install ansible

<code>pip install ansible</code>




## Need to know commands for Ansible
view info about your ansible

<code> ansible --version </code>
<blockquote>
Output

*ansible [core 2.11.2]

    config file = /etc/ansible/ansible.cfg
    configured module search path = ['/home/angella/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
    ansible python module location = /home/angella/Programming/Infrastructure-as-Code/venv/lib/python3.8/site-packages/ansible
    ansible collection location = /home/angella/.ansible/collections:/usr/share/ansible/collections
    executable location = /home/angella/Programming/Infrastructure-as-Code/venv/bin/ansible
    python version = 3.8.10 (default, Jun  2 2021, 10:49:15) [GCC 10.3.0]
    jinja version = 3.0.1
    libyaml = True
  </blockquote>


## Good to know

Functions of Ansible
- Application Deployment
- Multi-tier Orchestration
- Configuration Management
- Provisioning
- CICD Pipeline

Parts of Ansible 
- Playbook
  - Written in YAML
  - Tasks are executed sequentially
  - uses Ansible Modules
  - plays are ordered sets of tasks to execute against host selection from your inventory
  - a playbook is a file containing one or more plays.  
  ![Picture of Ansible playbook](../../images/Ansible-playbook.png)
- Modules
  - Bit of code/Tools in your toolkit
  - python, powershell, or any language 
  - You don't know to know how it work, just how to structure the task you give it
  - You can go on Ansible website and find the whole list of modules
  - SIDE NOTE
    - Sometime you make need to use runtime command modules that just pass commands to the devices
    - Examples are Shell, command, Raw (use if no python is on the end device) and scripts
- Inventory
  - Can come from a lot of different places
  - you can use your own CMDB
- Plugins ( I dont fully understand yet...)
  - python api
  - code that plugs into the core engine  
  
You can run the following to check you syntax  
<code> ansible-playbook {Playbook name} --syntax-check </code>


## Questions

When would you use Jinja Templating vs the cisco IOS module?
- you would use both. the power of a template is that you can update the task in one spot and have logic built into the template that you cant build into the task.
- seems like the best idea would be to use jinja template as you main config.

What is the best method for Idempotency and hashed/encrypted config?
example a secret username on a cisco device( password is encrypted)


What is the best method for ACL where a cisco devices does not keep the ACL in the order you want it to?
Example is a standard ACL moves remarks and host ip address around.


What is the best idea for having your custom Ansible config file?
Issue. when I run a playbook from a different folder it uses that the default config file instead of the 
- If you place an Ansible config file in your directory you are currently in. That will become your new Ansible config. If you don't put the Ansible config file in the directory you are in, the default will be in  /etc/ansible/ansible.cfg


is it best to use different role based on different switches
- IE one role for ios vs nexus?

What is a meta tag?

## Variables 

vars is a Keyword inside of ansible that you can create variables. you can use the vars keyword inside a playbook, inventory file, tasks, ect.

What is the highest precedence for Ansible vars
1. Extra Vars
2. Task Vars
3. Block Vars
4. Role and Included vars
5. Play var_files
6. Play Var_prompt
7. Play vars
8. Set_facts
9. Registered Vars
10. Host facts
11. Playbook host_vars
12. Playbook group_vars
13. Inventory host_vars
14. Inventory group_vars
15. Inventory vars
16. Role defaults

### task types
Normal tasks
- They will run sequentially  
Handler tasks
- Handlers are special tasks that run at the end of a play if notified by another task.
- if a configuration file get changed notify a service restart task it needs to run
- They will only run once at the end of a play. no matter how many times they have been triggered
- See bottom for an example


### Loops
- easiest way is {{ item }} then with_items: and list of items 
- see code below


### Roles
structure of a role directory
you can create this by hand or with the ansible galaxy command
<code> 
mkdir roles
cd roles/
ansible-galaxy init {role name}
</code>

roles/
  common/
    files/
    templates/
    tasks/
    handlers/
    vars/
    defaults/
    meta/
  switch/
    files/
    templates/
    tasks/
    handlers/
    vars/
    defaults/
    meta/

Common is for all if your devices, generally  this is true.  
you can create different tasks inside your role but Ansible will not pick them up by default. You will need to create a task, give it a unique name. Then in the main.yml task include any task you want and preform and include of the uniquely named yaml files.





Tips for using quotes in playbooks\tasks
1. if I have Jinja variable(eg {{ Variable_name }}) at the beginning or end of the line; otherwise YAML will parse the line as nested objects due to the braces.
2. If there are any colons in the string. (eg in urls)



NOTES
By default, ansible will stop all playbook execution when a task fails, and won't notify any handlers that may need to be triggered. In some cases, this leads to unintended side effects. If you want to make sure handlers always run after a task use notify to call the handler, if the playbook fails, add --force-handlers to your ansible-playbook command.



how to call a role from a playbook
---
- hosts: switches
  roles:
    - common
    - switch

Ansible must know
- register
- changed_when: false


### Handler example
<code>
tasks:
  - name: add cache dir
        file:
      path: /opt/cache
      state: directory
  - name:install nginx
    yum:
      name: nginx
      state: latest
    notify: restart nginx

handlers:
  - name: restart nginx
    service:
      name: nginx
      state: restart 

</code>


### Loop example
Basic
<code>
- name: install python bindings for SELinux
  yum: name={{item}} state=present
  with_items:
  - libselinux-python
  - libsemanage-python
</code>

Slightly more advanced
<code>
- name: Default config
  include_tasks: '{{ defaultconfigtasks }}'
  loop:
    - ../tasks/ntpconfig.yml
    - ../tasks/interfacesettings.yml
    - ../tasks/l3interface.yml
    - ../tasks/snmpcreate.yml
    - ../tasks/copyrunstart.yml  
  loop_control:
    loop_var: defaultconfigtasks
</code>