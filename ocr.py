import pytesseract
from PIL import Image
import os
from mdutils.mdutils import MdUtils
from mdutils import Html






def gettext(onde): # devolve texto de uma imagem de algum lado
    return pytesseract.image_to_string(Image.open(onde),lang = 'por+eng')


def inseretexto(onde,fich): # dado o diretorio da pasta adiciona ao texto.txt
    
    #texto = open(onde+"/texto.txt",'a')
    #texto.write(ocrt)
    #texto.close()
    
    #print(onde,fich)


#----------------------------------------------------------
# em teste
    if os.path.exists(onde+'/Resumo_da_aula.md'):
        # fich "ocr.pdf"
                
        if "ocr" in fich:

            ocrt = gettext(onde+'/'+fich)
            
            aula = open (onde+'/Resumo_da_aula.md','a')
            aula.write("![]("+fich+")")
            aula.write("\n```"+ocrt+"\n```")
            aula.write("\n----------------------------------------------------------------------------------\n")
        else:
            aula = open (onde+'/Resumo_da_aula.md','a')
            aula.write("![]("+fich+")")
            aula.write("\n----------------------------------------------------------------------------------\n")
            print("imagem")
    else :
        if "ocr" in fich:

            ocrt = gettext(onde+'/'+fich)
            
            aula = open (onde+'/Resumo_da_aula.md','w')
            aula.write(ocrt+"\n\n----------------------------------------------------------------------------------\n")
        else:
            aula = open (onde+'/Resumo_da_aula.md','w')
            aula.write("![]("+fich+")\n\n----------------------------------------------------------------------------------\n")
            print("imagem")
    aula.close()
    
    # ![](fich) 
    #pandoc -t latex -o x.pdf x.md
