import subprocess
print('''
 ____  _             ____               _
| __ )| |_   _  ___ / ___|_ __ __ _ ___| |__
|  _ \| | | | |/ _ \ |   | '__/ _` / __| '_ \\
| |_) | | |_| |  __/ |___| | | (_| \__ \ | | |
|____/|_|\__,_|\___|\____|_|  \__,_|___/_| |_|
______________________________________________
''')


def run_apt_up():
    try:
        subprocess.run(["sudo", "apt", "install", "bluetooth"], check=True)
        subprocess.run(["sudo", "apt", "install", "bluetoothctl"], check=True)
        subprocess.run(["sudo", "apt", "update"], check=True)
        print("Installed!")
    except subprocess.CalledProcessError:
        print("Error!")

if __name__ == "__main__":
    run_apt_up()
