from PIL import Image
from PyPDF2 import PdfReader, PdfWriter
from io import BytesIO
import os


def main():
    # Carpeta donde están las imágenes
    input_folder = 'C:/Users/JFROJAS/Desktop/PDF/test/IMAGES'

    # Imagen de carátula a buscar
    cover_image = Image.open(
        'C:/Users/JFROJAS/Desktop/PDF/test/SRC/caratula.png')

    # Directorio de salida para los PDFs separados
    output_folder = 'C:/Users/JFROJAS/Desktop/PDF/test/Results'

    # Contador para el nombre de los archivos PDF
    pdf_counter = 1

    # r el primer PDF
    current_pdf = None

    # Recorrer todas las imágenes en la carpeta
    for filename in os.listdir(input_folder):
        if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
            # Cargar la imagen
            image_path = os.path.join(input_folder, filename)
            image = Image.open(image_path)

            # Agregar la imagen al PDF actual
            img_temp = BytesIO()
            image.convert('RGB').save(img_temp, format='pdf')

            pdf_page = PdfReader(img_temp).pages[0]

            # Comparar la imagen con la carátula
            if image.histogram() == cover_image.histogram():
                # Guardar el PDF actual
                if current_pdf:
                    with open(os.path.join(output_folder, f'reporte_{pdf_counter}.pdf'), 'wb') as f:
                        current_pdf.write(f)
                        pdf_counter += 1

                # Crear un nuevo PDF y agregar la portada
                current_pdf = PdfWriter()
                current_pdf.add_page(pdf_page)

            else:
                # Agregar la imagen al PDF actual
                current_pdf.add_page(pdf_page)

    # Guardar el último PDF
    if current_pdf:
        with open(os.path.join(output_folder, f'reporte_{pdf_counter}.pdf'), 'wb') as f:
            current_pdf.write(f)


if __name__ == '__main__':
    main()
