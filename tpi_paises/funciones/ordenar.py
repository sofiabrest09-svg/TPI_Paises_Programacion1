def ordenar_por_nombre(lista_paises):
    lista_ordenada = list(lista_paises)
    n = len(lista_ordenada)

    for i in range(n):
        for j in range(0, n - i - 1):
            if (
                lista_ordenada[j]["nombre"].lower()
                > lista_ordenada[j + 1]["nombre"].lower()
            ):
                lista_ordenada[j], lista_ordenada[j + 1] = (
                    lista_ordenada[j + 1],
                    lista_ordenada[j],
                )
    return lista_ordenada


def ordenar_por_poblacion(lista_paises):
    lista_ordenada = list(lista_paises)
    n = len(lista_ordenada)

    for i in range(n):
        for j in range(0, n - i - 1):
            if lista_ordenada[j]["poblacion"] > lista_ordenada[j + 1]["poblacion"]:
                lista_ordenada[j], lista_ordenada[j + 1] = (
                    lista_ordenada[j + 1],
                    lista_ordenada[j],
                )
    return lista_ordenada


def ordenar_por_superficie(lista_paises):
    lista_ordenada = list(lista_paises)
    n = len(lista_ordenada)

    for i in range(n):
        for j in range(0, n - i - 1):
            if lista_ordenada[j]["superficie"] > lista_ordenada[j + 1]["superficie"]:
                lista_ordenada[j], lista_ordenada[j + 1] = (
                    lista_ordenada[j + 1],
                    lista_ordenada[j],
                )
    return lista_ordenada


def ejecutar_ordenamiento(lista_paises):
    if len(lista_paises) == 0:
        print("No hay países cargados en el sistema todavía.")
        return

    while True:
        print("\n---------------------------------")
        print("      SUBMENÚ DE ORDENAMIENTO    ")
        print("---------------------------------")
        print(" [1] Ordenar por Nombre")
        print(" [2] Ordenar por Población")
        print(" [3] Ordenar por Superficie")
        print(" [4] Volver al Menú Principal")
        print("---------------------------------")

        opcion_orden = input("Seleccione una opción de ordenamiento (1-4): ").strip()

        if opcion_orden == "1":
            lista_ordenada = ordenar_por_nombre(lista_paises)
            titulo = "Nombre"
        elif opcion_orden == "2":
            lista_ordenada = ordenar_por_poblacion(lista_paises)
            titulo = "Población"
        elif opcion_orden == "3":
            lista_ordenada = ordenar_por_superficie(lista_paises)
            titulo = "Superficie"
        elif opcion_orden == "4":
            print("Volviendo al menú principal...")
            break
        else:
            print("Opción inválida. Elija un número del 1 al 4.")
            continue

        print(f"\nResultados del ordenamiento por {titulo}:")
        print(
            "========================================================================="
        )
        print(
            f"{'País':<20} | {'Población':<15} | {'Superficie (km²)':<15} | {'Continente':<15}"
        )
        print(
            "========================================================================="
        )

        for pais in lista_ordenada:
            print(
                f"{pais['nombre']:<20} | {pais['poblacion']:<15} | {pais['superficie']:<15} | {pais['continente']:<15}"
            )
        print(
            "========================================================================="
        )
