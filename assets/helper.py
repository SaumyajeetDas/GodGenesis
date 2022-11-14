from rich.table import Table
from rich import print as xprint


def main_help():
    basic_commands_table = Table(show_header=True, header_style="bold white")
    basic_commands_table.add_column("Command", style="dim", width=12)
    basic_commands_table.add_column("Description")
    basic_commands_table.add_row("help", "Show this menu")
    basic_commands_table.add_row("exit", "Exit to C2 server prompt (Shell works in background)")
    basic_commands_table.add_row("clear", "Clear the previous outputs")
    basic_commands_table.add_row("terminate", "Exit the shell completely")

    system_commands_table = Table(show_header=True, header_style="bold white")
    system_commands_table.add_column("Command", style="dim", width=12)
    system_commands_table.add_column("Description")
    system_commands_table.add_row("cd", "Change directory")
    system_commands_table.add_row("pwd", "Print current working directory")
    system_commands_table.add_row("mkdir *dir_name*", "Create a specified directory")
    system_commands_table.add_row("rm *dir_name*", "Delete a specified directory")
    system_commands_table.add_row("powershell <command>", "Run powershell command")
    system_commands_table.add_row("start *exe_name*", "Start a specified executable")

    information_gathering_commands_table = Table(show_header=True, header_style="bold white")
    information_gathering_commands_table.add_column("Command", style="dim", width=12)
    information_gathering_commands_table.add_column("Description")
    information_gathering_commands_table.add_row("env", "Check environment variables")
    information_gathering_commands_table.add_row("sc", "List all running services")
    information_gathering_commands_table.add_row("user", "Current user")
    information_gathering_commands_table.add_row("info", "Get all information about compromised system")
    information_gathering_commands_table.add_row("av", "List all antivirus(es) in compromised system")

    data_exfiltration_commands_table = Table(show_header=True, header_style="bold white")
    data_exfiltration_commands_table.add_column("Command", style="dim", width=12)
    data_exfiltration_commands_table.add_column("Description")
    data_exfiltration_commands_table.add_row("download *file_name*", "Download files from compromised system")
    data_exfiltration_commands_table.add_row("upload *file_name*", "Upload files to compromised system")

    exploitation_commands_table = Table(show_header=True, header_style="bold white")
    exploitation_commands_table.add_column("Command", style="dim", width=12)
    exploitation_commands_table.add_column("Description")
    exploitation_commands_table.add_row("persistence1", "Persistence via Method 1")
    exploitation_commands_table.add_row("persistence2", "Persistence via Method 2")
    exploitation_commands_table.add_row("get", "Dump all stored passwords from Chrome browser")
    exploitation_commands_table.add_row("chrome_pass_dump", "Delete a specified directory")
    exploitation_commands_table.add_row("wifi_password", "Dump passwords of all saved Wifi networks")
    exploitation_commands_table.add_row("keylogger", "Start keylogger")
    exploitation_commands_table.add_row("dump_keylogger", "Dump all logs done by keylogger")
    exploitation_commands_table.add_row("python_install", "Install Python on compromised pc without UI")

    print("\nBASIC COMMANDS")
    xprint(basic_commands_table)
    print("\nSYSTEM COMMANDS")
    xprint(system_commands_table)
    print("\nINFORMATION GATHERING COMMANDS")
    xprint(information_gathering_commands_table)
    print("\nDATA EXFILTRATION COMMANDS")
    xprint(data_exfiltration_commands_table)
    print("\nEXPLOITATION COMMANDS")
    xprint(exploitation_commands_table)


def session_help():
    session_help_commands_table = Table(show_header=True, header_style="bold white")
    session_help_commands_table.add_column("Command", style="dim", width=12)
    session_help_commands_table.add_column("Description")
    session_help_commands_table.add_row("sessions -l", "List all victims connected to C2 server")
    session_help_commands_table.add_row("sessions -i <session number>", "Interact with a session individually")
    session_help_commands_table.add_row("sendall", "Send the same command to all victims")
    session_help_commands_table.add_row("shell_help", "All commands before/after getting shell")

    xprint(session_help_commands_table)


def shell_help():
    main_help()
    session_help()
