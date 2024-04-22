######################################################
# Ce script permet d'envoyer un e-mail à l'adresse   #
# spécifiée.                                         #
######################################################


import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def envoyer_email(destinataire, sujet, contenu):
    smtp_server = 'partage.univ-avignon.fr'
    smtp_port = 465
    email_address = 'gael.amoros@alumni.univ-avignon.fr'
    email_password = "Ga374803ga!!"

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
        try:
            # Connexion au compte
            server.login(email_address, email_password)
            # Création du message
            message = MIMEMultipart("alternative")
            message["Subject"] = sujet
            message["From"] = email_address
            message["To"] = destinataire

            # Création des parties du message
            text_part = MIMEText(contenu, "plain")
            html_part = MIMEText(contenu, "html")

            # Ajout des parties au message
            message.attach(text_part)
            message.attach(html_part)

            # Envoi du message
            server.sendmail(email_address, destinataire, message.as_string())
            print("L'email a été envoyé avec succès à", destinataire)
        except Exception as e:
            print(f"Erreur lors de l'envoi de l'email à {destinataire} : {e}")

