<?php

$file_path = 'stats.txt';
$file_content = file_get_contents($file_path);
$lines = explode("\n", $file_content);
$cpu_average = null;
$cpu_high = null;
$cpu_low = null;

foreach ($lines as $line) {
    $parts = explode(' ', $line);
    if ($parts[0] === 'cpu_average') {
        $cpu_average = floatval($parts[1]); 
    }
    if ($parts[0] === 'cpu_high') {
        $cpu_high = floatval($parts[1]); 
    }
    if ($parts[0] === 'cpu_low') {
        $cpu_low = floatval($parts[1]); 
    }
}

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
                <span id="titre">Sonde : CPU</span>
            </div>
        </div>
        <div id="text_cpu">

            <div style="display: inline-flex;">
                <div class="div_text">
                    <span class="text">Moyenne :</span>
                </div>
                <div class="div_text2">
                    <div class="container">
                        <div class="content">
                            <span class="stats"><?php echo $cpu_average ?><strong> %</strong></span>
                        </div>
                    </div>
                </div>
            </div>

            <div style="display: inline-flex;">
                <div class="div_text">
                    <span class="text">Pic le plus haut :</span>
                </div>
                <div class="div_text2">
                    <div class="container">
                        <div class="content">
                            <span class="stats"><?php echo $cpu_high ?><strong> %</strong></span>
                        </div>
                    </div>
                </div>
            </div>

            <div style="display: inline-flex;">
                <div class="div_text">
                    <span class="text">Pic le plus faible :</span>
                </div>
                <div class="div_text2">
                    <div class="container">
                        <div class="content">
                            <span class="stats"><?php echo $cpu_low ?><strong> %</strong></span>
                        </div>
                    </div>
                </div>
            </div>

        </div>
    </div>
    <div class="div_graphiques">
        <div class="graphiques">
            <?php 
                include('../charts/cpu_chart_from_json.svg');
            ?>
        </div>
    </div>
</body>
</html>