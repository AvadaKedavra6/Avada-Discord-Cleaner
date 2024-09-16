#                   Made by Avada
#                   Discord Cleaner

# Imports
import os
import glob
import subprocess
import time
import json
import colorama
from pystyle import Colorate, Colors
from datetime import datetime

# Display menu
def display_ascii_art():
    ascii_art = r"""                              ___               __    _________               __   
                            .'   `.            [  |  |  _   _  |             [  |  
                           /  .-.  \ _   _   __ | |  |_/ | | \_|.--.    .--.  | |  
                           | |   | |[ \ [ \ [  ]| |      | |  / .'`\ \/ .'`\ \| |  
                           \  `-'  / \ \/\ \/ / | |     _| |_ | \__. || \__. || |  
                            `.___.'   \__/\__/ [___]   |_____| '.__.'  '.__.'[___] 

                                        Created by Avada Kedavra                                                                                     
                                                                                                                                      
       ╔═════════════════════════════════════════════════════════════════════════════════════════╗   
       ║                                  [+] 1. Verify files [+]                                ║
       ╚═════════════════════════════════════════════════════════════════════════════════════════╝


       ┌──(avadakedavra@user)-[~/Home]
       │                      
       └─$>
    """
    colored_ascii_art = Colorate.Horizontal(Colors.purple_to_blue, ascii_art)
    print(colored_ascii_art)

# Get path to local
appdata = os.getenv('LOCALAPPDATA') if os.getenv('LOCALAPPDATA') else f'{os.path.splitdrive(__file__)[0]}:/Users/{os.getlogin()}/AppData/Local'

# Function for logs file + generate
def generate_log_file_path():
    timestamp = datetime.now().strftime('adc_%Y%m%d')
    return os.path.join(os.path.dirname(__file__), f'log_{timestamp}.txt')

def log_message(message, log_file_path):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(log_file_path, 'a', encoding='utf-8') as log_file:
        log_file.write(f'[{timestamp}] {message}\n')

# Get discord folders
def list_discord_folders():
    folders = [d for d in os.listdir(appdata) if os.path.isdir(os.path.join(appdata, d)) and 'cord' in d]
    return folders

# Main code
def check_token_grabber():
    log_file_path = generate_log_file_path()
    log_message("Launch of adc...", log_file_path)
    
    discord_folders = list_discord_folders()
    log_message(f"Directories found : {discord_folders}", log_file_path)

    if not discord_folders:
        log_message("No Discord folders found.", log_file_path)
        return

    for folder in discord_folders:
        for path in glob.glob(os.path.join(appdata, folder, 'app-*', 'modules', 'discord_desktop_core-*', 'discord_desktop_core')):
            log_message(f"Checking the path : {path}", log_file_path)
            if 'index.js' not in os.listdir(path):
                log_message(f"index.js file not found in {path}", log_file_path)
                continue

            filename = os.path.join(path, 'index.js')

            try:
                # Verify if discord are ON
                tasklist = subprocess.check_output('tasklist', shell=True, encoding='cp850')
            except subprocess.CalledProcessError as e:
                log_message(f"Error executing tasklist : {e}", log_file_path)
                continue

            if f'{folder}.exe' in tasklist:
                log_message(f"{folder}.exe running, closing the process.", log_file_path)
                subprocess.run(f'taskkill /IM {folder}.exe /F', shell=True)
                time.sleep(2)
                update_exe = os.path.join(appdata, folder, 'Update.exe')
                if os.path.exists(update_exe):
                    log_message(f"Restarting {folder}.exe via {update_exe}", log_file_path)
                    subprocess.run(f'{update_exe} --processStart {folder}.exe', shell=True)

            try:
                with open(filename, 'r', encoding='utf-8') as f:
                    content = f.read()
            except IOError as e:
                log_message(f"Error reading index.js file : {e}", log_file_path)
                continue

            if content != "module.exports = require('./core.asar');":
                log_message(f'ALERT : You have been token grabbed in {folder} !', log_file_path)
                try:
                    with open(filename, 'w', encoding='utf-8') as f:
                        f.write("module.exports = require('./core.asar');")
                    log_message('Token grabber successfully removed ! Please change your password.', log_file_path)
                except IOError as e:
                    log_message(f"Error writing to index.js : {e}", log_file_path)
            else:
                log_message(f"The index.js of {folder} is already clean.", log_file_path)

            package_json_path = os.path.join(path, 'package.json')
            if os.path.exists(package_json_path):
                try:
                    with open(package_json_path, 'r', encoding='utf-8') as f:
                        package_json = json.load(f)
                except (IOError, json.JSONDecodeError) as e:
                    log_message(f"Error reading package.json file : {e}", log_file_path)
                    continue

                if 'main' in package_json and package_json['main'] != 'index.js':
                    log_message(f'ALERT : You have been token grabbed in {package_json["main"]} !', log_file_path)
                    package_json['main'] = 'index.js'

                    try:
                        with open(package_json_path, 'w', encoding='utf-8') as f:
                            json.dump(package_json, f, indent=4)
                        log_message('Package.json file successfully fixed.', log_file_path)
                    except IOError as e:
                        log_message(f"Error writing to package.json : {e}", log_file_path)
                else:
                    log_message(f"The instance {folder} is clean (main = index.js).", log_file_path)
            else:
                log_message(f"package.json file not found for instance {folder}.", log_file_path)

    log_message("Cleaning completed, the log file has been created.", log_file_path)
    time.sleep(5)
                


# Function Menu
def main_menu():
    display_ascii_art()
    choice = input("\nChoose an option : ")

    if choice == "1":
        check_token_grabber()
        print(Colorate.Horizontal(Colors.purple_to_blue, "Clean finish , log files with all actions was created in the folder of this program !"))
    else:
        print(Colorate.Horizontal(Colors.purple_to_blue, "Option invalid.."))

if __name__ == "__main__":
    main_menu()