# Projet Prototype_ groupe 6
*Nom:* Deliv'Robot
*Auteurs:* BRIAND Estelle _ DUPUIS Florian _ KAHAN Jérémie _ MATHOU Cédric

Dossier /app =  contient tout les fichiers pour l'application android
        /doc = document tel que le fichier .stl


## Moteur dynamixel
-	Telecharger le git : https://github.com/arebgun/dynamixel_motor.git
-	Sur la VM autoriser l’USB Xevelabs
-	Sur un teminal :
$ls /dev/
On verra un ttyAMC0  $chmod 666 /dev/ttyAMC0
Ensuite $rosrun dynamixel_driver info_dump.py -p /dev/ttyAMC0 1

Pour faire tourner le motor pas en continue :  
trouver où se trouve le set_servo_config.py (logiquement dans dynamixel_driver)
$./set_servo_config.py –port=/dev/ttyAMC0 –baud=1000000 –ccw-angle=1023 –cw-angle-limit=0 1

