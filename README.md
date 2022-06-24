# Welcome To God Genesis
![FinalGod](https://user-images.githubusercontent.com/66937297/175554898-58c56076-7cf9-4b1d-9d5d-2f2b27a9c0e3.png)

God Genesis is a C2 server purely coded in Python3 created to help Red Teamers and Penetration Testers. 
Currently It only supports TCP reverse shell but wait a min, its a FUD and can give u admin shell from any targeted WINDOWS Machine.

The List Of Commands It Supports :-

```
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


```


# Features Of Our Framework :-
Check The Video To Get A Detail Knowledge
```
1. The Payload.py is a FULLY UNDETECTABLE(FUD) use your own techniques for making an exe file. (Best Result When Backdoored With Some Other Legitimate Applictions)
2. Able to perform privilege escalation on any windows systems.
3. Fud keylogger
4. 2 ways of achieving persistance 
5. Recon automation to save your time.

```


How To Use Our Tool : 

```
git clone https://github.com/SaumyajeetDas/GodGenesis.git

pip3 install -r requirements.txt

python3 c2c.py

```

It is worth mentioning that [Suman Chakraborty](https://github.com/ANON4MOUS)
have contributed in the framework by coding the the the Fud Keyloger, Wifi Password Extraction and Chrome Password Dumper modules. 


https://user-images.githubusercontent.com/66937297/175561859-a0e9f9dd-1e59-46da-a8e9-197d800bee37.mp4






## Dont Forget To Change The IP ADDRESS Manually in both c2c.py and payload.py

