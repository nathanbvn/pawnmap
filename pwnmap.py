#!/usr/bin/env python3
import argparse
import requests
import subprocess
import bs4
import re
import readline


readline.parse_and_bind("tab: complete")
readline.parse_and_bind("set editing-mode emacs") 
readline.parse_and_bind("set enable-keypad on")

HISTORY_FILE = ".pwnmp_history"
try:
    readline.read_history_file(HISTORY_FILE)
except FileNotFoundError:
    pass

parser = argparse.ArgumentParser(description="A pwnmap script")

parser.add_argument('-no','--nmap-options', type=str, help='Options for nmap, e.g., -T4 -Pn -p-', default='')
parser.add_argument('-t','--target', type=str, help='Target for nmap scan')
parser.add_argument('-o','--output', type=str, help='Output file name', default='scan_results.txt')
parser.add_argument('-f','--file', type=str, help='Open scan file (grep mode)')

args = parser.parse_args()

if args.file == None :
    print(f"nmap options: {args.nmap_options}")
    print(f"Target: {args.target}")
    print(f"Output file: {args.output}")


    command = f"nmap {args.nmap_options} -sV {args.target} -oG {args.output}"
    nmap = subprocess.run(command, capture_output=True, text=True, shell=True)

    nmap_output = nmap.stdout
    print(nmap_output)

    file = args.output
    try :
        nsplit = nmap_output.split("VERSION")[1].split("MAC")[0].split("\n\n")[0].split("Service")[0]+"\n"
    except : 
        nsplit = nmap_output

else :
    file = args.file
    f = open(file,"r",encoding='utf-8')
    a = f.read().split("Ports: ")[1].split("# Nmap done")[0]
    nsplit = '\n'
    for i in a.split(", "):
        nsplit += i.replace("open/","").replace("//","    ")[:-1]+'\n'
        print(i.replace("open/","").replace("//","    ")[:-1])



fileread = open(file,"r",encoding='utf-8')
fileread = fileread.read()
print(" \n \npwnMap console ...")

try : 
    result = fileread.split("Ports:")[1].split("# Nmap ")[0]
except :
    result = "Error"

d = {}

for i in result.split(", "):
    try : 
        d[i.split("/")[0].strip()] = i.split("//")[2].split("/")[0]
    except :
        pass

choice = ""
exploits = {}
saves = []

while choice != "exit":
    BOLD = "\033[1m"
    RED = "\033[0;33m"
    RESET = "\033[0m"
    UNDERLINE = "\033[4m"

    choice = input(f"{RED}{UNDERLINE}{BOLD}pwnmp{RESET} {RED}{BOLD}>{RESET} ")
    if "sc" in choice:
        try : 
            service = d[choice.split(" ")[1]]

            if '-t' in choice or '-v' in choice or '-s' in choice : 
                serviceV = d[choice.split(" ")[1]]
                service = ""
                for j in serviceV :
                    if ord(j) <= 57 and ord(j) >= 48:
                        break
                    else : 
                        service+=j


            # choose custom version
            if '-v' in choice:
                newVersion = choice.split("-v")[1].strip()
                service += newVersion
            

            #choose exploit type
            elif '-t' in choice : 
                newVersion = choice.split("-t")[1]
                service += newVersion

            #custom search
            elif '-o' in choice :
                service = choice.split("-o")[1]


            print("\nLooking for exploits using : ",service)
            commandsearch = f"searchsploit {service}"

            searchsploit = subprocess.run(commandsearch, capture_output=True, text=True, shell=True)
            searchsploit_output = searchsploit.stdout

            print(searchsploit_output)

            ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')

            exploits = {}
            for cpt, line in enumerate(searchsploit_output.splitlines()[3:]):  
                line = ansi_escape.sub('', line).strip()
                if "|" in line:
                    parts = line.split("|")
                    if len(parts) >= 2:
                        title = parts[0].strip()
                        uri = parts[1].strip()
                        exploits[cpt] = {"title": title, "uri": uri}
        except : 
            print("Error\n")

    
    elif "clear" in choice:
        subprocess.run("clear",shell=True)
        print(nsplit)
    
    elif "ll" in choice:
        print(" Exploit List : ")
        for i in exploits : 
            print(i,exploits[i])

    elif 'ls' in choice:
        print("Saves List : ")
        cpt = 0
        for i in saves:
            print(cpt,i)
            cpt+=1

    elif 'save' in choice:
        save_number = choice.split(" ")[1]
        print(exploits[int(save_number)],"saved")
        try : 
            saves.append(exploits[int(save_number)])
        except : 
            print("Error saving the exploit")

    elif 'get' in choice: 
        save_number = choice.split(" ")[1]

        if '-e' in choice:
            try :
                exploitChosen = exploits[int(save_number)]
            except : 
                print("No exploit found for this number\n")

        else : 
            try :
                exploitChosen = saves[int(save_number)]
            except : 
                print("No exploit found for this number\n")


        try : 
            print("Fetching exploit",exploitChosen['title'])
            uri = exploitChosen['uri']

            code = uri.split("/")[2].split(".")[0]

            url = 'https://www.exploit-db.com/exploits/'+code

            print(url,"\n\n")
            headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
                }
            response = requests.get(url, headers=headers)

            soup = bs4.BeautifulSoup(response.text, 'html.parser')

            code_content = soup.find('code').get_text()
        except : 
            code_content = "Error finding the exploit.\n"

        print(code_content)
    readline.write_history_file(HISTORY_FILE)