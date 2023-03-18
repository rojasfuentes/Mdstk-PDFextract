import PyPDF2
import re
from openpyxl import Workbook

# Abrir el archivo PDF en modo lectura binaria
with open('C:/Users/JFROJAS/Desktop/PDF/test/PDF/3123 FRAGUA GUADALAJARA.pdf', 'rb') as pdf_file:

    # Crear un objeto PDFFileReader
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Obtener el número de páginas del archivo PDF
    num_pages = len(pdf_reader.pages)

    # Crear una lista vacía para almacenar la información de cada página
    pages_info = []

    # Definir la expresión regular para buscar el texto después de la palabra "Cantidad"
    regex = re.compile(r'de vencimiento Cantidad\s+([^\n]+)')

    # Recorrer todas las páginas del archivo PDF
    for page_number in range(num_pages):
        # Obtener la página actual del archivo PDF
        page = pdf_reader.pages[page_number]

        # Obtener el contenido de la página actual
        page_content = page.extract_text()

        # Buscar el texto después de la palabra "Cantidad" en el contenido de la página actual
        matches = regex.findall(page_content)

        if matches:
            # Si se encontró una coincidencia, obtener la línea siguiente
            next_line_regex = re.compile(r'Cantidad\s+[^\n]+\n(.+)')
            next_line_matches = next_line_regex.findall(page_content)

            if next_line_matches:
                next_lines = next_line_matches[0]
            else:
                next_lines = ""

            # Agregar la información a la lista de información de cada página
            for match in matches:
                pages_info.append(match + " " + next_lines)

    # Crear un nuevo archivo de Excel y seleccionar la hoja de trabajo
    workbook = Workbook()
    sheet = workbook.active

    # Escribir los encabezados de las columnas
    sheet['A1'] = "Lote"
    sheet['B1'] = "Fecha Venc"
    sheet['C1'] = "Cantidad"

    # Escribir los resultados en las filas correspondientes
    for row, info in enumerate(pages_info, start=2):
        data = info.split()
        sheet.cell(row=row, column=1, value=data[0])
        sheet.cell(row=row, column=2, value=data[3])
        sheet.cell(row=row, column=3, value=data[4])

    # Guardar el archivo de Excel
    workbook.save("output.xlsx")
