 ################################ Fichier de configuration SSH (/etc/ssh/sshd_config) ####################################

# Port SSH personnalisé
Port 2222

# Désactivation de l'authentification par mot de passe
PasswordAuthentication no

# Activation de l'authentification par clé publique
PubkeyAuthentication yes

# Autoriser uniquement certains utilisateurs
AllowUsers user1 user2

# Désactivation de l'accès root
PermitRootLogin no

# Limiter les ciphers et les MAC autorisés
Ciphers aes256-ctr
MACs hmac-sha2-512

# Limiter les versions de protocole SSH
Protocol 2

 ################################  Fichier de configuration SSH client (/etc/ssh/ssh_config)  ################################ 
# Désactivation de l'utilisation de l'agent SSH
ForwardAgent no

# Utilisation d'une clé spécifique pour une connexion
IdentityFile ~/.ssh/id_rsa_example

# Limiter les ciphers et les MAC autorisés pour les connexions sortantes
Ciphers aes256-ctr
MACs hmac-sha2-512