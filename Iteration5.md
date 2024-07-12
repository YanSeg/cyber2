# Firewall

### 1.2 iptable basique

liens utiles:
https://www.linuxtricks.fr/wiki/iptables-quelques-trucs-utiles
https://linux.die.net/man/8/iptables


Désactiver tous les accès au port 22 sauf à partir d'une adresse IP donnée:
```
sudo iptables -A INPUT -p tcp --dport 22 ! -s <addresse_ip_allowed> -j DROP
```



Désactiver tous les accès au port 80 à partir d'un système extérieur, mais autoriser à partir de toutes les machines virtuelles et de votre système local:
```
sudo iptables -A INPUT -p tcp --dport 80 ! -s 127.0.0.1 -m iprange ! --src-range <plage_autorisée> -j DROP
```
Ou <plage_autorisée> s'écrit par exemple 192.168.122.0-192.168.122.255



Activer ou Désactiver le ping:
```
sudo iptables -A INPUT -p icmp --icmp-type 8 -j ACCEPT/DROP
sudo iptables -A INPUT -p icmp --icmp-type 0 -j ACCEPT/DROP
```
ACCEPT pour activer DROP pour désactiver

Désactiver l'accès à tout service extérieur au port 80 (http, web non sécurisé), mais
autoriser le port 443 (https, web sécurisé):
```
sudo iptables -A INPUT -p tcp --dport 80 -j DROP
sudo iptables -A INPUT -p tcp --dport 443 -j ACCEPT
```

REJECT/DROP différences:
Reject renvoie un message (par ICMP) alors que Drop ne renvoie rien. Il est préférable d'utiliser Drop de manière générale, Reject sera plus utilisé a des fin de déboggage.

Additionellement vous pouvez : 
- Bloquer tout le trafic entrant non autorisé avec:
```
    sudo iptables -P INPUT DROP
```
- Sauvegarder les règles dans un fichier pour réplication/backup:
```
    sudo iptables-save > /etc/iptables/rules.v4
```

### 1.3 port knocking 
https://www.digitalocean.com/community/tutorials/how-to-configure-port-knocking-using-only-iptables-on-an-ubuntu-vps