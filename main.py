import random
import string
import subprocess
import winreg as reg
import uuid
import os
import sys
import ctypes


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


if not is_admin():
    print(colors.FAIL + "vSpoofer requires administrator privileges. Please run the terminal as administrator.\n" + colors.ENDC)
    exit()


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_random_string(length):
    return "".join(random.choices(string.ascii_uppercase + string.digits, k=length))


def spoof_sys_uuid():
    volumeid_path = "AMIDEWINx64.exe"
    try:
        command = f"{volumeid_path} /SU AUTO"
        subprocess.run(command, shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,)
        return colors.OKGREEN + f"Successfully spoofed system UUID" + colors.ENDC
    except subprocess.CalledProcessError as e:
        return colors.FAIL + f"An error occurred: {e}" + colors.ENDC


def spoof_sys_sn():
    new_serial_number = random.randint(0000000000000000, 9999999999999999)
    volumeid_path = "AMIDEWINx64.exe"
    try:
        command = f"{volumeid_path} /SS {new_serial_number}"
        subprocess.run(command, shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return colors.OKGREEN + f"Successfully spoofed system serial number to {new_serial_number}" + colors.ENDC
    except subprocess.CalledProcessError as e:
        return colors.FAIL + f"An error occurred: {e}" + colors.ENDC


def spoof_baseboard_sn():
    new_serial_number = random.randint(0000000000000000, 9999999999999999)
    volumeid_path = "AMIDEWINx64.exe"
    try:
        command = f"{volumeid_path} /BS {new_serial_number}"
        subprocess.run(command, shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return colors.OKGREEN + f"Successfully spoofed baseboard serial number to {new_serial_number}" + colors.ENDC
    except subprocess.CalledProcessError as e:
        return colors.FAIL + f"An error occurred: {e}" + colors.ENDC


def spoof_cpu_sn():
    new_serial_number = random.randint(0000000000000000, 9999999999999999)
    volumeid_path = "AMIDEWINx64.exe"
    try:
        command = f"{volumeid_path} /PSN {new_serial_number}"
        subprocess.run(command, shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return colors.OKGREEN + f"Successfully spoofed CPU serial number to {new_serial_number}" + colors.ENDC
    except subprocess.CalledProcessError as e:
        return colors.FAIL + f"An error occurred: {e}" + colors.ENDC


def spoof_disk_sn():
        part1 = "".join(random.choices("0123456789ABCDEF", k=4))
        part2 = "".join(random.choices("0123456789ABCDEF", k=4))
        new_serial_number = f"{part1}-{part2}"
        volumeid_path = "Volumeid.exe"
        try:
            command = f"{volumeid_path} -nobanner {os.getenv("SystemDrive")} {new_serial_number}"
            subprocess.run(command, shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            return colors.OKGREEN + f"Successfully spoofed disk serial number to {new_serial_number}" + colors.ENDC
        except subprocess.CalledProcessError as e:
            return colors.FAIL + f"An error occurred: {e}" + colors.ENDC
    

def spoof_pc_name():
    new_name = generate_random_string(8)
    keys = [
        r"SYSTEM\CurrentControlSet\Control\ComputerName\ActiveComputerName",
        r"SYSTEM\CurrentControlSet\Control\ComputerName\ComputerName",
    ]

    for key in keys:
        try:
            reg_key = reg.OpenKey(reg.HKEY_LOCAL_MACHINE, key, 0, reg.KEY_SET_VALUE)
            reg.SetValueEx(reg_key, "ComputerName", 0, reg.REG_SZ, new_name)

            if key == r"SYSTEM\CurrentControlSet\Control\ComputerName\ComputerName":
                reg.SetValueEx(reg_key, "Hostname", 0, reg.REG_SZ, new_name)

            reg.CloseKey(reg_key)
            return colors.OKGREEN + f"Successfully spoofed pc name to {new_name}" + colors.ENDC
        except Exception as e:
            return colors.FAIL + f"An error occured: {e}" + colors.ENDC
        

def spoof_guid():
    new_guid = str(uuid.uuid4())
    keys = [
        r"SYSTEM\CurrentControlSet\Control\IDConfigDB\Hardware Profiles\0001",
        r"SOFTWARE\Microsoft\Cryptography",
    ]
    values = ["HwProfileGuid", "MachineGuid"]

    for key in keys:
        for value in values:
            try:
                reg_key = reg.OpenKey(
                    reg.HKEY_LOCAL_MACHINE, key, 0, reg.KEY_SET_VALUE
                )
                reg.SetValueEx(reg_key, value, 0, reg.REG_SZ, new_guid)
                reg.CloseKey(reg_key)
                return colors.OKGREEN + f"Updated {key}\\{value} with value {new_guid}" + colors.ENDC
            except Exception as e:
                return colors.FAIL + f"Failed to update {key}\\{value}: {e}" + colors.ENDC


def spoof_product_id():
    new_product_id = generate_random_string(20)
    key = r"SOFTWARE\Microsoft\Windows NT\CurrentVersion"
    value = "ProductId"

    try:
        reg_key = reg.OpenKey(reg.HKEY_LOCAL_MACHINE, key, 0, reg.KEY_SET_VALUE)
        reg.SetValueEx(reg_key, value, 0, reg.REG_SZ, new_product_id)
        reg.CloseKey(reg_key)
        return colors.OKGREEN + f"Updated {key}\\{value} with value {new_product_id}" + colors.ENDC
    except Exception as e:
        return colors.FAIL + f"Failed to update {key}\\{value}: {e}" + colors.ENDC
    

def clean_ubisoft_cache():
    cache_path = r"C:\Program Files (x86)\Ubisoft\Ubisoft Game Launcher\cache"
    if os.path.exists(cache_path):
        for root, dirs, files in os.walk(cache_path):
            for file in files:
                os.remove(os.path.join(root, file))
        return colors.OKGREEN + "Ubisoft cache cleaned." + colors.ENDC
    else:
        return colors.FAIL + "Ubisoft cache path not found." + colors.ENDC


def clean_valorant_cache():
    cache_path = r"C:\Riot Games\VALORANT\live\ShooterGame\Content\Paks"
    if os.path.exists(cache_path):
        for root, dirs, files in os.walk(cache_path):
            for file in files:
                os.remove(os.path.join(root, file))
        return colors.OKGREEN + "Valorant cache cleaned." + colors.ENDC
    else:
        return colors.FAIL + "Valorant cache path not found." + colors.ENDC


def clean_battlenet_cache():
    cache_path = r"C:\Users\{user}\AppData\Local\Blizzard Entertainment\Telemetry"
    if os.path.exists(cache_path):
        for root, dirs, files in os.walk(cache_path):
            for file in files:
                os.remove(os.path.join(root, file))
        return colors.OKGREEN + "Battle.net cache cleaned." + colors.ENDC
    else:
        return colors.FAIL + "Battle.net cache path not found." + colors.ENDC
    

def spoof_all():
    print(colors.WARNING + "\nAfter this operation everything will be spoofed.")
    user_input = input("Do you want to continue? [Y/n] " + colors.ENDC + colors.BOLD)
    if user_input.lower() == "y":
        spoof_sys_uuid()
        spoof_sys_sn()
        spoof_baseboard_sn()
        spoof_cpu_sn()
        spoof_disk_sn()
        spoof_pc_name()
        spoof_guid()
        spoof_product_id()
        spoof_mac_address()
        return colors.OKGREEN + "SPOOFED EVERYTHING" + colors.ENDC
    else:
        return colors.FAIL + "Operation cancelled" + colors.ENDC

    
###########################################################################################################################


def spoof_mac_address():
        return "Not yet implemented."


if __name__ == "__main__":
    while True:
        user_input = 0
        status = ""
        clear()
        print(colors.OKCYAN + "vSpoofer\n" + colors.ENDC)
        print("1. Spoofing")
        print("2. Cleaning")
        print(colors.FAIL + "\nX. Exit\n" + colors.ENDC)

        user_input = input(colors.BOLD + "vSpoofer $ ")
        print("")

        if user_input == "1":
            while True:
                clear()
                if status != "" and status.startswith(colors.FAIL):
                    print(f"{status}\n")
                elif status != "" and status.startswith(colors.OKGREEN):
                    print(f"{status} | Restart your computer for the changes to take effect\n")
                else:
                    print(colors.OKCYAN + "vSpoofer\n" + colors.ENDC)
                print("1. Spoof System UUID")
                print("2. Spoof System Serial Number")
                print("3. Spoof Baseboard Serial Number")
                print("4. Spoof CPU Serial Number")
                print("5. Spoof Disk Serial Number")
                print("6. Spoof PC Name")
                print("7. Spoof GUID")
                print("8. Spoof Product ID")
                print(colors.BOLD + "\n9. Spoof All" + colors.ENDC)
                print(colors.FAIL + "\nX. Exit" + colors.ENDC)
                
                user_input = input(colors.BOLD + "\nvSpoofer $ ")

                if user_input == "1":
                    status = spoof_sys_uuid()
                elif user_input == "2":
                    status = spoof_sys_sn()
                elif user_input == "3":
                    status = spoof_baseboard_sn()
                elif user_input == "4":
                    status = spoof_cpu_sn()
                elif user_input == "5":
                    status = spoof_disk_sn()
                elif user_input == "6":
                    status = spoof_pc_name()
                elif user_input == "7":
                    status = spoof_guid()
                elif user_input == "8":
                    status = spoof_product_id()
                elif user_input == "9":
                    status = spoof_all()
                elif user_input.lower() == "x" or user_input.lower() == "exit":
                    break


        elif user_input == "2":
            while True:
                clear()
                if status != "":
                    print(f"{status}\n")
                else:
                    print(colors.OKCYAN + "vSpoofer\n" + colors.ENDC)
                print("1. Clean Ubisoft Cache")
                print("2. Clean Valorant Cache")
                print("3. Clean Battle.net Cache")
                print(colors.FAIL + "\nX. Exit" + colors.ENDC)

                user_input = input(colors.BOLD + "\nvSpoofer $ ")

                if user_input == "1":
                    status = clean_ubisoft_cache()
                elif user_input == "2":
                    status = clean_valorant_cache()
                elif user_input == "3":
                    status = clean_battlenet_cache()
                elif user_input.lower() == "x" or user_input.lower() == "exit":
                    break

        elif user_input.lower() == "x" or user_input.lower() == "exit":
            exit()
