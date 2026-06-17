def registrar_pais(lista_paises):
    """Solicita datos de un nuevo pais, valida entradas y lo agrega a la lista."""

    print("\n --- Registrar nuevo pais ---")

    # Validar nombre
    while True:
        nombre = input("Nombre del pais: ").strip()
        if not nombre:
            print("[ERROR] El nombre no puede estar vacio.")
            continue

        if any(p["nombre"].lower() == nombre.lower() for p in lista_paises):
            print("[ERROR] Ese pais ya existe.")
            continue
        break

    # Validar poblacion
    while True:
        try:
            poblacion = int(input("Poblacion: ").strip())
            if poblacion <= 0:
                print("[ERROR] Debe ser mayor a 0.")
                continue
            break
        except ValueError:
            print("[ERROR] Numero invalido.")

    # Validar superficie
    while True:
        try:
            superficie = int(input("Superficie (km²): ").strip())
            if superficie <= 0:
                print("[ERROR] Debe ser mayor a 0.")
                continue
            break
        except ValueError:
            print("[ERROR] Numero invalido.")

    # Validar continente
    while True:
        continente = input("Continente: ").strip()
        if not continente:
            print("[ERROR] No puede estar vacio.")
            continue
        break

    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }

    lista_paises.append(nuevo_pais)

    print(f"\n[OK] '{nombre}' agregado correctamente.")