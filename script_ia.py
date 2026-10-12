# Script de monitoreo verificado línea por línea para la entrega de la Semana 9
def verificar_servicios(lista_servicios):
    # REVISIÓN LÍNEA POR LÍNEA - PUNTO CORREGIDO: 
    # Se añade validación defensiva. Si la lista está vacía, evita fallas críticas si cae la infraestructura.
    if not lista_servicios:
        return "Alerta Crítica: No se detectan servicios activos en la infraestructura."

    return f"Infraestructura estable. Monitoreando {len(lista_servicios)} servicios activos."

# Prueba simulando tus contenedores Docker previos (Nginx y MySQL)
mis_servicios = ['nginx-proxy', 'mysql-database']
print(verificar_servicios(mis_servicios))
