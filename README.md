# Infraestructura Local - APTI LAB

## Descripción
Este repositorio contiene el despliegue del servidor proxy Nginx y la base de datos MySQL mediante contenedores Docker.

## Requisitos
- Ubuntu Server 22.04 LTS
- Docker Core
- Docker Compose

## Entrega de Laboratorio - Automatizaciones Semana 9

* **Script en Bash (`respaldo.sh`):** Desarrollado para la ejecución automatizada de copias de seguridad compactadas y estructuradas en el demonio del sistema `cron`.
* **Reportes de Diagnóstico (`.csv`):** Extracción nativa mediante comandos de Windows PowerShell de los procesos activos y el estado de los servicios del sistema.
* **Script en Python (`script_ia.py`):** Código enfocado en la auditoría preventiva e integridad en caliente de la conectividad de los servicios del entorno.

### 🤖 Bitácora de Verificación de Código Asistido por IA
* **Script Analizado:** `script_ia.py`
* **Análisis Línea por Línea:** Se auditó la función lógica dedicada a comprobar y listar los servicios del ecosistema local de red.
* **Punto Técnico Corregido:** El bloque provisto originalmente por la IA carecía de validación defensiva ante listas vacías. Se implementó un control condicional (`if not lista_servicios:`) para interceptar fallos críticos de ejecución si los contenedores Nginx o MySQL se encuentran caídos, garantizando la resiliencia integral del script.
