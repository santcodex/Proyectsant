from flask import Flask, render_template, request, redirect, url_for, flash
import os
import io
import PyPDF2
import docx

app = Flask(__name__)
app.secret_key = 'mi_clave_secreta'  

# Se definen las extensiones permitidas
ALLOWED_EXTENSIONS = {'.txt', '.pdf', '.docx'}

def allowed_file(filename):
    
    ext = os.path.splitext(filename)[1].lower()
    return ext in ALLOWED_EXTENSIONS

def read_file(file):
   
    filename = file.filename
    ext = os.path.splitext(filename)[1].lower()
    contenido = ""
    try:
        
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
    except Exception as e:
        contenido = f"Error al leer el archivo: {e}"
    return contenido

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
            contenido = read_file(file)
            return render_template("resultado.html", content=contenido)
        else:
            flash("Formato de archivo no permitido. Utiliza un archivo .txt, .pdf o .docx.")
            return redirect(request.url)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
