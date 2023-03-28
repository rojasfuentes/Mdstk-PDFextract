import pytesseract
from PIL import Image

# Especifica la ruta de Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:/Users/JFROJAS/Desktop/Tesseract-OCR'

# Lee la imagen y extrae el texto
image = Image.open('C:/Users/JFROJAS/Desktop/PDF/meritm/pagina_0.jpg')
text = pytesseract.image_to_string(image)

# Imprime el texto extraído
print(text)