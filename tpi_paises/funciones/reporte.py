def obtener_max_min_poblacion(lista_paises):
    pais_maximo = lista_paises[0]
    pais_minimo = lista_paises[0]

    for pais in lista_paises:
        if pais["poblacion"] > pais_maximo["poblacion"]:
            pais_maximo = pais
        if pais["poblacion"] < pais_minimo["poblacion"]:
            pais_minimo = pais

    return pais_maximo, pais_minimo


def calcular_promedio_poblacion(lista_paises):
    total_poblacion = 0
    for pais in lista_paises:
        total_poblacion += pais["poblacion"]

    promedio = total_poblacion / len(lista_paises)
    return promedio


def calcular_promedio_superficie(lista_paises):
    total_superficie = 0
    for pais in lista_paises:
        total_superficie += pais["superficie"]

    promedio = total_superficie / len(lista_paises)
    return promedio


def contar_por_continente(lista_paises):
    conteo_continentes = {}

    for pais in lista_paises:
        continente = pais["continente"].strip().capitalize()

        if continente in conteo_continentes:
            conteo_continentes[continente] += 1
        else:
            conteo_continentes[continente] = 1

    return conteo_continentes


def ejecutar_reporte(lista_paises):
    if len(lista_paises) == 0:
        print("No hay países cargados en el sistema todavía.")
        return

    print("\n=========================================================================")
    print("                      REPORTE ESTADÍSTICO DE PAÍSES                      ")
    print("=========================================================================")

    p_max, p_min = obtener_max_min_poblacion(lista_paises)
    print(f"-> País con MAYOR población: {p_max['nombre']} ({p_max['poblacion']} hab.)")
    print(f"-> País con MENOR población: {p_min['nombre']} ({p_min['poblacion']} hab.)")
    print("-------------------------------------------------------------------------")

    prom_poblacion = calcular_promedio_poblacion(lista_paises)
    prom_superficie = calcular_promedio_superficie(lista_paises)

    print(f"-> Promedio de población general: {prom_poblacion:.2f} habitantes")
    print(f"-> Promedio de superficie general: {prom_superficie:.2f} km²")
    print("-------------------------------------------------------------------------")

    dicc_continentes = contar_por_continente(lista_paises)
    print("-> Cantidad de países por continente:")

    for continente, cantidad in dicc_continentes.items():
        print(f"   * {continente}: {cantidad} {'país' if cantidad == 1 else 'países'}")

    print("=========================================================================")
