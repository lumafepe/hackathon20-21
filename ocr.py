import pytesseract
from PIL import Image
import os
from mdutils.mdutils import MdUtils
from mdutils import Html
import json
from getpass import getuser

with open('config.json') as json_file:
    data = json.load(json_file)

if data["nome de autor"]=="":
    user=getuser()
else:
    user=data["nome de autor"]


def gettext(onde): # devolve texto de uma imagem de algum lado
    return pytesseract.image_to_string(Image.open(onde),lang = 'por+eng')


def inseretexto(onde,fich): # dado o diretorio da pasta adiciona ao texto.txt
    
    #texto = open(onde+"/texto.txt",'a')
    #texto.write(ocrt)
    #texto.close()
    
    #print(onde,fich)


#----------------------------------------------------------
# em teste
    if os.path.exists(onde+'/Diario_de_bordo.md'):
        # fich "ocr.pdf"
                
        if "ocr" in fich:

            ocrt = gettext(onde+'/'+fich)
            
            aula = open (onde+'/Diario_de_bordo.md','a')
            aula.write(f"![]({onde}/{fich})")
            aula.write("\n```"+ocrt+"\n```")
            aula.write("\n--------------------\n")
        else:
            aula = open (onde+'/Diario_de_bordo.md','a')
            aula.write(f"![]({onde}/{fich})")
            aula.write("\n--------------------\n")
        aula.close()

 
    else:
        aula = open (onde+'/Diario_de_bordo.md','a')
        aula.write('---\ntitle: \"Diário de bordo\"\nauthor: João Novais \ndate: March 22, 2005\ngeometry: margin=2cm\noutput: pdf_document\n---\n')
        aula.close()
        inseretexto(onde,fich)
    #pandoc -t latex -o x.pdf x.md
