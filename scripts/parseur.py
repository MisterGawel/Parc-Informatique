######################################################
# Ce script permet de récupérer la dernière alerte   #
# CERT et de l'afficher.                             #
######################################################

import requests
import xml.etree.ElementTree as ET
import datetime

# Fonction pour récupérer la dernière alerte CERT
def get_latest_cert_alert():
    url = 'https://www.cert.ssi.gouv.fr/alerte/feed/'
    response = requests.get(url)
    root = ET.fromstring(response.content)
    
    latest_alert_title = None
    latest_alert_date = None
    
    for item in root.findall('./channel/item'):
        title = item.find('title').text
        date = datetime.datetime.strptime(item.find('pubDate').text, '%a, %d %b %Y %H:%M:%S %z')
        
        if latest_alert_date is None or date > latest_alert_date:
            latest_alert_title = title
            latest_alert_date = date
    
    return latest_alert_title, latest_alert_date

# Appel de la fonction pour récupérer la dernière alerte CERT
latest_alert_title, latest_alert_date = get_latest_cert_alert()

# Affichage de la dernière alerte
if latest_alert_title and latest_alert_date:
    print("Dernière alerte CERT:")
    print("Titre:", latest_alert_title)
    print("Date de publication:", latest_alert_date)
else:
    print("Aucune alerte trouvée.")
