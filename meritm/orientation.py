import os
from PyPDF2 import PdfReader, PdfWriter

# Ruta a la carpeta que contiene los archivos PDF
input_folder = 'C:/Users/JFROJAS/Desktop/PDF/meritm/PDF'

# Ruta a la carpeta donde se guardarán los archivos girados
output_folder = 'C:/Users/JFROJAS/Desktop/PDF/meritm/PDF'

# Función para verificar la orientación de una página
def is_vertical(page):
    #return page['/Rotate'] in [90, 270] 
    return page['/Rotate'] in [0, 180]

# Función para rotar una página
def rotate_page(page):
    page.rotate(-90)
    return page

# Loop a través de todos los archivos PDF en la carpeta de entrada
for filename in os.listdir(input_folder):
    if filename.endswith('.pdf'):
        print(f'Procesando archivo {filename}...')

        # Abrir el archivo PDF y crear un objeto PdfFileReader
        input_path = os.path.join(input_folder, filename)
        pdf_reader = PdfReader(open(input_path, 'rb'))

        # Crear un objeto PdfFileWriter para escribir el archivo de salida
        pdf_writer = PdfWriter()

        # Loop a través de todas las páginas del archivo PDF
        for page in pdf_reader.pages:
            if is_vertical(page):
                # Si la página está en orientación vertical, girarla
                page = rotate_page(page)

            # Agregar la página al objeto PdfFileWriter
            pdf_writer.add_page(page)

        # Guardar el archivo de salida
        output_path = os.path.join(output_folder, filename)
        with open(output_path, 'wb') as output_file:
            pdf_writer.write(output_file)

print('Proceso completo.')
