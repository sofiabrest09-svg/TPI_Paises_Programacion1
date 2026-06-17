import csv

def cargar_csv(ruta_archivo):
    """Lee el archivo CSV y devuelve una lista de diccionarios con los datos de cada pais."""
    lista_paises = []

    try:
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            lector = csv.reader(archivo)
            next(lector) # Saltamos la primera fila (encabezados)

            for fila in lector:
                print("FILA:", repr(fila))
                if fila:
                    pais = {
                        "nombre": fila[0],
                        "poblacion": int(fila[1].strip()),
                        "superficie": int(fila[2].strip()),
                        "continente": fila[3],
                    }
                    lista_paises.append(pais)

    except FileNotFoundError:
        print(f"    [ERROR] No se encontro el archivo: {ruta_archivo}")

    return lista_paises

def guardar_csv(ruta_archivo, lista_paises):
    """Guarda la lista de paises en un archivo CSV."""
    try:
        with open(ruta_archivo, "w", encoding="utf-8", newline="") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(["nombre", "poblacion", "superficie", "continente"]) # Escribimos los encabezados

            for pais in lista_paises:
                escritor.writerow([
                    pais["nombre"],
                    pais["poblacion"],
                    pais["superficie"],
                    pais["continente"]
                ])
        print(f"\n [OK] Cambios guardados en '{ruta_archivo}' exitosamente.")
    except IOError as e:
        print(f"    [ERROR] No se pudo guardar el archivo: {e}")

def mostrar_lista_paises(lista_paises):
    """Muestra todos los paises en formato de tabla por consola."""
    if not lista_paises:
        print("\n    [AVISO] No hay paises para mostrar.")
        return

    print(f"\n {'#':<4} {'Pais':<20} {'Poblacion':>15} {'Superficie (km²)':>18} {'Continente':<15}")
    print("  " + "-" * 75)
    for i, pais in enumerate(lista_paises, start=1):
        print(
            f" {i:<4} {pais['nombre']:<20} {pais['poblacion']:>15,} {pais['superficie']:>18,} {pais['continente']:<15}"
        )
    
    print(f"\n Total: {len(lista_paises)} paises cargados.")