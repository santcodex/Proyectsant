# Planteamiento del Problema

**Contexto:**  
En muchas organizaciones y entornos académicos se manejan grandes volúmenes de documentos. Estos documentos pueden estar en diferentes formatos, como archivos de texto (.txt), documentos PDF (.pdf) y archivos de Word (.docx). Por ejemplo, en una universidad, cada departamento recibe informes, trabajos, tesis y otros documentos en formatos variados. A la vez, cada uno de estos archivos contiene valiosa información que requiere análisis, validación y control de calidad, pero revisarlos manualmente consume mucho tiempo.

**Problema Real:**  
Una institución educativa necesita evaluar de manera rápida y eficiente la extensión y el contenido básico de los documentos entregados por sus estudiantes. Actualmente, los coordinadores y jurados deben revisar manualmente cada documento para determinar si el trabajo cumple con los parámetros requeridos (como la extensión mínima en líneas, palabras o caracteres) y, en ocasiones, esta revisión es esencial para detectar posibles desviaciones en la presentación del contenido o incluso detectar errores en la compilación de información.

El proceso actual presenta los siguientes inconvenientes:
- **Trabajo Manual Excesivo:** La revisión manual de cada archivo, independientemente de su extensión, resulta lenta y consume recursos humanos.
- **Errores Humanos:** El recuento manual de líneas, palabras o caracteres puede ser impreciso, llevando a inconsistencias en la evaluación.
- **Diversidad de Formatos:** Los documentos se encuentran en distintos formatos, lo que obliga a utilizar diferentes herramientas para abrir cada archivo, dificultando la estandarización del análisis.

**Necesidad:**  
Se requiere una herramienta que pueda:
- Interpretar y extraer el contenido de archivos en formato `.txt`, `.pdf` y `.docx`.
- Realizar de forma automática la cuenta de líneas, palabras y caracteres de cada documento.
- Consolidar y generar un resumen o reporte que permita a los coordinadores verificar rápidamente si el documento cumple con los requisitos establecidos.

# Solución Propuesta con el Código

El script proporcionado aborda esta problemática de la siguiente manera:
- **Lectura Universal del Contenido:**  
  La función `leerArchivo` detecta la extensión del archivo y utiliza la herramienta adecuada (método de lectura de texto, `PyPDF2` para PDF o `python-docx` para archivos Word) para extraer el contenido del documento.

- **Extracción de Métricas Básicas:**  
  Mediante la función `contarArchivo`, el código procesa el contenido extraído y realiza el conteo de líneas, palabras y caracteres. Esto proporciona las métricas esenciales que se requieren para validar la extensión y calidad del documento.

- **Generación Automática del Reporte:**  
  Con la función `escribirResumen`, se genera un resumen en un nuevo archivo que consolida los datos obtenidos, permitiendo una verificación rápida y estandarizada. De este modo, los responsables pueden comparar el contenido entregado con los estándares requeridos, sin necesidad de abrir manualmente cada documento para realizar el análisis.

# Impacto y Beneficios

- **Eficiencia en la Revisión:**  
  Automatizando la lectura y el análisis de los documentos, se reduce significativamente el tiempo invertido en la revisión y se minimiza la posibilidad de errores humanos.

- **Adaptabilidad y Escalabilidad:**  
  Al soportar múltiples formatos de archivo, la herramienta es versátil y puede ser implementada en diferentes áreas: desde la educación hasta el sector editorial o cualquier industria que maneje grandes volúmenes de documentos.

- **Control de Calidad:**  
  Los reportes automáticos permiten establecer métricas comparativas a lo largo del tiempo, ayudando a mejorar estándares y detectar rápidamente desviaciones en los trabajos entregados.

- **Facilidad de Integración:**  
  Este script puede integrarse en sistemas de gestión documental o en pipelines automatizados de procesamiento de información, contribuyendo a la digitalización y optimización de procesos administrativos.
  
  # Herramientas Utilizadas
- Python.
- Librería os (Para el manejo de archivos)
- Librería PyPDF2 y docx (Para lectura de archivos PDF y docx, además de los txt) 
