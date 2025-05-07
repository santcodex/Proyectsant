import os
import PyPDF2
import docx
from datetime import datetime

def leerArchivo(rutadeArchivo):
    ext = os.path.splitext(rutadeArchivo)[1].lower()
    contenido = ""
    try:
        if ext == ".txt":
            with open(rutadeArchivo, "r", encoding="utf-8") as file:
                contenido = file.read()
        elif ext == ".pdf":
            with open(rutadeArchivo, "rb") as file:
                lectorPdf = PyPDF2.PdfReader(file)
                for pagina in lectorPdf.pages:
                    textodePagina = pagina.extract_text()
                    contenido += textodePagina + "\n"
        elif ext == ".docx":
            documento = docx.Document(rutadeArchivo)
            for parrafo in documento.paragraphs:
                contenido += parrafo.text + "\n"
        else:
            print("Tipo de archivo no soportado. Utiliza un archivo con extensión .txt, .pdf o .docx")
            return None
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return None

    return contenido

def obtener_metadatos(rutadeArchivo):
    try:
        stats = os.stat(rutadeArchivo)
        fecha_creacion = datetime.fromtimestamp(stats.st_ctime).strftime('%Y-%m-%d %H:%M:%S')
        fecha_modificacion = datetime.fromtimestamp(stats.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
        tamaño = stats.st_size
        return fecha_creacion, fecha_modificacion, tamaño
    except Exception as e:
        print(f"Error al obtener metadatos: {e}")
        return None, None, None

def contarArchivo(rutadeArchivo):
    contenido = leerArchivo(rutadeArchivo)
    if contenido is None:
        return None

    # Contar líneas
    lineas = contenido.splitlines()
    numLineas = len(lineas)

    # Contar palabras (split separa por espacios, saltos de línea, etc.)
    palabras = contenido.split()
    numPalabras = len(palabras)
    
    # Contar caracteres (incluyendo espacios y saltos de línea)
    numCaracteres = len(contenido)

    # Obtener metadatos del archivo
    fecha_creacion, fecha_modificacion, tamaño = obtener_metadatos(rutadeArchivo)

    # Crear diccionario con toda la información
    resumen = {
        'lineas': numLineas,
        'palabras': numPalabras,
        'caracteres': numCaracteres,
        'fecha_creacion': fecha_creacion,
        'fecha_modificacion': fecha_modificacion,
        'tamaño_bytes': tamaño,
        'contenido': contenido
    }

    return resumen

def escribirResumen(rutaSalida, resumen):
    if resumen is None:
        return

    resumen_texto = (
        "=== RESUMEN DEL ARCHIVO ===\n\n"
        f"• Líneas: {resumen['lineas']}\n"
        f"• Palabras: {resumen['palabras']}\n"
        f"• Caracteres: {resumen['caracteres']}\n"
        f"• Tamaño: {resumen['tamaño_bytes']} bytes\n"
        f"• Fecha de creación: {resumen['fecha_creacion']}\n"
        f"• Última modificación: {resumen['fecha_modificacion']}\n\n"
        "=== CONTENIDO ===\n\n"
        f"{resumen['contenido']}"
    )

    try:
        with open(rutaSalida, "w", encoding="utf-8") as file:
            file.write(resumen_texto)
        print(f"Se ha generado el resumen en: {rutaSalida}")
    except Exception as e:
        print(f"Error al escribir el archivo de resumen: {e}")

def main():
     # En la variable "archivodeEntrada" se debe especificar el nombre del archivo a analizar junto con su ruta.
    archivodeEntrada = "unidad de memoria johan.pdf"  # Ejemplo: "entrada.pdf" o "entrada.docx". 
    archivodeSalida = "Resumen.txt" # Aquí se especifica el nombre del archivo de salida y la extensión en la que se desea ver.
    resumen = contarArchivo(archivodeEntrada)
    if resumen is not None:
        escribirResumen(archivodeSalida, resumen)

if __name__ == "__main__":
    main()