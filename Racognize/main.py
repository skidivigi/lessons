import pytesseract
from PIL import Image

img = input('Pls enter name file(FORMAT: text.jpg):')
def racognize(img):

    #for Windows users
    pytesseract.pytesseract.tesseract_cmd = r'D:\Frameworks\Tesseract\tesseract.exe'

    img = Image.open(img)
    file_name = img.filename
    file_name = file_name.split('.')[0]

    custom_config = r'--oem 3 --psm 7'

    text = pytesseract.image_to_string(img, config=custom_config)

    with open(f'{file_name}.txt', 'w') as file:
        file.write(text)
    print(text)

def main(img):
    racognize(img)

if __name__ == '__main__':
    main(img)