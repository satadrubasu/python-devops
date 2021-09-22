## 1. Setting up Ansible on control Node 
  > python3 -m pip install ansible 

## 2. Ansible Configuration File ( Controlling COnnections to Managed Hosts )
  Set defaults on : 
  |Sno|Description|
  |---|---|
  |1|Location of inventory file|
  |2|Connection protocol to use (SSH)|
  |3|if a non-standard network port to connect to server|
  |4|what user is can login as|
  |5a|if user is not root - if Ansible should escalate to root|
  |6b|How ansible becomes root - default sudo|
  |6c|Prompt for an SSH password to login/sudo or use keys|
  

### 2.1 Load of config priority for ansible.cfg ( ansible --version )  
  
    > ansible --version  (SHows the configuration in use )
     
   - ENV Variable - ANSIBLE_CONFIG set to path  
   - current working dir  
   - ~/.ansible.cfg  
   - Else default location : /etc/ansible/ansible.cfg  

### 2.2 ansible.cfg SECTIONS :   
   ```
   [defaults]
   inventory = ./inventory
   remote_user = ubuntu
   remote_port = 22 ( default ssh )
   ask_pass
   [priviliedge_escalation]
   become = false | true ( by default be the become_user or not )
   become_user = root ( default ) what user on the mansged host Ansible shud become
   become_method = sudo ( default ) or su
   become_ask_pass = no ( default) if ask for pwd
   
   ```
 
 ### 2.3 ansible.cfg ( HOST based variables )  
  The inventory should have same hostname as the filename in host_vars.    
 
 ```
   Base Folder
    |-- ansible.cfg
    |-- host_vars
    |    |-- server1.aws.com
    |    |-- server2.aws.com
    |-- inventory ( has mention by same hostname as file inside the host_vars )
  ``` 
  
   Content of the host_override_file ( server1.aws.com )  
     these settings override the ones in ansible.cfg    
  
   ```
    ansible_host= different ip or hostname to use for the connection to host overriding inventory
    ansible_port=
    ansible_user=ubuntu
    ansible_become=true
    ansible_become_user=root
    ansible_become_method=sudo
   ```
  
   

### 2.4 Inventory  
  - Collection of hosts  
  - Groups / Child Groups ( no Dashes only underscores )  
    [india:delhi]  
  - Written in INI or YAML  
  - Static Inventory  
  - Dynamic Inventory ( automatically generated and updated )  
  
  ```
  [web]
  web01
  web02
  
  [databases]
  db[01:02]
  
  ```

    
### 2.5 Hosts and Ranges
  - Ranges match all values from [START:END]  
  - 192.168.[4:7].[0:255] 
    server[01:10].domain.com
    [a:c]name.domain.com
    
 List an inventory in yaml format     
  > ansible-inventory -y --list
  > ansible <group> --limit <host> -m ping  
  > ansible-config dump --only-changed    
  > ansible -m user -a'name=nebiw uid=40 state=present' server.com  


 ## 3 Ansible Adhoc Commands
 Some adhoc command line params for override  
  > ansible host-pattern -m module [-a 'module args'] [-i inventory]  
  > ansible all -m ping
  
|Command|description|
|---|---|
|ansible --version| confirm the ansible.cfg file that will be loaded during execution from this location|
|ansible all -i inventory -m ping|ping all hosts in  inventory|
|ansible all --limit web01 -i inventory -k -m ping| limit server and seek password|
|ansible-doc -l \| grep ping | check the documentatin of the ping module |
  
 
 |Item|Desc|  
 |---|---|
 |-k| --ask-pass prompt for the conn password|
 |-u| override the remote_user setting in ansible.cfg|
 |-b| become:True |
 |-K| --ask-become-pass prompt priviledge escalation password|
 |--become-method| sudo by default|
 
### Common Modules  
  
 >  ansible all -m package -a'name=httpd state=present'  
 >  ansible localhost -m command -a /usr/bin/hostname
 >  ansible localhost -m shell -a /usr/bin/hostname
  
  
## 4. Ansible Playbooks (.yml 2 spaces )
 
 > ansible-playbook sample.yml --limit server2
 > ansible-playbook --syntax-check sample.yml  
 > ansible-playbook -C sample.yml   (dry run) 
  
 ```
 ---
 - name : Example playbook
   hosts: all 
   become: yes
   tasks:
     - name: user exists with UIO 4000
       user:
         name: newuser
         uid: 4000
         state: present
 ```
 
### 4.1 Playbook Variables (letter | number | _ only ):
  
  Scope:  
   Global -> every host  
   Host -> Host specific  
   Play -> all hosts in current play (local file )  
  
```
  - hosts: all
    vars: 
      user_name: sat
      user_state: present
```
  
  OR  
  
```
   - hosts: all
     vars_files:
       - vars/users.yml
```
  
  To use the variable : 
  
```
  tasks:
  - name: Create the user {{ user_name }}
    user:
      name: "{{ user_name }}"
```
  
### 4.2 Host Variables & Group Variables
    
```
   project
     |-- inventory
     |     |-- host_vars/
     |             |------ server1.aws.com
     |             |------ server2.aws.com
     |     |-- group_vars/
     |             |------ all
     |             |------ datacenter-1
     |--- playbook.yml
```
  
### 4.3 Defining Variables in Playbooks  
    The packages will expand to the list provided in vars and auto loop through.  
  
```
    - name: Install Packages
      hosts: all
      vars:
        packages:
          - httpd
          - nmap
          - mod_ssl
      tasks:
        - name: Install software
          yum:
            name: "{{ packages }}"  
```
   
### 4.4 Capture Output with Register  
  
## 5. Sensitive Data (Encrypted files )  
  
  Will need a password to work with :  
  
   |Command|Desc|
   |---|---|
   |ansible-vault create filename|Create new|
   |ansible-vault view filename|view |
   |ansible-vault edit filename|edit |
   |ansible-vault encrypt existingfile |encrypt existing non encrypted|
   |ansible-vault decrypt filename |decrypt|
   |ansible-vault rekey filename |change password|  
   
   > ansible-playbook --vault-id @prompt filename  
  
  ```
  vi mysecret.file   
  secretpassword: catchme@123   
  ```  
  
  Encrypt and use the value for secretpassword:  

  > ansible-vault encrypt mysecret.file  
  
 ```
   tasks:  
     - name: Load variable from encrypted file  
       include_vars:  
         file: mysecret.file  
     - name: Display the encrypted variable  
       debug:  
         msg: "{{ secretpassword }}"  
 ```
 
  To ensure the vault password is asked before execution  
  > ansible-playbook --ask-vault-pass sample.yml
  
  

  
  
  
  
  
  
  
