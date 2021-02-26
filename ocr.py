import pytesseract
from PIL import Image


def gettext(onde): # devolve texto de uma imagem de algum lado
    return pytesseract.image_to_string(Image.open(onde),lang = 'por+eng')



def inseretexto(onde): # dado o diretorio da pasta adiciona ao texto.txt
    a = onde.split('/') 
    b = a.pop()
    a = '/'.join(a)+'/'
    texto = open(a+"texto.txt",'a')
    texto.write(gettext(onde))
    texto.close()
