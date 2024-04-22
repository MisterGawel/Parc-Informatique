######################################################
# Ce script va permettre de récolter les données sur #
# - l'utilisation du CPU (python)                    #
# - l'utilisation de la mémoire (python)             #
# - l'utilisation du disque (python)                 #
# - le nombre de processus en cours (bash)           #
# - le nombre d'utilisateurs connectés (bash)        #
######################################################


#!/bin/bash

# Fonction pour afficher les informations collectées
print_info() {
    echo "CPU Usage: $1 %"
    echo "Total memory: $2 bytes"
    echo "Used memory: $3 bytes"
    echo "Memory Usage: $4 %"
    echo "Total disk space: $5 bytes"
    echo "Used disk space: $6 bytes"
    echo "Disk usage: $7 %"
    echo "Number of processes: $8"
    echo "Number of Users: $9"
}

# Collecte des informations CPU, mémoire et disque (python)
info=$(python3 << END
import psutil
import os

cpu_percent = psutil.cpu_percent(interval=1)

mem = psutil.virtual_memory()
mem_total = mem.total
mem_used = mem.used
mem_percent = mem.percent

disk = psutil.disk_usage('/')
disk_total = disk.total
disk_used = disk.used
disk_percent = disk.percent

print(cpu_percent, mem_total, mem_used, mem_percent, disk_total, disk_used, disk_percent)
END
)

# Collecte des informations sur le nombre de processus en cours (bash)
num_processes=$(ps -A --no-headers | wc -l)

# Collecte des informations sur le nombre d'utilisateurs connectés (bash)
num_users=$(who | wc -l)

# Extraire les valeurs de $info
cpu_percent=$(echo "$info" | awk '{print $1}')
mem_total=$(echo "$info" | awk '{print $2}')
mem_used=$(echo "$info" | awk '{print $3}')
mem_percent=$(echo "$info" | awk '{print $4}')
disk_total=$(echo "$info" | awk '{print $5}')
disk_used=$(echo "$info" | awk '{print $6}')
disk_percent=$(echo "$info" | awk '{print $7}')

# Appel de la fonction pour afficher les informations collectées
print_info $cpu_percent $mem_total $mem_used $mem_percent $disk_total $disk_used $disk_percent $num_processes $num_users

# Appel du script stockage.py pour stocker les informations collectées
python3 /home/gawel/MiniProjet/scripts/stockage.py "$cpu_percent" "$mem_total" "$mem_used" "$mem_percent" "$disk_total" "$disk_used" "$disk_percent" "$num_processes" "$num_users"

# Appel du script detection.py pour détecter les anomalies
python3 /home/gawel/MiniProjet/scripts/detection.py "$cpu_percent" "$mem_percent" "$disk_percent" "$num_processes" "$num_users"

# Appel du script graphiques.py pour afficher les graphiques
python3 /home/gawel/MiniProjet/scripts/graphiques.py