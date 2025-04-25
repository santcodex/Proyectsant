import os
import PyPDF2
import docx

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

def contarArchivo(rutadeArchivo):
    
    contenido = leerArchivo(rutadeArchivo)
    if contenido is None:
        return None, None, None

    # Contar líneas
    lineas = contenido.splitlines()
    numLineas = len(lineas)

    # Contar palabras (split separa por espacios, saltos de línea, etc.)
    palabras = contenido.split()
    numPalabras = len(palabras)

    # Contar caracteres (incluyendo espacios y saltos de línea)
    numCaracteres = len(contenido)

    return numLineas, numPalabras, numCaracteres

def escribirResumen(rutaSalida, numLineas, numPalabras, numCaracteres):
   
    resumen = (
        "Resumen del archivo:\n\n"
        f"Número de líneas: {numLineas}\n"
        f"Número de palabras: {numPalabras}\n"
        f"Número de caracteres: {numCaracteres}\n"
    )

    try:
        with open(rutaSalida, "w", encoding="utf-8") as file:
            file.write(resumen)
        print(f"Se ha generado el resumen en: {rutaSalida}")
    except Exception as e:
        print(f"Error al escribir el archivo de resumen: {e}")

def main():
    # En la variable "archivodeEntrada" se debe especificar el nombre del archivo a analizar junto con su ruta.
    archivodeEntrada = "unidad de memoria johan.pdf"  # Ejemplo: "entrada.pdf" o "entrada.docx". 
    archivodeSalida = "Resumen.txt" # Aquí se especifica el nombre del archivo de salida y la extensión en la que se desea ver.

    numLineas, numPalabras, numCaracteres = contarArchivo(archivodeEntrada)
    if numLineas is not None:
        escribirResumen(archivodeSalida, numLineas, numPalabras, numCaracteres)

if __name__ == "__main__":
    main()
