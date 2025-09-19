# Delta-data_CRUD
delta data project CRUD 
Este proyecto es una aplicación web de gestión de créditos desarrollada en Python usando Flask y SQLite. Permite registrar, actualizar, eliminar y visualizar créditos de clientes, además de generar gráficos interactivos con Chart.js para analizar los montos otorgados.

Características

- Registro de créditos: Permite ingresar créditos nuevos con datos de cliente, monto, tasa de interés, plazo y fecha de otorgamiento.

- Actualización de créditos: Modifica la información de un crédito existente.

- Eliminación de créditos: Borra créditos por su ID.

- Visualización de datos: Genera gráficos interactivos que muestran los montos de los créditos por cliente (solo un grafico).

- Interfaz sencilla: Navegación fácil con botones y formularios claros.

Tecnologías

- Backend: Python 3.11, Flask

- Base de datos: SQLite (archivo .db local)

- Frontend: HTML, CSS, JavaScript, Chart.js

- Plantillas: Jinja2 para renderizado dinámico

Estructura del proyecto
Delta-data_CRUD/
  DataBase/
    DeltaDataDB.db      # Base de datos SQLite
    CRUD/
        templates/
            index.html      # Página principal con formulario
            actualizar_credito.html
            graphics.html   # Página de gráficos interactivos
            static/             # Archivos CSS o JS si se usan
            main.py             # Aplicación Flask
 README.md

Instalación y ejecución

Clonar el repositorio:

git clone https://github.com/Christian99-EG/Delta-data_CRUD.git

cd Delta-data_CRUD


