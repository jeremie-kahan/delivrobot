# Projet Prototype_ groupe 6

*Nom:* Deliv'Robot

*Auteurs:* BRIAND Estelle _ DUPUIS Florian _ KAHAN Jérémie _ MATHOU Cédric

*Ecole:* CPE Lyon

## But du projet:
Projet de prototypage libre sur 20h

Problématique:

Solution: un robot téléguidable qui ouvre la boite que s'il détécte la présence d'une personne

## Description git

        /app =  contient tout les fichiers pour l'application android

        /doc = document tel que le fichier .stl

        /[PC]_deliv_robot_ws => worspace ROS executable sur PC linux

        /[raspberry]_deliv_robot_ws => worspace ROS executable sur la raspberry


### Moteur dynamixel
-	Telecharger le git : https://github.com/arebgun/dynamixel_motor.git
-	Sur la VM autoriser l’USB Xevelabs
-	Sur un teminal, pour savoir quel port correspond au moteur : ```$ls /dev/```

On verra un ttyAMC0 ```$sudo chmod 666 /dev/ttyAMC0```

Ensuite ```$rosrun dynamixel_driver info_dump.py -p /dev/ttyAMC0 1```

Pour faire tourner le motor pas en continue :  

trouver où se trouve le set_servo_config.py (logiquement dans dynamixel_driver)
```$./set_servo_config.py –port=/dev/ttyAMC0 –baud=1000000 –ccw-angle=1023 –cw-angle-limit=0 1```

### ROSSERIAL
installer ROSSERIAL sur PC
installer la librairie Arduino IDE rosserial

