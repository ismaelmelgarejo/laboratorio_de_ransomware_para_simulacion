# 🛡️ Ransomware Behavior Simulator (Educational Lab)
Este proyecto es un laboratorio educativo diseñado para simular el comportamiento de un ransomware en un entorno completamente controlado y seguro.

El objetivo principal no es desarrollar software malicioso, sino comprender cómo operan este tipo de amenazas desde una perspectiva técnica, permitiendo analizar su flujo de ejecución, impacto en el sistema de archivos y generación de eventos relevantes para su detección.

La simulación se ejecuta exclusivamente dentro de un entorno aislado (sandbox), donde los archivos son procesados de forma segura mediante copias y renombrado, evitando cualquier tipo de daño real al sistema. Además, el proyecto incluye mecanismos de logging que permiten observar el comportamiento del “ataque” y facilitan su análisis posterior.

---
## Arquitectura

```
lab-ransomware/
│
├── simulator/
│   ├── main.py
│   ├── os_detector.py
│   ├── file_scanner.py
│   ├── encryptor_sim.py
│   └── logger.py
│
├── sandbox/
│   ├── documentos/
│   │   ├── archivo1.pdf
│   │   └── archivo2.pdf
│   └── escritorio/
│
├── logs/
│   └── activity.log
│
└── README.md
```

## 🎯 Objetivos del laboratorio

+ Comprender el ciclo de vida básico de un ransomware
+ Simular la manipulación de archivos de forma segura
+ Analizar eventos y generar logs tipo incidente
+ Explorar estrategias de detección y mitigación
+ Aplicar buenas prácticas de aislamiento y ejecución controlada

## ⚙️ Características principales

+ Detección de sistema operativo (Windows, Linux, macOS)
+ Escaneo controlado de archivos (.pdf) en entorno sandbox
+ Simulación de “cifrado” mediante copia y renombrado
+ Generación de logs para análisis de comportamiento
+ Creación de nota educativa de incidente

## 🔒 Consideraciones de seguridad

Este proyecto fue desarrollado con fines estrictamente educativos.
No interactúa con archivos reales del sistema ni intenta evadir mecanismos de seguridad.

Todas las pruebas deben realizarse en entornos controlados como contenedores o máquinas virtuales.

## 🚀 Enfoque profesional
Este laboratorio está orientado a perfiles de:

+ DevOps / SRE
+ Seguridad informática (Blue Team / Red Team)
+ Ingeniería de sistemas

y busca reforzar conocimientos en observabilidad, análisis de comportamiento y simulación de incidentes.

#### 🏁 Para defender sistemas, primero hay que entender cómo funcionan los ataques
---