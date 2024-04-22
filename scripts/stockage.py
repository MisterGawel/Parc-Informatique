######################################################
# Ce script va permettre de stocker les données des  #
# sondes dans des fichiers .json et .db              #
######################################################


import os
import json
import shutil
import parseur
import sqlite3
from datetime import datetime
import sys


# Récupérer les arguments de collecte.sh passés au script
cpu_percent = float(sys.argv[1])
mem_total = float(sys.argv[2])
mem_used = float(sys.argv[3])
mem_percent = float(sys.argv[4])
disk_total = float(sys.argv[5])
disk_used = float(sys.argv[6])
disk_percent = float(sys.argv[7])
num_processes = int(sys.argv[8])
num_users = int(sys.argv[9])


# save_data_json va permettre de créer des .json avec les données de chaque sonde à l'intérieur
def save_data_json(data):

    # On vérifie si le dossier data existe, sinon on le crée
    if not os.path.exists('/home/gawel/MiniProjet/data'):
        os.makedirs('/home/gawel/MiniProjet/data')

    # On crée un fichier data.json et on y écrit les données
    with open('/home/gawel/MiniProjet/data/data.json', 'w') as file:
        json.dump(data, file, indent=4)

    # On crée un fichier data.json et on y écrit les données
    if not os.path.exists('/home/gawel/MiniProjet/backup'):
        os.makedirs('/home/gawel/MiniProjet/backup')


# backup_data_json va permettre de renommer le .json actuel avec les métadonnées de la date de création
# et de le déplacer dans un dossier backup jusqu'à au maximum 10 fichiers de backup
def backup_data_json():

    # Récupère la date de création du fichier de données
    data_file = '/home/gawel/MiniProjet/data/data.json'
    creation_time = os.path.getctime(data_file)
    creation_date = datetime.utcfromtimestamp(creation_time).strftime('%d-%m-%Y_%H-%M-%S')

    # Renomme le fichier de sauvegarde avec la date de création
    backup_file = f'/home/gawel/MiniProjet/backup/data_{creation_date}.json'
    shutil.copy(data_file, backup_file)

    # On vérifie si le dossier backup contient plus de 10 fichiers
    # Si c'est le cas, on supprime le fichier le plus ancien
    if len(os.listdir('/home/gawel/MiniProjet/backup')) > 10:
        files = os.listdir('/home/gawel/MiniProjet/backup')
        files.sort(key=lambda x: os.path.getctime(f'/home/gawel/MiniProjet/backup/{x}'))
        os.remove(f'/home/gawel/MiniProjet/backup/{files[0]}')


# save_data_db va permettre de créer un fichier data.db avec les données de chaque sonde à l'intérieur ainsi que les alertes
def save_data_db(data):
    
    # On vérifie si le dossier data existe, sinon on le crée
    if not os.path.exists('/home/gawel/MiniProjet/data'):
        os.makedirs('/home/gawel/MiniProjet/data')

    # On crée un fichier data.db et on y écrit les données des sondes et alertes
    with sqlite3.connect('/home/gawel/MiniProjet/data/data.db') as connection:
        cursor = connection.cursor()

        # Je crée une table sondes pour stocker les données des sondes
        cursor.execute('CREATE TABLE IF NOT EXISTS sondes (id INTEGER PRIMARY KEY AUTOINCREMENT, creation_time TEXT, CPU_Usage REAL, Total_Memory INTEGER, Used_Memory INTEGER, Memory_Usage REAL, Total_Disk INTEGER, Used_Disk INTEGER, Disk_Usage REAL, Number_of_Processes INTEGER, Number_of_Users INTEGER)')
        cursor.execute('INSERT INTO sondes (creation_time, CPU_Usage, Total_Memory, Used_Memory, Memory_Usage, Total_Disk, Used_Disk, Disk_Usage, Number_of_Processes, Number_of_Users) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (data['creation_time'], data['CPU Usage'], data['Total Memory'], data['Used Memory'], data['Memory Usage'], data['Total Disk'], data['Used Disk'], data['Disk Usage'], data['Number of Processes'], data['Number of Users']))
        
        # Dans le même fichier data.db, je crée une table alerts pour stocker les données des alertes
        cursor.execute('CREATE TABLE IF NOT EXISTS alerts (id INTEGER PRIMARY KEY AUTOINCREMENT, creation_time TEXT, alert TEXT)')
        cursor.execute('INSERT INTO alerts (creation_time, alert) VALUES (?, ?)', (data['creation_time'], data['Last CERT alert']))
        
        # On transmet les changements
        connection.commit()


# cleanup_db va permettre de nettoyer la base de données en supprimant les données les plus anciennes
def cleanup_db():
    with sqlite3.connect('/home/gawel/MiniProjet/data/data.db') as connection:
        cursor = connection.cursor()

        cursor.execute("SELECT COUNT(*) FROM sondes")

        cpt = cursor.fetchone()[0]
        if cpt > 10:
            cursor.execute("DELETE FROM sondes WHERE id IN (SELECT id FROM sondes ORDER BY id LIMIT :limit)", {'limit': cpt - 10})

        cursor.execute("SELECT COUNT(*) FROM alerts")
        if cpt > 10:
            cursor.execute("DELETE FROM alerts WHERE id IN (SELECT id FROM alerts ORDER BY id LIMIT :limit)", {'limit': cpt - 10})
    connection.commit()

# On stocke les données des sondes récupérées via le script collecte.py
data_sondes = {
    'creation_time': datetime.now().strftime('%d-%m-%Y_%H-%M-%S'),
    'CPU Usage': cpu_percent,
    'Total Memory': mem_total,
    'Used Memory': mem_used,
    'Memory Usage': mem_percent,
    'Total Disk': disk_total,
    'Used Disk': disk_used,
    'Disk Usage': disk_percent,
    'Number of Processes': num_processes,
    'Number of Users': num_users,
    'Last CERT alert': parseur.latest_alert_title
}

save_data_db(data_sondes)
save_data_json(data_sondes)
backup_data_json()
cleanup_db()