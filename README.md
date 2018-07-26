###### Pedro Oliveira Homework - 2018.07.23

##Deploy Server with Main System Information
#####Required Tools: Ansible, Python
#####Goal:
* Create a process for automatic deployment of a system backend application that shows system information
* Nginx server is installed too and is used as a reverse proxy in front of the application and provides SSL communication based on self-signed certificate

#####Instructions:
* Implement as much as possible
* Instantiation of the host (e.g. creating the machine in a cloud) is NOT part of the task
* Use latest Ansible to create roles and playbooks for the goal


#####Implemented items:
* Web server is installed on the machine
* Server can be accessible from your local computer using hostname not just ip
* Web page shows IP of the machine and whether numbers are odd or even
* Web page shows current date
* Web page shows current time
* Web page shows usage of CPU of the machine
* Service management is configured (start, stop, restart, status)
* Tools like supervisord may be used for this

#####Results:
* All source codes in Github (or some other public git repository) 
* Readme.MD documentation how to use it
* Found problems, not implemented features, etc. should be mentioned there

#####Assessment:
* It is up to the developer and required level how much is 100% automatic and scripted
* Manual steps are considered as minus

##Installation process:

### Contents description:
Inside the folder PedroOliveiraHomework you will find the following files:

```
addServerToHosts.sh
roles (folder)
playbook.yaml
README.MD
```
* __addServerToHosts.sh__ scritp aimed to prepare your local machine
* __roles__ contains the ansible roles files/folders
* __playbook.yaml__ the ansible playbook 
* __README.MD__ readme file


### Prepaging the local machine

In order to prepare your local machine please run the script ```addServerToHosts.sh```, pass the two arguments needed, ```hostname``` and ```IP``` (in this specific order).

E.g.:

```
addServerToHosts.sh myUnixServer 192.168.1.10
```

The result of the script is that both your Ansible hosts file and local machine hosts file will have a new entry (your target machine). This will allow you to reach your target server by its IP or hostname and also will allow Ansible to recognise the host.

Overall your local hosts file will have the new entry(e.g.):

```
[...content already present on your file...]
192.168.1.10 myUnixServer myApp
```

and your ansible hosts file will have(e.g.):

```
[...content already present on your file...]
[myUnixServer]
192.168.1.10
```

###Running the Ansible-playbook

_NOTE: In order to sucessfully deploy this application you have to have a user with access to the target server using ***ssh*** , ***sudo*** priviledges and also that ***ansible*** is installed._

To run the playbook execute the following command from the root folder of this project:

_NOTE: replace USER and PASSWORD. If your server does not requiere sudo password leave PASSWORD empty._

```
ansible-playbook playbook.yaml -i hosts -u USER --extra-vars "ansible_sudo_pass=PASSWORD" -v
```

Once the playbook finishes, type in your browser ``` flaskwpage.me```.

###Supervisord

Nginx and the flaskwpage can be managed by supervisord.

E.g.:

```
supervisorctl start nginx
```
```
supervisorctl start flaskwpage
```