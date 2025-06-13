  # Proyecto Aplicaciones de IoT



- **Zayda Fernanda Vargas Vargas**  
  📌 *No. Control:* `1223458878`

---

- **Grupo:** `GDS0653`  
- **Materia:** *Aplicaciones de IoT*
 
## 📋 Descripción del proyecto
Este proyecto implementa un sistema automático de monitoreo y control de ambiente utilizando ESP32, sensores de temperatura, humedad, sensor de calidad del aire y sensor de agua.
El sistema monitorea constantemente las condiciones ambientales y controla automáticamente los siguientes dispositivos:
- **Ventilador**: Se activa cuando la temperatura supera el umbral establecido o cuando la calidad del aire es deficiente
- **Humidificador**: Se activa cuando la humedad es baja
- **Sistema de calefacción (Lamparas de calor)**: Se activa cuando la temperatura es baja
- **Sistema de sonido (Buzzer)**: Se activa cuando el nivel de agua es bajo
- **Sistema de Alimentacion (Servomotor)**: Se abre cada cierto tiempo, para la alimentacion de los insectos  


## 💾 Códigos

- 🔌 [ESP32 #1](https://github.com/Pedro-Uriel-Perez/ProyectoUniidad3AIOT/blob/main/DHT22-RELAY1-RELAY2-MQ135.py)
  
- 🔌 [ESP32 #2](https://github.com/Pedro-Uriel-Perez/ProyectoUniidad3AIOT/blob/main/Servo-Buzzer-SensorAgua.py)

- - 🔌 [pantalla](https://github.com/Zayda1995fer/ProyectoIOT/commit/7272b8a11eab76d82cbec21ca45262e0ee61154f)



## 🔧 Componentes

| **Componente**               | **Descripción**                                                                                                                                                               | **Imagen**                                                                                          |
|------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| **2 ESP32**                     | Microcontrolador principal que coordina todo el sistema.                                                                                                                     | <img src="https://github.com/user-attachments/assets/c650635a-9bcd-4f11-838e-982a7d413050" width="150"> |
| **DHT22**                     | Sensor de temperatura y humedad de alta precisión. **Rango de medición:** -40°C a 80°C / 0–100% HR.                                                                          | <img src="https://github.com/user-attachments/assets/14b93496-4a37-4430-bae8-318b63246710" width="150"> |
| **MQ-135**                    | Sensor de calidad del aire. Detecta gases contaminantes como: NH₃, NOₓ, alcohol, benceno, humo, CO₂.                                                                        | <img src="https://github.com/user-attachments/assets/7a0789e5-94bd-4a2c-a86e-67c4970373ba" width="150"> |
| **Módulo de 4 Relevadores**   | Controla dispositivos de alto voltaje. Permite activar/desactivar el ventilador, humidificador y sistema de calefacción.                                                      | <img src="https://github.com/user-attachments/assets/d79e6412-3b3f-487a-9762-34e76300d648" width="150"> |
| **Ventilador**                | Se activa cuando la temperatura supera los **20.0°C**. También se enciende si la calidad del aire es deficiente (**>1200**).                                                  | <img src="https://github.com/user-attachments/assets/4cdddb4a-fddc-4ac8-95db-80cf8e2975cc" width="150"> |
| **Humidificador**             | Se activa cuando la humedad cae por debajo del **50.0%**. Ayuda a mantener niveles óptimos de humedad.                                                                        | <img src="https://github.com/user-attachments/assets/739b651a-f66f-4828-99cb-44cd5da8ad5e" width="150"> |
| **Sistema de Calefacción**    | Se activa cuando la temperatura baja de **40.0°C**. Mantiene la temperatura adecuada para los insectos.                                                                       | <img src="https://github.com/user-attachments/assets/035732d0-7977-4c0e-8496-600e121bd5f4" width="150"> |
| **Sistema de Sonido (Buzzer)**| Emite una alarma sonora cuando el nivel de agua es bajo. Alerta al usuario para rellenar el depósito.                                                                        | <img src="https://github.com/user-attachments/assets/a0d03c3a-7bc0-4b2d-8148-10f955d66a9d" width="150"> |
| **Sistema de Alimentación**   | Se activa automáticamente según una programación establecida. Libera alimento para los insectos en intervalos regulares.                                                      | <img src="https://github.com/user-attachments/assets/14fb29ce-42f9-4ffb-bcae-8b31ba5a93d5" width="150"> |


## 📊 Parámetros
| Parámetro | Valor predeterminado | Descripción |
|-----------|----------------------|-------------|
| TEMP_UMBRAL_ALTO | 20.0°C | Temperatura máxima antes de activar ventilación |
| TEMP_UMBRAL_BAJO | 40.0°C | Temperatura mínima antes de activar calefacción |
| HUM_UMBRAL | 50.0% | Humedad mínima antes de activar humidificador |
| AIR_UMBRAL | 1200 | Umbral de calidad de aire para ventilación |

## Evidencia de funcionamiento
# [Video de Funcionamiento](https://drive.google.com/file/d/1EGO6X0KMH1n4xwFAi2eMJfMdOrtz5Lv_/view?usp=drive_link)

# Imagenes de Evidencia
<img src="https://github.com/user-attachments/assets/435de6a5-ac59-4ff5-bcae-536a2d2264bf" width="300" alt="Imagen1">
<img src="https://github.com/user-attachments/assets/f3acc4ae-f941-4ffe-bffb-8c2f0a156e00" width="300" alt="Imagen2">




---

# Diagramas de componentes  
<img src="https://github.com/user-attachments/assets/60e2088f-d119-4d7a-8a2e-41b153fed68c" width="1000" alt="ESP32">

## [Link de Diagrama](https://app.cirkitdesigner.com/project/f4358489-d239-4308-8797-f59eab44631c)



---


## 🚀 Uso
El sistema inicia automáticamente al conectar el ESP32. La información del sistema se muestra a través del puerto serie:
- Lecturas de temperatura, humedad y calidad del aire
- Estado de los dispositivos controlados

## 🔄 Funcionamiento
El sistema sigue un ciclo simple de operación:
1. Lee los valores de los sensores
2. Compara con los umbrales establecidos
3. Activa/desactiva los dispositivos según sea necesario


---

# ESP32-2432S028 Con LVGL
<img src="https://github.com/user-attachments/assets/ef73f6c0-ce82-4ee4-9682-ee41573a47bd" width="1000" alt="ESP32">

## [Link de Diagrama](https://app.cirkitdesigner.com/project/eaf57e37-b451-443b-987b-f6f723841fcf)
---

## Evidencia de funcionamiento 
<img src="https://github.com/user-attachments/assets/630d154e-5da4-4271-9d7c-189b227808ce" width="200" alt="Imagen1">
<img src="https://github.com/user-attachments/assets/7fbbeecc-17ee-47e7-9923-9f67d928d13c" width="200" alt="Imagen2">
<img src="https://github.com/user-attachments/assets/1b995e7e-c866-4f1c-9679-44b30029b1c0" width="200" alt="Imagen2">




# Evidencias de practicas de clase

# [Videos](https://drive.google.com/drive/folders/1l9y0XJNzt9TzZj0Vxs_8aQH1ene6313q)










