<?php

$file_path = 'stats.txt';
$file_content = file_get_contents($file_path);
$lines = explode("\n", $file_content);
$disk_average = null;
$disk_high = null;
$disk_low = null;
$disk_total = null;	
$disk_used = null;

foreach ($lines as $line) {
    $parts = explode(' ', $line);
    if ($parts[0] === 'disk_average') {
        $disk_average = floatval($parts[1]); 
    }
    if ($parts[0] === 'disk_high') {
        $disk_high = floatval($parts[1]); 
    }
    if ($parts[0] === 'disk_low') {
        $disk_low = floatval($parts[1]); 
    }
    if ($parts[0] === 'disk_total') {
        $disk_total = floatval($parts[1]); 
    }
    if ($parts[0] === 'disk_used') {
        $disk_used = floatval($parts[1]); 
    }
}
$disk_nused = $disk_total - $disk_used;

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <div class="div_capteurs">
        <div id="div_cpu">
            <div>
                <span id="titre">Sonde : Disque</span>
            </div>
        </div>
        <div id="text_cpu" style="display:flex;">
            <div style="width:50%; height:80%; display: grid; margin:10% 0 10% 0;">
                <div style="display: inline-flex; width: 100%; align-items:center">
                    <div class="div_text">
                        <span class="text">Moyenne</span>
                    </div>
                    <div class="div_text2">
                        <div class="container">
                            <div class="content">
                                <span><?php echo $disk_average ?><strong> %</strong></span>
                            </div>
                        </div>
                    </div>
                </div>

                <div style="display: inline-flex; width: 100%; align-items:center ">
                    <div class="div_text">
                        <span class="text">Pic haut</span>
                    </div>
                    <div class="div_text2">
                        <div class="container">
                            <div class="content">
                                <span class="stats"><?php echo $disk_high ?><strong> %</strong></span>
                            </div>
                        </div>
                    </div>
                </div>

                <div style="display: inline-flex; width: 100%; align-items:center">
                    <div class="div_text">
                        <span class="text">Pic faible</span>
                    </div>
                    <div class="div_text2">
                        <div class="container">
                            <div class="content">
                                <span class="stats"><?php echo $disk_low ?><strong> %</strong></span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div style="width:50%; height:80%; display: grid; margin:10% 0 10% 0;">
                <div style="display: inline-flex; width: 100%; align-items:center">
                    <div class="div_text">
                        <span class="text">Mémoire totale</span>
                    </div>
                    <div class="div_text2">
                        <div class="container">
                            <div class="content">
                                <span><?php echo $disk_total ?><strong> Go</strong></span>
                            </div>
                        </div>
                    </div>
                </div>

                <div style="display: inline-flex; width: 100%; align-items:center">
                    <div class="div_text">
                        <span class="text">Mémoire utilisé</span>
                    </div>
                    <div class="div_text2">
                        <div class="container">
                            <div class="content">
                                <span class="stats"><?php echo $disk_used ?><strong> Go</strong></span>
                            </div>
                        </div>
                    </div>
                </div>

                <div style="display: inline-flex; width: 100%; align-items:center">
                    <div class="div_text">
                        <span class="text">Mémoire non-utilisé</span>
                    </div>
                    <div class="div_text2">
                        <div class="container">
                            <div class="content">
                                <span class="stats"><?php echo $disk_nused ?><strong> Go</strong></span>
                            </div>
                        </div>
                    </div>
                </div>

                </div>
            </div>
        </div>


    <div class="div_graphiques">
        <div class="graphiques">
            <?php 
                include('../charts/disk_chart_from_json.svg');
            ?>
        </div>
    </div>
</body>
</html>