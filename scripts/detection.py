######################################################
# Ce script permet de paramétrer les alertes en cas  #
# de surcharge CPU, mémoire, disque, processus et    #
# utilisateurs.                                      #
######################################################


import configparser
import envoi
import sys


# Récupérer les arguments de collecte.sh passés au script
cpu_percent = float(sys.argv[1])
mem_percent = float(sys.argv[2])
disk_percent = float(sys.argv[3])
num_processes = int(sys.argv[4])
num_users = int(sys.argv[5])


# Lecture des critères à partir du fichier de configuration criteres.ini
criteres = configparser.ConfigParser()
criteres.read('/home/gawel/MiniProjet/data/criteres.ini')

critere_cpu = int(criteres.get('CRITERES', 'cpu_limit'))
critere_mem = int(criteres.get('CRITERES', 'memory_limit'))
critere_disk = int(criteres.get('CRITERES', 'disk_limit'))
critere_process = int(criteres.get('CRITERES', 'processus_limit'))
critere_users = int(criteres.get('CRITERES', 'users_limit'))


contenu_email = ""

# Vérification de la surcharge CPU
if cpu_percent > critere_cpu:
    contenu_email += f"Alerte : CPU usage est de {cpu_percent}%\n"

# Vérification de la surcharge de mémoire
if mem_percent > critere_mem:
    contenu_email += f"Alerte : Memory usage est de {mem_percent}%\n"

# Vérification de la surcharge du disque
if disk_percent > critere_disk:
    contenu_email += f"Alerte : Disk usage est de {disk_percent}%\n"

# Vérification du nombre de processus
if num_processes > critere_process:
    contenu_email += f"Alerte : Nombre de processus est de {num_processes}\n"

# Vérification du nombre d'utilisateurs
if num_users > critere_users:
    contenu_email += f"Alerte : Nombre d'utilisateurs est de {num_users}\n"


# S'il y a des alertes, envoyer l'e-mail
if contenu_email:
    print(contenu_email)
    envoi.envoyer_email("gael.amoros@alumni.univ-avignon.fr", "Alerte Critique", contenu_email)
