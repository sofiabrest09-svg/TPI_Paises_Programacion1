def obtener_max_min_poblacion(lista_paises):
    """Devuelte e imprime el pais con mayor y menor poblacion."""

    mayor = lista_paises[0]
    menor = lista_paises[0]

    for pais in lista_paises[1:]:
        if pais["poblacion"] > mayor["poblacion"]:
            mayor = pais
        if pais["poblacion"] < menor["poblacion"]:
            menor = pais

    print(f"\n País con MAYOR población: {mayor['nombre']} ({mayor['poblacion']:,} hab.)")
    print(f" País con MENOR población: {menor['nombre']} ({menor['poblacion']:,} hab.)")

def calcular_promedio_poblacion(lista_paises):
    """Devuelve e imprime el promedio de población de los países."""

    total = 0
    for pais in lista_paises:
        total += pais["poblacion"]

    promedio = total // len(lista_paises)
    print(f"\n Promedio de población: {promedio:,} hab.")

def calcular_promedio_superficie(lista_paises):
    """Calcula e imprime el promedio de superficie."""

    total = 0
    for pais in lista_paises:
        total += pais["superficie"]

    promedio = total // len(lista_paises)
    print(f" Promedio de superficie : {promedio:,} km²")

def contar_por_continente(lista_paises):
    """Cuenta e imprime el número de países por continente."""

    conteo = {}
    for pais in lista_paises:
        continente = pais["continente"].strip().capitalize()#agrego esto para que si se agrega un continente en
                                                            #minuscula, en la estadistica aparezca en mayuscula
        if continente in conteo:
            conteo[continente] += 1
        else:
            conteo[continente] = 1

    print("\n Número de países por continente:")
    for continente, cantidad in conteo.items():
        print(f"  {continente:<15}: {cantidad} país/es")

def mostrar_reporte_estadistico(lista_paises):
    """Muestra el reporte completo de estadisticas."""

    if not lista_paises:
        print("\n [AVISO] No hay datos para calcular estadisticas.")
        return
    
    print("\n ====== REPORTE ESTADÍSTICO ======")
    obtener_max_min_poblacion(lista_paises)
    calcular_promedio_poblacion(lista_paises)
    calcular_promedio_superficie(lista_paises)
    contar_por_continente(lista_paises)
    print(" ====== FIN DEL REPORTE ======")