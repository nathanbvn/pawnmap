# Pawnmap
Pawnmap is an advanced penetration testing tool that extends the functionality of Nmap by integrating vulnerability detection and exploitation checks. It automates port scanning and correlates discovered services and versions with known vulnerabilities, making it a powerful asset in security assessments and red teaming engagements.



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
