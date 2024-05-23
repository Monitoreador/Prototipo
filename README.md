## Monitoreador sanitario

------------

### Autores 
- Gabriel Gerardo Parra Rosales
- Abril Yaretsi Cuellar Fuentes

------------

### Requerimientos
#### Hardware 
- Esp32
- Sensor Ultrasónico HC-SR04
- Motor A Pasos 28byj-48
- RC522 Módulo RFID

#### Software
- Arduino IDE

##### Bibliotecas Arduino
- WiFi.h: Para manejar la conexión WiFi en el ESP32.
- HTTPClient.h: Para realizar solicitudes HTTP.
- Stepper.h: Para controlar el motor paso a paso.
- SPI.h: Para comunicación SPI.
- MFRC522.h: Para interactuar con el módulo RFID RC522.

------------


### Código 
[Aquí ](https://github.com/Monitoreador/Prototipo/blob/9a9ba01c4b871aef2569257c4c182d00ce757c7d/proyecto_con_web.ino "Aquí ")podrás acceder al enlace del código, el cual está anotado de manera que te permita comprender su estructura y propósito.

------------

###  Datos del código 
- Cambia el valor de ssid por el nombre de la red WiFi a la que quieres conectarte.

- Cambia el valor de password por la contraseña de la red WiFi.

- Cambia el valor de serverName por la URL o IP del servidor y el endpoint donde se enviarán los datos. Asegúrate de que la URL o IP esté correcta y que el endpoint esté configurado para recibir datos.

```c
const char* ssid = "Monitor Sanitario"; // Replace with your WiFi SSID
const char* password = "monitor12345"; // Replace with your WiFi password
const char* serverName = "http://192.168.105.71/save_data.php"; // Replace with your server IP or domain

```

------------

### Prototipo 
Aquí dejaremos algunas imagenes de nuestro prototipo 

------------

[![imagen1.jpg](https://i.postimg.cc/y8HX3n6y/imagen1.jpg)](https://postimg.cc/CzcfWGqR)
[![imagen2.jpg](https://i.postimg.cc/0y0GYmbR/imagen2.jpg)](https://postimg.cc/Yvjmkv6b)
[![imagen3.jpg](https://i.postimg.cc/Gp3Fq2yB/imagen3.jpg)](https://postimg.cc/VJT0Nz41)
[![imagen4.jpg](https://i.postimg.cc/0Ntp3sYV/imagen4.jpg)](https://postimg.cc/DWXJJRYG)
[![imagen5.jpg](https://i.postimg.cc/vBcWwNXb/imagen5.jpg)](https://postimg.cc/zbYLnp9c)

