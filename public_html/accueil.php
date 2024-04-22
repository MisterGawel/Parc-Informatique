<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <div id="div_accueil">
        <div id="div_cpu">
            <div>
                <span id="titre">Introduction au projet </span>
            </div>
        </div>
        <div id="text_cpu">

                <div style="width:100%; margin-top:15px; height:55px; display:flex; justify-content: center; align-items: center;">
                    <span class="text" style="font-size:1.4em;padding-left:0px;text-align: center;width: 70%;">Ce projet a pour but de mettre en place un système de surveillance de l'état d'un parc informatique. 
                        Il est composé de plusieurs capteurs (CPU, mémoire, disque, processus, utilisateurs).
                    </span>
                </div>

                <div style="display:flex; height:250px ">
                    <div style="width:50%; display:flex; justify-content: center; align-items: center;">
                        <span class="text" style="line-height:28px; font-size:1.2em;padding-left:0px">Coté Web : 6 pages.<br><br>
                            <li>Accueil : Page d'accueil du projet</li>
                            <li>CPU : Page de surveillance de l'état du CPU</li>
                            <li>Mémoire : Page de surveillance de l'état de la mémoire</li>
                            <li>Disque : Page de surveillance de l'état du disque</li>
                            <li>Processus : Page de surveillance des processus</li>
                            <li>Utilisateurs : Page de surveillance des utilisateurs</li>
                        </span>
                    </div>
                    <div style="width:50%; display:flex; justify-content: center; align-items: center;">
                        <span class="text" style="line-height:28px; font-size:1.2em;padding-left:0px">
                        Coté Répertoire : 6 scripts<br><br>
                            <li>collecte.sh : Collecte les informations des sondes</li>
                            <li>detection.py : Détecte et envoie des alertes </li>
                            <li>envoi.py : Envoi de mail lors d'une alerte</li>
                            <li>graphiques.py : Créer les graphiques sous format SVG</li>
                            <li>parseur.py : Récupère l'alerte de CERT</li>
                            <li>stockage.py : Gestionnaire de stockages des informations</li>
                        </span>
                    </div>
                </div>

                <div>
                    <div style="width:100%; height:30px; display:flex; justify-content: center; align-items: center;">
                        <span class="text" style="font-size:1em;padding-left:0px;text-align: center;width: 90%;">
                            Un fichier Readme.txt est disponible dans le répertoire du projet, celui-ci vous expliquera l'ensemble du projet.
                        </span>
                    </div>
                </div>


        </div>
    </div>
</body>
</html>