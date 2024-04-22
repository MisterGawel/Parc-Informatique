<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <div id="main_nav">
        <div id="div1_nav">
            <div>
                <span id="titre">Menu</span>
            </div>
        </div>
        <div id="div2_nav">
            <?php foreach ($TABPAGES as $nom_page => $url_page): ?>
                <div class="div_liens">
                    <a class="liens" href="index.php?page=<?php echo $url_page; ?>"><?php echo $nom_page; ?></a>
                </div>
            <?php endforeach; ?>
        </div>
    </div>
</body>
</html>