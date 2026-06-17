def ejecutar_busqueda(lista_paises):
    """Busca paises cuyo nombre contenga el texto ingresado (parcial o exacto):"""

    print("\n --- Buscar pais por nombre ---")

    termino = input(" Ingresa el nombre o parte del nombre: ").strip()

    if not termino:
        print(" [ERROR] El termino de busqueda no puede estar vacio.")
        return
    
    # Filtramos los paises que contengan el termino (ignorando mayusculas)

    resultados = [
        pais for pais in lista_paises
        if termino.lower() in pais["nombre"].lower()        
    ]

    if not resultados:
        print(f"\n [AVISO] No se encontraron paises que coincidan con '{termino}'.")
        return
    
    print(f"\n Resultados para '{termino}' ({len(resultados)} encontrados):")
    print(f"\n {'Pais':<20} {'Poblacion':>15} {'Superficie (km2)':>18} {'Continente':<15}")
    print(" " + "-" * 72)
    for pais in resultados:
        print(
            f" {pais['nombre']:<20} {pais['poblacion']:>15,} {pais['superficie']:>18,} {pais['continente']:<15}"
        )