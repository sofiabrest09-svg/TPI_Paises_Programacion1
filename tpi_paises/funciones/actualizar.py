def actualizar_pais(lista_paises):
    """Busca un pais por nombre exacto y permite modificar su poblacion y superficie."""

    print("\n--- Actualizar datos de un pais ---")

    nombre_buscar = input("Ingresa el nombre exacto del pais: ").strip()

    if not nombre_buscar:
        print("[ERROR] El nombre no puede estar vacio.")
        return

    pais_encontrado = None

    for pais in lista_paises:
        if pais["nombre"].lower() == nombre_buscar.lower():
            pais_encontrado = pais
            break

    if not pais_encontrado:
        print(f"[AVISO] No se encontro el pais '{nombre_buscar}'.")
        return

    print(f"\nPais encontrado: {pais_encontrado['nombre']}")
    print(f"Poblacion actual: {pais_encontrado['poblacion']:,}")
    print(f"Superficie actual: {pais_encontrado['superficie']:,} km²")

    # Poblacion
    while True:
        try:
            entrada = input("Nueva poblacion (Enter para mantener actual): ").strip()

            if entrada == "":
                nueva_poblacion = pais_encontrado["poblacion"]
            else:
                nueva_poblacion = int(entrada)

            if nueva_poblacion <= 0:
                print("[ERROR] Debe ser mayor a 0.")
                continue

            break
        except ValueError:
            print("[ERROR] Numero invalido.")

    # Superficie
    while True:
        try:
            entrada = input("Nueva superficie (Enter para mantener actual): ").strip()

            if entrada == "":
                nueva_superficie = pais_encontrado["superficie"]
            else:
                nueva_superficie = int(entrada)

            if nueva_superficie <= 0:
                print("[ERROR] Debe ser mayor a 0.")
                continue

            break
        except ValueError:
            print("[ERROR] Numero invalido.")

    pais_encontrado["poblacion"] = nueva_poblacion
    pais_encontrado["superficie"] = nueva_superficie

    print(f"\n[OK] Datos del pais '{pais_encontrado['nombre']}' actualizados.")