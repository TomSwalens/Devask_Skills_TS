Task name:
Ansible
Task preparation:
VM with linux OS.
Task implementation:

suda apt-get install ansible

mkdir Ansible

make ansible.cfg file
make hosts file with the router ip + ssh login info
make ansible-playbook with the requested output as a result.


ansible-playbook -i hosts iosfacts.yaml 

Task troubleshooting:

While trying to launch my playbook I forgot to put hosts in my command:
ansible-playbook -i iosfacts.yaml 

After I put hosts the playbook worked fine.

Task verification:
Screenshot under Ansible
https://docs.google.com/document/d/1sJQKWfi7IL6FfIjJBT3c5zstpOfB3hE3WigJU2X5QX4/edit?usp=sharing

Output playbook:
 
devasc@labvm:~/labs/devnet-src/Devasc_Skills/Ansible$ ansible-playbook -i hosts iosfacts.yaml 
PLAY [DISCOVER IOS VERSION] ***********************************************************************************************************************************************************
TASK [run show version on remote devices] *********************************************************************************************************************************************
ok: [CSR1kv]
TASK [Save IOS version output to a file] **********************************************************************************************************************************************
changed: [CSR1kv]
TASK [Set Logging Buffer Size] ********************************************************************************************************************************************************
ok: [CSR1kv]
PLAY RECAP ****************************************************************************************************************************************************************************
CSR1kv                     : ok=3    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   