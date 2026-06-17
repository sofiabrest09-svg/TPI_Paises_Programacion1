from funciones.datos import mostrar_lista_paises

def pedir_direccion():
    """Pide al usuario si el orden es ascendente o descendente.Devuelve True si es descendente."""
    while True:
        direccion = input(" Orden: [1] Ascendente [2] Descendente: ").strip()
        if direccion == "1":
            return False
        elif direccion == "2":
            return True
        else:          
            print(" [ERROR] Opción no válida. Por favor, ingrese 1 o 2.")

def ordenar_por_nombre(lista_paises):
    """Ordena la lista de paises por nombre (A-Z o Z-A)"""
    descendente = pedir_direccion()
    lista_paises.sort(key=lambda p: p["nombre"].lower(), reverse=descendente)
    orden_texto = "descendente" if descendente else "ascendente"
    print(f"\n Lista de países ordenada por nombre ({orden_texto}):")
    mostrar_lista_paises(lista_paises)

def ordenar_por_poblacion(lista_paises):
    """Orden la lista de paises por población (menor a mayor o mayor a menor)"""
    descendente = pedir_direccion()
    lista_paises.sort(key=lambda p: p["poblacion"], reverse=descendente)
    orden_texto = "descendente" if descendente else "ascendente"
    print(f"\n Lista de países ordenada por población ({orden_texto}):")
    mostrar_lista_paises(lista_paises)

def ordenar_por_superficie(lista_paises):
    """Orden la lista de paises por superficie (menor a mayor o mayor a menor)"""
    descendente = pedir_direccion()
    lista_paises.sort(key=lambda p: p["superficie"], reverse=descendente)
    orden_texto = "descendente" if descendente else "ascendente"
    print(f"\n Lista de países ordenada por superficie ({orden_texto}):")
    mostrar_lista_paises(lista_paises)

def ejecutar_ordenamiento(lista_paises):
    """Ejecuta el proceso de ordenamiento según la elección del usuario."""

    if not lista_paises:
        print("\n [AVISO] No hay países para ordenar. Por favor, ingresa algunos países primero.")
        return
    
    print("\n --- Ordenar países ---")
    print(" [1] Ordenar por nombre")
    print(" [2] Ordenar por población")
    print(" [3] Ordenar por superficie")

    opcion = input("\n Elige una opción: ").strip()

    if opcion == "1":
        ordenar_por_nombre(lista_paises)
    elif opcion == "2":
        ordenar_por_poblacion(lista_paises)
    elif opcion == "3":
        ordenar_por_superficie(lista_paises)
    else:
        print("\n [ERROR] Opción no válida. Por favor, ingresa 1, 2 o 3.")