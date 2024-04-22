<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <title>Miniprojet</title>
</head>
<body>
    <?php 
        $TABPAGES = array(
            "Accueil"=>"accueil.php", 
            "CPU"=>"cpu.php",
            "Mémoire"=>"memory.php",
            "Disque"=>"disk.php",
            "Processus"=>"process.php",
            "Utilisateurs"=>"users.php",
        );
    ?>
    <header>
        <div id="header1">
            <div id="header2">
                <span id="titre">Gestion du parc informatique</span>
            </div>
        </div>
	</header>
    <div style="width:100%; display:flex; justify-content: center;">
        <div id="main">

            <div id="nav">
                <?php include 'nav.php'; ?>
            </div>

            <div id="contenu">
                <div class="main_content">
                    <?php
                        if (isset($_GET['page'])){
                            include($_GET['page']); 
                        } else {
                            include('home.php');
                        }
                    ?>
                </div>
            </div>

        </div>
    </div>
    
    <footer>
        <div id="footer1">
            <div id="footer2">
                <img src="UAPV_logo.svg" alt="logo" id="logo" style="width:40px">
            </div>
            <div id="footer3">
                <span id="titre_footer">Auteur : Amoros Gaël</span>
            </div>
        </div>
	</footer>
</body>
</html>