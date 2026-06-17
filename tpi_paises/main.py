from funciones.datos import cargar_csv, guardar_csv, mostrar_lista_paises
from funciones.altas import registrar_pais
from funciones.actualizar import actualizar_pais
from funciones.busquedas import ejecutar_busqueda
from funciones.filtros import aplicar_filtros
from funciones.ordenamiento import ejecutar_ordenamiento
from funciones.estadisticas import mostrar_reporte_estadistico

ARCHIVO_CSV = 'paises.csv'


def mostrar_menu():
    print("\n=== Menu Principal ===")
    print("[1]. Mostrar lista completa de paises")
    print("[2]. Registrar un nuevo pais")
    print("[3]. Actualizar datos de un pais")
    print("[4]. Buscar pais")
    print("[5]. Filtrar paises")
    print("[6]. Ordenar paises")
    print("[7]. Ver reporte estadistico")
    print("[8]. Guardar cambios y salir")


def main():
    paises = cargar_csv(ARCHIVO_CSV)

    if not paises:
        print("\n[ERROR] No se cargaron paises.")

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opcion (1-8): ").strip()

        if opcion == "1":
            mostrar_lista_paises(paises)

        elif opcion == "2":
            registrar_pais(paises)

        elif opcion == "3":
            actualizar_pais(paises)

        elif opcion == "4":
            ejecutar_busqueda(paises)

        elif opcion == "5":
            aplicar_filtros(paises)

        elif opcion == "6":
            ejecutar_ordenamiento(paises)

        elif opcion == "7":
            mostrar_reporte_estadistico(paises)

        elif opcion == "8":
            guardar_csv(ARCHIVO_CSV, paises)
            print("\nCambios guardados. Saliendo del programa.")
            break

        else:
            print("\n[ERROR] Opcion invalida.")


if __name__ == "__main__":
    main()
    
