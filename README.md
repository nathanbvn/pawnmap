# Pawnmap
Pawnmap is an advanced penetration testing tool that extends the functionality of Nmap by integrating vulnerability detection and exploitation checks. It automates port scanning and correlates discovered services and versions with known vulnerabilities, making it a powerful asset in security assessments and red teaming engagements.


## Set Up
```
git clone https://github.com/nathanbvn/pawnmap.git

# Make it excecutable
chmod +x pwnmap.py

# Then create a symbolic link to be able to use it as a command :
sudo ln -s PwnMap/pwnmap.py /usr/local/bin/pwnmap

# Install Dependecies
pip install -r requirements.txt
```


## Format 

```
pwnmap -no <nmap options> -t HOST -o output.txt 

```
## Arguments 
- `-no / --nmap-options` : Nmap options you want to use (ex. -no "-T4 -Pn -p-")
- `-t / --target` : The host you want to target (ex. -t 192.168.56.1)
- `-o / --output` : Save the scan in a text file (ex. -o scan.txt, by default = "scan_result.txt")
- `-f / --file` : Open Pawnmap with a nmap grepfile scan (ex. -f scan.txt) 


## Commands 

`sc <portNumber>` (-v, -s, -t) : Searches an exploit with this service version
- '-v' : choose specified version
- '-s' : service alone no version specified
- '-t' : specify exploit type (RCE, Injection, XSS ...)
- '-o' : custom search

`get <save_number> (-e)` : get the exploit code / info 
- '-e' : get exploit without saving

`save <exploit_number ` : save exploit title / URI for later 

`ls` : show save list

`ll` : Show Exploit list 

`clear` : clear screen and retrieve nmap result


## Use case 
### *Search the vulnerabilities in a service*
![image](https://github.com/user-attachments/assets/df7e1a35-fe85-48cd-bfed-9da00518e490)


### *Get the exploit info*
![image](https://github.com/user-attachments/assets/c0839e49-cd29-4d4c-95c9-8733b0b0171e)


### *Make a precise search for version*
![image](https://github.com/user-attachments/assets/f285c719-439d-4a88-906d-5cb11b1b19fe)


### *Prepare an attack plan by saving different exploits that can be useful in the saves list*
![image](https://github.com/user-attachments/assets/2426f71c-b0a4-4d0f-ae64-bebe0823c6f8)
