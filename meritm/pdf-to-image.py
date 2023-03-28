import os
from pdf2image import convert_from_path

# Agrega la ruta de Poppler a la variable de entorno PATH en tiempo de ejecución
poppler_path = r'C:/Users/JFROJAS/Downloads/poppler-0.68.0_x86/poppler-0.68.0/bin'
os.environ['PATH'] += os.pathsep + poppler_path

# Indica la ruta del archivo PDF
pdf_path = 'C:/Users/JFROJAS/Desktop/PDF/meritm/PDF/457954.pdf'

# Convierte todas las páginas del PDF en imágenes
pages = convert_from_path(pdf_path)

# Guarda cada página como una imagen separada
for i, page in enumerate(pages):
    page.save(f'pagina_{i}.jpg', 'JPEG')

