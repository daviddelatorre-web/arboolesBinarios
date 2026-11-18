from arboles import ArbolBinarioBusqueda
from arboles import Incidente
from arboles import Nodo

# Menú de opciones
print("menu de opciones")
print("1-agregar incidente")
print("2-mostrar arbol")
print("3-mostrar inorden")
print("4-mostrar postorden")
print("5-mostrar preorden")
print("6-buscar incidente por ID")
print("7-eliminar incidente por ID")
print("8-obtener menor y mayor incidente")
print("9-contar incidentes registrados")
print("10-buscar por nivel de riesgo")

if __name__ == "__main__":
    arbol = ArbolBinarioBusqueda()
    
    # Datos de prueba iniciales
    incidentes_iniciales = [
        Incidente(150, "192.168.1.25", "Fuerza bruta", "Alto", "En investigacion"),
        Incidente(100, "192.168.1.30", "Malware", "Critico", "En "),
        Incidente(200, "10.0.0.15", "Escaneo de puertos", "Medio", "Resuelto"),
        Incidente(75, "192.168.1.45", "Phishing", "Alto", "Pendiente"),
        Incidente(125, "10.0.0.20", "Acceso no autorizado", "Critico", "En investigacion"),
        Incidente(175, "192.168.1.80", "Ransomware", "Critico", "En investigacion"),
        Incidente(250, "10.0.0.50", "Denegacion de servicio", "Alto", "Pendiente")
    ]
    
    for inc in incidentes_iniciales:
        arbol.insertar(inc)

    while True:
        opcion = input("\nIngrese una opcion o 'salir' para terminar: ")
        
        if opcion == "1":
            id_inc = int(input("Ingrese el ID del incidente: "))
            ip = input("Ingrese la direccion IP: ")
            tipo = input("Ingrese el tipo de ataque: ")
            riesgo = input("Ingrese el nivel de riesgo: ")
            estado = input("Ingrese el estado: ")
            arbol.insertar(Incidente(id_inc, ip, tipo, riesgo, estado))
            
        elif opcion == "2":
            print("Arbol binario de busqueda (IDs):")
            if arbol.is_empty():
                print("El arbol esta vacio")
            else:
                arbol.imprimirArbol()
                
        elif opcion == "3":
            print("Recorrido inorden:")
            if arbol.is_empty():
                print("El arbol esta vacio")
            else:
                arbol.recorridoInorden()
                
        elif opcion == "4":
            print("Recorrido postorden:")
            if arbol.is_empty():
                print("El arbol esta vacio")
            else:
                arbol.recorridoPostorden()
                
        elif opcion == "5":
            print("Recorrido preorden:")
            if arbol.is_empty():
                print("El arbol esta vacio")
            else:
                arbol.recorridoPreorden()
                
        elif opcion == "6":
            dato = int(input("Ingrese el ID del incidente a buscar: "))
            encontrado = arbol.buscar(dato)
            if encontrado is not None:
                print(f"Incidente encontrado:\n{encontrado}")
            else:
                print(f"El incidente con ID {dato} no fue encontrado.")
                
        elif opcion == "7":
            dato = int(input("Ingrese el ID del incidente a eliminar: "))
            arbol.eliminarNodo(dato)
            print(f"Proceso de eliminacion finalizado para ID {dato}.")
            
        elif opcion == "8":
            if not arbol.is_empty():
                print(f"Menor ID: {arbol.obtenerMenor()}")
                print(f"Mayor ID: {arbol.obtenerMayor()}")
            else:
                print("El arbol esta vacio")
                
        elif opcion == "9":
            print(f"Total de incidentes registrados: {arbol.contarNodos()}")
            
        elif opcion == "10":
            nivel = input("Ingrese el nivel de riesgo a buscar (ej. Critico): ")
            print(f"Incidentes con riesgo '{nivel}':")
            arbol.buscarPorNivelRiesgo(nivel)
            
        elif opcion.lower() == "salir":
            break
        else:
            print("Opcion invalida. Intente nuevamente.")