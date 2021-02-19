

### Inventory  
  - Collection of hosts  
  - Groups / Child Groups ( no Dashes only underscores )  
    [india:delhi]  
  - Written in INI or YAML  
  - Static Inventory  
  - Dynamic Inventory ( automatically generated and updated )  

### Location of Inventory    
   Controlled by ansible config
   > ~/.ansible/ansible.cfg

    
## Hosts and Ranges
  - Ranges match  all values from [START:END]  
  - 192.168.[4:7].[0:255] 
    server[01:10].domain.com
    [a:c]name.domain.com
    
 List an inventory in yaml format     
  > ansible-inventory -y --list


## Ansible
 - Configuration file 
 - Connection Control
 - Use priviledge escalation
 
  ### Ansible Configuration ( ansible --version )
    i) ENV Variable - ANSIBLE_CONFIG set to path
    ii) Current working dir
    iii) ~/.ansible.cfg
    iv) Else default location
    
  ### Connection Settings
  
    Setting to control the SSH can go into the [defaults] section  
    - remote_user
    - remote_port 
    - ask_pass ( use key based auth )
    
  #### Priviledge Escalation   
   
     |Item | Description |  
     |---|---|  
     |become|1.1.1.1|  
     |become_user|user to switch to on the managed host|  
     |become_method| (sudo ) how to become that user by sudo)default) or su etc|  
     |become_ask_pass|false|  
     
     ```
       --- < Sample ansible.cfg > ---
     [defaults]
     inventory = ./inventory
     remote_user = ansible
     become_ask_pass = false
     
     [priviledge_escalation]
     become = true  
     become_user = root  
     become_ask_pass = false  
     ```
    
    
        
 ## Host-Based Connection Variables
   - place setting in a file in the host_vars dir in the same as inventory file.  
   - hosts should appear with those names in the inventory  
   - these settings override the ones in ansible.cfg  
   
   |Item | Description |
   |---|---|
   |ansible_host|1.1.1.1|
   |ansible_port|34101|
   |ansible_user|root|
   |ansible_become|false|
   
   ```
   project   
    |--ansible.cfg  
    |--host_vars  
    |    |--server1.com  
    |--inventory  ( has mention by same hostname as file inside the host_vars )  
   ```
 
 
  > ansible <group> --limit <host> -m ping  
  
  > ansible-config dump --only-changed    
  > ansible -m user -a'name=nebiw uid=40 state=present' server.com  


## Ansible Adhoc
 Some adhoc command line params for override  
 
 |Item|Desc|  
 |---|---|
 |-k| prompt for the conn password|
 |-u| override the remote_user setting in ansible.cfg|
 |-b| enable priviledge esc , become:yes|
 |-K| prompt priviledge escalation password|
 |--become-method| sudo by default|
 
 
 
  > ansible all -m ping
  > ansible -