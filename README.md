# IAIDSWebsite

## Just get this running:
Go into the **IAIDSWebsite Directory** in your Windows or Linux Terminal and run
```
vagrant up
```
This will run vagrant bash script and it would look for a **"Vagrantfile"**, which would find and configure the machine.
Once the machine runs, you can go ahead and 
```
vagrant ssh
```
into the machine.  
Then run
```
cd IAIDSWebsite
```
 to change the directory. Once you're in the directory, run
```
startupScript.sh
```
 command to run the server.

## Refreahing the DB

If the database gets curropted were you have to start from scratch just run
```
cd IAIDSWebsite
refreshDB.sh
```

## Vagrant GUI Trigger
Cool tip: If you don't want a gui interface for vagrant, just edit the **Vagrantfile** and set v.gui = false, or vice versa. It will trigger the gui interface to be on or off. It will be located here: 

```
config.vm.provider "virtualbox" do |v|
    v.gui = false
    v.name = "IAIDSVM"
    v.memory = 2048
    v.cpus = 1
    v.customize ["modifyvm",:id,"--natdnshostresolver1","on"]
  end
```
If you decided to not use the GUI, just 
```
vagrant ssh
```
 into the machine. You will be able to just use the VM just like any other computer
 
 
## Windows Developers:
For those who are developing on Windows: 
The VM environment has this issue if you're on Windows, any shell scripts wouldn't be able to run. To fix this issue, go on the vagrant machine and run
```
sudo apt install dos2unix
```
 Then once you install it, run 

```
dos2unix provision.sh
```
 or
``` 
dos2unix startupScript.sh
```
 to fix the issue.
You will be able to run the script like this: 
```
./provision.sh
```
 or
``` 
./startupScript.sh
```
pip3 install -r ./requirements.txt
```
```
