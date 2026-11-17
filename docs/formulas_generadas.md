
# Generación de fórmulas DAX con Inteligencia Artificial

## 1. Objetivo

El objetivo de este documento es explicar cómo se utilizaron fórmulas DAX para analizar la información del mercado de energías renovables en Power BI, con apoyo de herramientas de Inteligencia Artificial.

## 2. Uso de Inteligencia Artificial

Se utilizó IA como apoyo para proponer fórmulas DAX, comprender sus funciones y realizar ajustes para adaptarlas a las tablas y columnas del proyecto.

### Prompt utilizado

"Actúa como experto en Power BI y DAX. Ayúdame a crear medidas para analizar un conjunto de datos de energías renovables. Necesito calcular energía total, costos, ingresos, precios promedio, número de transacciones, márgenes, participación y crecimiento interanual. Explica cada fórmula y adapta las expresiones a los nombres de mis tablas y columnas."

## 3. Fórmulas DAX implementadas

### 1. Energía Total (MWh)

```DAX
Energía Total (MWh) =
SUM('TRANSACCIONES (1)'[energia_mwh])
```

Objetivo: calcular la energía total comercializada.

### 2. Costos Totales (USD)

```DAX
Costos Totales (USD) =
SUMX(
    'TRANSACCIONES (1)',
    'TRANSACCIONES (1)'[energia_mwh] *
    'TRANSACCIONES (1)'[costo_operacion_usd_mwh]
)
```

Objetivo: calcular los costos de operación.

### 3. Ingresos Totales (USD)

```DAX
Ingresos Totales (USD) =
SUMX(
    'TRANSACCIONES (1)',
    'TRANSACCIONES (1)'[energia_mwh] *
    'TRANSACCIONES (1)'[precio_venta_usd_mwh]
)
```

Objetivo: calcular los ingresos por venta de energía.

### 4. Número de Transacciones

```DAX
Número de Transacciones =
DISTINCTCOUNT('TRANSACCIONES (1)'[id_transaccion])
```

Objetivo: contar las transacciones realizadas.

### 5. Precio Promedio de Venta

```DAX
Precio Promedio de Venta =
DIVIDE(
    [Ingresos Totales (USD)],
    [Energía Total (MWh)]
)
```

Objetivo: calcular el precio promedio de venta por MWh.

### 6. Energía por Año

```DAX
Energía por Año =
CALCULATE(
    [Energía Total (MWh)],
    FILTER(
        ALL('TRANSACCIONES (1)'[fecha]),
        YEAR('TRANSACCIONES (1)'[fecha]) =
        YEAR(MAX('TRANSACCIONES (1)'[fecha]))
    )
)
```

Objetivo: analizar la energía comercializada por año.

### 7. Precio Promedio de Compra

```DAX
Precio Promedio de Compra =
AVERAGE('TRANSACCIONES (1)'[precio_compra_usd_mwh])
```

Objetivo: calcular el precio promedio de compra.

### 8. Margen Comercial (USD)

```DAX
Margen Comercial (USD) =
[Ingresos Totales (USD)] - [Costos Totales (USD)]
```

Objetivo: calcular la diferencia entre ingresos y costos.

### 9. Participación de Energía (%)

```DAX
Participación de Energía (%) =
DIVIDE(
    [Energía Total (MWh)],
    CALCULATE(
        [Energía Total (MWh)],
        ALL('TRANSACCIONES (1)')
    ),
    0
)
```

Objetivo: calcular la participación porcentual de energía.

### 10. Crecimiento Interanual (%)

```DAX
Crecimiento Interanual (%) =
VAR EnergiaActual = [Energía Total (MWh)]
VAR EnergiaAnterior =
    CALCULATE(
        [Energía Total (MWh)],
        SAMEPERIODLASTYEAR('TRANSACCIONES (1)'[fecha])
    )
RETURN
    DIVIDE(
        EnergiaActual - EnergiaAnterior,
        EnergiaAnterior,
        0
    )
```

Objetivo: comparar la energía comercializada con el año anterior.

## 4. Ajustes realizados

Las propuestas de IA se adaptaron a los nombres reales de las tablas y columnas del proyecto.

Se utilizaron funciones como SUM, SUMX, DISTINCTCOUNT, AVERAGE, DIVIDE, CALCULATE, FILTER y SAMEPERIODLASTYEAR.

También se organizaron las medidas dentro del modelo de Power BI y se configuró el formato porcentual para las medidas de participación y crecimiento.

## 5. Resultados

Las medidas permiten analizar la energía comercializada, los costos, los ingresos, los precios de compra y venta, el margen comercial y la evolución de la energía en el tiempo.

## 6. Conclusión

El uso de Inteligencia Artificial facilitó la construcción y comprensión de las fórmulas DAX. La combinación de IA y Power BI permitió desarrollar un análisis más completo y mejorar la interpretación de los datos del sector de energías renovables.
