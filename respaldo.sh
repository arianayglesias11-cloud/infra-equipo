#!/bin/bash
# Script de respaldo automatizado - Semana 9
ORIGEN="./"  # Respalda el contenido actual del repositorio (docker-compose, indice.html, etc.)
DESTINO="$HOME/backups"
FECHA=$(date +%Y%m%d_%H%M%S)

mkdir -p "$DESTINO"
tar -czf "$DESTINO/respaldo_infra_$FECHA.tar.gz" "$ORIGEN"
echo "Respaldo completado con éxito en: $DESTINO/respaldo_infra_$FECHA.tar.gz"
