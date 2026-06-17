def ejecutar_busqueda(lista_paises):
    if len(lista_paises) == 0:
        print("No hay países cargados en el sistema todavía.")
        return

    busqueda = input("Ingrese el nombre del pais a buscar: ").strip().lower()

    coincidencia = False

    print("\nResultados de la búsqueda:")
    print("=========================================================================")
    print(
        f"{'País':<20} | {'Población':<15} | {'Superficie (km²)':<15} | {'Continente':<15}"
    )
    print("=========================================================================")

    for pais in lista_paises:
        if busqueda in pais["nombre"].strip().lower():
            print(
                f"{pais['nombre']:<20} | {pais['poblacion']:<15} | {pais['superficie']:<15} | {pais['continente']:<15}"
            )
            coincidencia = True

    if not coincidencia:
        print("No se encontraron países que coincidan con la búsqueda.")
