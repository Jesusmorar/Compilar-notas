# 🎓 Ecosistema de Automatización Académica (ETL & RPA)

Este proyecto es una solución integral para la **limpieza, consolidación y automatización** de reportes de notas entre las plataformas Brightspace y Q10. Elimina el error humano y reduce el tiempo de procesamiento manual en un 90%.



## 🎯 Problema a Resolver
Las plataformas educativas suelen exportar datos con formatos inconsistentes (tildes, mayúsculas desordenadas, nombres fragmentados). Este ecosistema estandariza la información y calcula notas finales bajo reglas de negocio específicas para cada materia.

## 🚀 Funcionalidades Principales
- **Limpieza de Datos (Data Wrangling):** Normalización de nombres (remoción de tildes, corrección de `Title Case`) manteniendo caracteres especiales como la 'ñ'.
- **Lógica de Negocio Dinámica:** Cálculo de notas finales con diferentes ponderaciones (50/50, 40/60 o nota única) según el código de la materia.
- **Consolidación en Excel:** Generación de un archivo `.xlsx` con hojas separadas por materia, organizadas alfabéticamente y con ajuste automático de columnas.
- **Seguridad y Privacidad:** Incluye un generador de **Mock Data** (datos sintéticos) para realizar pruebas de estrés sin exponer datos reales de instituciones.

## 🛠️ Stack Tecnológico
- **Python 3.13**
- **Pandas:** Manipulación de estructuras de datos.
- **XlsxWriter:** Motor de escritura para reportes Excel personalizados.
- **OS & Random:** Gestión de rutas de archivos y generación de datos aleatorios.

## 📁 Estructura del Repositorio
* `datos_prueba.py`: Script para generar 10 archivos CSV de prueba con "ruido" en los datos (errores de formato a propósito).
* `procesar_notas.py`: Script principal que ejecuta la limpieza y genera el consolidado final.
* `.gitignore`: Configuración para prevenir la subida accidental de datos sensibles.
* `requirements.txt`: Lista de librerías necesarias.

## 💻 Instrucciones de Uso

1. **Clonar el repositorio:**
    Escribe en tu terminal: git clone https://github.com/TU_USUARIO/Compilar-notas.git

2. **Instalar dependencias:**
    pip install -r requirements.txt

3. **Generar el entorno de pruebas:**
    python datos_prueba.py

4. **Procesar y consolidar las notas:**
    python procesar_notas.py

El resultado aparecerá en la carpeta /Resultados.