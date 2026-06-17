from funciones.datos import mostrar_lista_paises


def filtrar_paises_por_continente(lista_paises):
    """Filtra paises por continente."""

    continente = input("Continente a filtrar: ").strip()

    if not continente:
        print("[ERROR] El continente no puede estar vacio.")
        return

    resultados = [
        p for p in lista_paises
        if p["continente"].lower() == continente.lower()
    ]

    if not resultados:
        print(f"\n[AVISO] No se encontraron paises en '{continente}'.")
    else:
        print(f"\nPaises en el continente '{continente}':")
        mostrar_lista_paises(resultados)


def filtrar_por_rango_poblacion(lista_paises):
    """Filtra paises por rango de poblacion."""

    try:
        minimo = int(input("Poblacion minima: ").strip())
        maximo = int(input("Poblacion maxima: ").strip())
    except ValueError:
        print("[ERROR] Numero invalido.")
        return

    if minimo > maximo:
        print("[ERROR] El minimo no puede ser mayor al maximo.")
        return

    resultados = [
        p for p in lista_paises
        if minimo <= p["poblacion"] <= maximo
    ]

    if not resultados:
        print("\n[AVISO] No se encontraron paises en ese rango.")
    else:
        mostrar_lista_paises(resultados)


def filtrar_por_rango_superficie(lista_paises):
    """Filtra paises por rango de superficie."""

    try:
        minimo = int(input("Superficie minima (km²): ").strip())
        maximo = int(input("Superficie maxima (km²): ").strip())
    except ValueError:
        print("[ERROR] Numero invalido.")
        return

    if minimo > maximo:
        print("[ERROR] El minimo no puede ser mayor al maximo.")
        return

    resultados = [
        p for p in lista_paises
        if minimo <= p["superficie"] <= maximo
    ]

    if not resultados:
        print("\n[AVISO] No se encontraron paises en ese rango.")
    else:
        mostrar_lista_paises(resultados)


def aplicar_filtros(lista_paises):
    """Submenu de filtros."""

    while True:
        print("\n--- FILTROS ---")
        print("[1] Por continente")
        print("[2] Por poblacion")
        print("[3] Por superficie")
        print("[4] Volver")

        opcion = input("Opcion: ").strip()

        if opcion == "1":
            filtrar_paises_por_continente(lista_paises)
        elif opcion == "2":
            filtrar_por_rango_poblacion(lista_paises)
        elif opcion == "3":
            filtrar_por_rango_superficie(lista_paises)
        elif opcion == "4":
            break
        else:
            print("[ERROR] Opcion invalida.")
