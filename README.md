[README.md](https://github.com/user-attachments/files/29069739/README.md)
# TPI_Paises_Programacion1
Trabajo Practico Integrador - Programacion 1 UTN
# Gestión de Datos de Países en Python

**Trabajo Práctico Integrador (TPI) — Programación 1**
Tecnicatura Universitaria en Programación — UTN

---

## Descripción

Aplicación de consola en Python que permite gestionar un dataset de países (almacenado en CSV), aplicando listas, diccionarios, funciones, filtros, ordenamientos y estadísticas.

---

## Estructura del proyecto

```
tpi_paises/
├── funciones/
│   ├── __init__.py
│   ├── datos.py          # Lectura y escritura del CSV + mostrar tabla
│   ├── altas.py          # Registrar nuevo país con validaciones
│   ├── actualizar.py     # Modificar población y superficie
│   ├── busquedas.py      # Búsqueda por nombre (parcial o exacta)
│   ├── filtros.py        # Filtros por continente y rangos
│   ├── ordenamiento.py   # Ordenar por nombre, población o superficie
│   └── estadisticas.py   # Estadísticas y reporte
├── paises.csv            # Dataset base
├── main.py               # Menú principal
└── README.md
```

---


## Menú principal

```
=========================================================
       SISTEMA DE GESTIÓN DE DATASET DE PAÍSES
=========================================================
 [1] Mostrar lista completa de países
 [2] Registrar un nuevo país
 [3] Actualizar datos de un país (Población/Superficie)
 [4] Buscar país por nombre (coincidencia parcial)
 [5] Filtrar países (Continente o Rangos)
 [6] Ordenar países por columnas
 [7] Ver reporte estadístico e indicadores
 [8] Guardar cambios y salir
=========================================================
```

---

## Ejemplos de uso

### Buscar un país
```
Ingresá el nombre o parte del nombre: arg
→ Muestra: Argentina
```

### Filtrar por rango de población
```
Población mínima: 50000000
Población máxima: 100000000
→ Muestra: Alemania, Egipto, Francia, Italia, España, Sudáfrica
```

### Reporte estadístico
```
País con MAYOR población : China (1.412.000.000 hab.)
País con MENOR población : Nueva Zelanda (5.120.000 hab.)
Promedio de población    : 301.000.000 hab.
Promedio de superficie   : 2.998.000 km²

Países por continente:
  América   : 4 país/es
  Asia      : 3 país/es
  Europa    : 5 país/es
  África    : 2 país/es
  Oceanía   : 2 país/es
```

---

## Integrantes

| Nombre |
| Brest Sofia |
| Nieva Agustina |     


---

## Links

- 📹 Video demostración: (https://youtu.be/xhtxAtzo5Fc?si=Fh4-mBfkXlo8Gj1k)
- 📄 Documentación PDF: (https://github.com/sofiabrest09-svg/TPI_Paises_Programacion1/blob/main/tpi_paises/tpi-paises-brest-nieva.pdf)
- Link repositorio en GitHub: (https://github.com/sofiabrest09-svg/TPI_Paises_Programacion1)



