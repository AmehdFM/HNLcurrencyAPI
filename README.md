# HNLcurrencyAPI

Esta API esta destinada para el monitoreo y conversion de diferentes divisas con respecto al Lempira hondureño (HNL).
Los precios son extraidos de [currencyapi](https://app.currencyapi.com/)
El proyecto esta desplegado en vercel.

## Monedas Soportadas

Monedas las cuales tienen un seguimiento:
- SVC (Colon Salvadoreño)
- USD (Dólar Estadounidense)
- EUR (Euro)
- CRC (Colón Costarricense)
- GTQ (Quetzal Guatemalteco)
- NIO (Córdoba Nicaragüense)
- CNY (Yuan Chino)
- RUB (Rublo Ruso)

## Endpoints

### Obtener Historial de Divisas

Este endpoint permite obtener el historial de una divisa dentro de un rango de fechas.

- **URL**: `/historial/{divisa}/{fecha_inicio}/{fecha_fin}`
- **Método HTTP**: GET
- **Parámetros de la URL**:
  - `divisa` (str): La abreviatura de la divisa deseada (por ejemplo, USD).
  - `fecha_inicio` (str): La fecha de inicio del rango en formato YYYY-MM-DD.
  - `fecha_fin` (str): La fecha de fin del rango en formato YYYY-MM-DD.
- **Respuesta Exitosa**:
  - Código de Estado: 200 OK
  - Tipo de Contenido: application/json
  - Cuerpo de la Respuesta: Lista de registros de historial de la divisa.

### Obtener Historial por Divisa

Este endpoint permite obtener el historial completo de una divisa.

- **URL**: `/historial/{divisa}`
- **Método HTTP**: GET
- **Parámetros de la URL**:
  - `divisa` (str): La abreviatura de la divisa deseada (por ejemplo, EUR).
- **Respuesta Exitosa**:
  - Código de Estado: 200 OK
  - Tipo de Contenido: application/json
  - Cuerpo de la Respuesta: Lista de registros de historial de la divisa.

### Obtener Todos los Datos

Este endpoint permite obtener todos los datos de la tabla historial_divisas.

- **URL**: `/datos`
- **Método HTTP**: GET
- **Respuesta Exitosa**:
  - Código de Estado: 200 OK
  - Tipo de Contenido: application/json
  - Cuerpo de la Respuesta: Lista de todos los datos de historial_divisas.

### Convertir Monedas

Este endpoint permite realizar conversiones entre monedas. Solo se admiten conversiones entre Lempiras (HNL) y otras divisas o viceversa. La tasa de cambio utilizada es la más reciente disponible en la base de datos.

- **URL**: `/convertir`
- **Método HTTP**: GET
- **Parámetros de consulta**:
  - `moneda_origen` (str): La abreviatura de la moneda de origen. Puede ser "HNL" (Lempiras) o la abreviatura de otra divisa.
  - `moneda_destino` (str): La abreviatura de la moneda de destino. Puede ser "HNL" (Lempiras) o la abreviatura de otra divisa.
  - `cantidad` (float): La cantidad de la moneda de origen que se desea convertir.
- **Respuesta Exitosa**:
  - Código de Estado: 200 OK
  - Tipo de Contenido: application/json
  - Cuerpo de la Respuesta: La cantidad de la moneda de destino que se puede comprar con la cantidad ingresada de la moneda de origen.