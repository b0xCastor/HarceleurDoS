import os
import base64
import socket
import time

try:
    from colorama import Fore, init
except:
    os.system("py -m pip install colorama")
    from colorama import Fore, init
init()

banner = (Fore.BLUE + """
___________________________          

╦ ╦┌─┐┬─┐┌─┐┌─┐┬  ┌─┐┬ ┬┬─┐
╠═╣├─┤├┬┘│  ├┤ │  ├┤ │ │├┬┘ DoS
╩ ╩┴ ┴┴└─└─┘└─┘┴─┘└─┘└─┘┴└─
___________________________
                                                                                       
          """ + Fore.LIGHTBLUE_EX)
print(banner)

def ping(host, count):
    try:
        ip = socket.gethostbyname(host)
    except socket.gaierror:
        print("Impossible de résoudre l'adresse IP de l'hôte.")
        return

    print(f"Ping vers {host} [{ip}]")

    for i in range(count):
        start_time = time.time()
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP) as s:
                s.connect((ip, 0))
                s.sendall(b'\x08\x00\x7d\x4b\x00\x00\x00\x00Ping')
                s.recvfrom(1024)
            end_time = time.time()
            elapsed_time_ms = (end_time - start_time) * 1000
            print(f"Réponse de {host}: temps={elapsed_time_ms:.2f} ms")
        except OSError:
            print("Échec de la requête.")

if __name__ == "__main__":
    host = input("Entrez l'adresse IP ou le nom d'hôte à pinger : ")
    count = int(input("Nombre de requêtes à envoyer : "))
    ping(host, count)
