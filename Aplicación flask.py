from flask import Flask, render_template, request, redirect, url_for, flash
import os
import io
import PyPDF2
import docx
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'mi_clave_secreta'

ALLOWED_EXTENSIONS = {'.txt', '.pdf', '.docx'}

def allowed_file(filename):
    ext = os.path.splitext(filename)[1].lower()
    return ext in ALLOWED_EXTENSIONS

def get_file_metadata(file):
    try:
        file.seek(0, os.SEEK_END)
        tamaño = file.tell()
        file.seek(0)
        
        # Para archivos subidos, usamos la hora actual como "creación"
        fecha_creacion = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        fecha_modificacion = fecha_creacion
        return fecha_creacion, fecha_modificacion, tamaño
    except Exception as e:
        print(f"Error al obtener metadatos: {e}")
        return None, None, None

def read_file(file):
    filename = file.filename
    ext = os.path.splitext(filename)[1].lower()
    contenido = ""
    
    try:
        file.seek(0)
        data = file.read()
        file_bytes = io.BytesIO(data)
        
        if ext == ".txt":
            contenido = data.decode("utf-8")
        elif ext == ".pdf":
            pdf_reader = PyPDF2.PdfReader(file_bytes)
            for page in pdf_reader.pages:
                texto_pagina = page.extract_text()
                contenido += texto_pagina + "\n"
        elif ext == ".docx":
            documento = docx.Document(file_bytes)
            for parrafo in documento.paragraphs:
                contenido += parrafo.text + "\n"
        else:
            contenido = "Formato no soportado."
            
        # Obtener estadísticas
        lineas = contenido.splitlines()
        num_lineas = len(lineas)
        palabras = contenido.split()
        num_palabras = len(palabras)
        num_caracteres = len(contenido)
        
        # Obtener metadatos
        fecha_creacion, fecha_modificacion, tamaño = get_file_metadata(file)
        
        # Crear resumen
        resumen = {
            'content': contenido,
            'lines': num_lineas,
            'words': num_palabras,
            'chars': num_caracteres,
            'creation_date': fecha_creacion,
            'modification_date': fecha_modificacion,
            'size': tamaño,
            'filename': filename
        }
        
        return resumen
        
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return None

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
         # Se verifica que se haya enviado el archivo
        if "archivo" not in request.files:
            flash("No se encontró el archivo a subir.")
            return redirect(request.url)
            
        file = request.files["archivo"]
        if file.filename == "":
            flash("No se seleccionó ningún archivo.")
            return redirect(request.url)
            
        if file and allowed_file(file.filename):
            resumen = read_file(file)
            if resumen:
                return render_template("resultado.html", resumen=resumen)
            else:
                flash("Error al procesar el archivo.")
                return redirect(request.url)
        else:
            flash("Formato no permitido. Use .txt, .pdf o .docx.")
            return redirect(request.url)
            
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)