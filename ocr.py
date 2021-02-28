import datetime
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

    if os.path.exists(onde+'/Diario_de_bordo.md'):
        # fich "ocr.pdf"
                
        if "ocr" in fich:

            ocrt = gettext(onde+'/'+fich)
            
            aula = open (onde+'/Diario_de_bordo.md','a')
            aula.write(f"\n![]({onde}/{fich})\n")
            aula.write("\n```\n"+ocrt+"\n```\n")
            #aula.write("\n---\n")
        else:
            aula = open (onde+'/Diario_de_bordo.md','a')
            aula.write(f"\n![]({onde}/{fich})\n")
            #aula.write("\n---\n")
        aula.close()

 
    else:
        aula = open (onde+'/Diario_de_bordo.md','a')
        x = datetime.datetime.now()
        ano = x.year
        mes = x.strftime("%B")
        dia = x.day
        aula.write(f'---\ntitle: \"Diário de bordo\"\nauthor: {user} \ndate: {mes} {dia}, {ano}\ngeometry: margin=2cm\noutput: pdf_document\nfontsize: 100pt\n---\n')
        aula.close()
        inseretexto(onde,fich)
    #pandoc -t latex -o x.pdf x.md
