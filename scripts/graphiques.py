######################################################
# Ce script permet de créer des graphiques à partir  #
# des données stockées dans les fichiers .json       #
######################################################


import pygal
import json
import os
from datetime import datetime
from pygal.style import Style


dossier_backup = '/home/gawel/MiniProjet/backup/'
chemins_tries = []

dates_tab = []
cpu_usage_values = []
memory_usage_values = []
disk_usage_values = []
processes_values = []
users_values = []


if not os.path.exists('/home/gawel/MiniProjet/charts'):
    os.makedirs('/home/gawel/MiniProjet/charts')


for filename in os.listdir(dossier_backup):
    if filename.endswith('.json'):
        chemin_fichier = os.path.join(dossier_backup, filename)
        parts = filename.split('_')
        date_str, heure_str = parts[1], parts[2].split('.')[0]
        date_obj = datetime.strptime(date_str + '_' + heure_str, '%d-%m-%Y_%H-%M-%S')
        chemins_tries.append((date_obj, chemin_fichier))

chemins_tries.sort()


for date_creation, chemin_fichier in chemins_tries:
    with open(chemin_fichier, 'r') as file:
        data = json.load(file)

        cpu_usage = data.get('CPU Usage')
        cpu_usage_values.append(cpu_usage)
        cpu_high = max(cpu_usage_values)
        cpu_low = round(min(cpu_usage_values),1)
        cpu_average = sum(cpu_usage_values) / len(cpu_usage_values)

        memory_usage = data.get('Memory Usage')
        memory_usage_values.append(memory_usage)
        memory_high = max(memory_usage_values)
        memory_low = min(memory_usage_values)
        memory_average = round(sum(memory_usage_values) / len(memory_usage_values),1)
        memory_total = data.get('Total Memory') 
        if memory_total is not None:
            memory_total = round((memory_total / 1073741824) ,1)
        memory_used = data.get('Used Memory')
        if memory_used is not None:
            memory_used = round((memory_used / 1073741824) ,1)

        disk_usage = data.get('Disk Usage')
        disk_usage_values.append(disk_usage)
        disk_high = max(disk_usage_values)
        disk_low = min(disk_usage_values)
        disk_average = sum(disk_usage_values) / len(disk_usage_values)
        disk_total = data.get('Total Disk')
        if disk_total is not None:
            disk_total = round((disk_total / 1073741824) ,1)
        disk_used = data.get('Used Disk')
        if disk_used is not None:
            disk_used = round((disk_used / 1073741824) ,1)

        processes = data.get('Number of Processes')
        processes_values.append(processes)
        processes_high = max(processes_values)
        processes_low = min(processes_values)
        processes_average = sum(processes_values) / len(processes_values)

        users = data.get('Number of Users')
        users_values.append(users)
        users_high = max(users_values)
        users_low = min(users_values)
        users_average = sum(users_values) / len(users_values)

        formatted_date = date_creation.strftime('%H:%M:%S')
        dates_tab.append(formatted_date)


with open('/home/gawel/MiniProjet/public_html/stats.txt', 'w') as f:
    f.write(f"cpu_average {cpu_average}\n")
    f.write(f"cpu_high {cpu_high}\n")
    f.write(f"cpu_low {cpu_low}\n")

    f.write(f"memory_average {memory_average}\n")
    f.write(f"memory_high {memory_high}\n")
    f.write(f"memory_low {memory_low}\n")
    f.write(f"memory_total {memory_total}\n")
    f.write(f"memory_used {memory_used}\n")

    f.write(f"disk_average {disk_average}\n")
    f.write(f"disk_high {disk_high}\n")
    f.write(f"disk_low {disk_low}\n")
    f.write(f"disk_total {disk_total}\n")
    f.write(f"disk_used {disk_used}\n")

    f.write(f"processes_average {processes_average}\n")
    f.write(f"processes_high {processes_high}\n")
    f.write(f"processes_low {processes_low}\n")

    f.write(f"users_average {users_average}\n")
    f.write(f"users_high {users_high}\n")
    f.write(f"users_low {users_low}\n")

custom_style = Style(
  background='transparent',
  plot_background='transparent',
  foreground='#fefdf9',
  foreground_strong='#fefdf9',
  foreground_subtle='#fefdf9',
  opacity='0.7',
  font_family='Indivisible',
  title_font_size=20,
  opacity_hover='.9',
  transition='400ms ease-in',
  colors=('#E853A0', '#E8537A', '#E95355', '#E87653', '#E89B53'))


def generate_chart(title, x_labels, data_values, filename):
    chart = pygal.StackedLine(fill=True, style=custom_style)
    chart.title = title
    chart.x_labels = x_labels
    chart.add(None, data_values, dots_size=4)
    chart.render_to_file(filename)

charts_data = [
    ('cpu_chart', 'Utilisation du CPU (en %) en fonction du temps', cpu_usage_values),
    ('memory_chart', 'Utilisation de la mémoire (en %) en fonction du temps', memory_usage_values),
    ('disk_chart', 'Utilisation du disque (en %) en fonction du temps', disk_usage_values),
    ('processes_chart', 'Nombre de processus en fonction du temps', processes_values),
    ('users_chart', 'Nombre d\'utilisateurs connectés en fonction du temps', users_values)
]

for chart_name, title, data_values in charts_data:
    generate_chart(title, dates_tab, data_values, f'/home/gawel/MiniProjet/charts/{chart_name}_from_json.svg')
