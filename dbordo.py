#!/usr/bin/env python3
from getpass import getuser
from time import sleep
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import datetime
import json
import subprocess #
import signal#
import sys    # 
import pytesseract
from PIL import Image
from mdutils.mdutils import MdUtils
from mdutils import Html
import getopt

#FAZER DEPOISSS RECEBER ARGUMENTOS
#PERGUNTAR PELO COMPRIMENTO
#pri = sys.argv[1]
oqueestaaestudar = sys.argv

opcs,args = (oqueestaaestudar[1:],"h")
if "-h" in opcs:
    print("""
    ********************* Diário de Bordo ********************
            
            configurar paths,autor  : /home/dbordo/config.json
            configurar horarios     : /home/dbordo/horario.json
            
            Se no nome do fichiero tiver expressão regular 'ocr'
            vai ser adicionado a imagem e o texto

            """)
    quit()

if "-c" in opcs:
    os.system("dbordo_creator")
    quit()
#user
user = getuser()


#configs
with open('/home/dbordo/config.json') as json_file: 
    data = json.load(json_file)
# defenir diretorio default de entrada
if data["onde As Imagens Vao Parar"]=="":
    pics = f"/home/{user}/Pictures/"
else:
    pics = data["onde As Imagens Vao Parar"] 
#diretorio default para guardar
if data["onde colocar as imagens"]=="":
    pathpasta = f"/home/{user}/Documents/" 
else:
    pathpasta = data["onde colocar as imagens"]
pathpasta+=data["nome da pasta onde guardar"]

#cria a pasta da aulas se nao existir
os.system("mkdir -p " + pathpasta)


#event logger
class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        now,datadodia,cadeira = aux()

        #if oqueestaaestudar!=data["nome base para usar o horario"]:
         #   cadeira = oqueestaaestudar

        if len(oqueestaaestudar) > 1:
            cadeira = oqueestaaestudar[1]



        if cadeira!="NADA":
            base = f"{pathpasta}{cadeira}/{datadodia}"
            #print(base)
            #cria pastas para essa aula
            os.system(f"mkdir -p {base}" )

            #nome da nova foto
            ficheirocriado = up(pics)
            fc=ficheirocriado
            n=1
            nomes = ""
            while os.path.exists(base + '/' + fc):
                nome = fc.split('.')
                tipo=nome.pop()
                nome1 = nome
                nome=""
                for i in nome:
                    nomes+=i+"."
                nomes=nomes[:-1]
                fc = nome1+f"-{n}."+tipo
                n+=1
            if len(oqueestaaestudar)==1:#data["nome base para usar o horario"]:
                signal.alarm((fimaula(datetime.datetime.today().weekday(),now.hour,now.minute))*60 - ((now.hour*60+now.minute)*60+now.second))




            # mover para o novo sitio
            #os.system("mv " + pics + f'"{ficheirocriado}"' +" " + base +'/'+fc)
            sleep(1)
            pathinput  = os.path.join( pics,ficheirocriado)
            pathoutput = os.path.join( base,fc)

            subprocess.run(["mv",pathinput,pathoutput])
            # adicionado ficheiro de texto

            # obtem texto
            sleep(1)

            inseretexto(base,fc)


def handler(sig, frame):
    print(sig)
    now,datadodia,cadeira = aux()

    if len( oqueestaaestudar)>1:#data["nome base para usar o horario"]:
        cadeira = oqueestaaestudar

    if cadeira == 'NADA':
        print("nao tens nenhuma cadeira")
    else:

        #print('a passar para pdf/html', sig)
        dis = up(f"{pathpasta}")
        dia = up(f"{pathpasta}{dis}")

        #print(f"{pathpasta}{dis}/{dia}/")
        os.system(f"pandoc -t latex -o {pathpasta}{dis}/{dia}/dbordo.pdf {pathpasta}{dis}/{dia}/Diario_de_bordo.md")
        os.system(f"pandoc {pathpasta}{dis}/{dia}/Diario_de_bordo.md -V fontsize=12pt -V geometry:margin=1in -o {pathpasta}{dis}/{dia}/dbordo.html")
    sys.exit(0)
    
def handler2(sig, frame):
    now,datadodia,cadeira = loader.aux()
    if len(oqueestaaestudar) >1: #!= data["nome base para usar o horario"]:
        cadeira = oqueestaaestudar[1]
    if cadeira == 'NADA':
        print("nao tens nenhuma cadeira")
    else:

        print('a passar para pdf/html', sig)
        dis = loader.up(f"{pathpasta}")
        dia = loader.up(f"{pathpasta}{dis}")

        print(f"{pathpasta}{dis}/{dia}/")
        os.system(f"pandoc -t latex -o {pathpasta}{dis}/{dia}/dbordo.pdf {pathpasta}{dis}/{dia}/Diario_de_bordo.md")
        os.system(f"pandoc {pathpasta}{dis}/{dia}/Diario_de_bordo.md -V fontsize=12pt -V geometry:margin=1in -o {pathpasta}{dis}/{dia}/dbordo.html")


#devolve o último ficheiro editado na diretoria dos screenshots
def up(path):
    # return os.system("ls -t /home/" + user + "/Pictures  |  head -n1")

    name_list = os.listdir(path)
    full_list = [os.path.join(path,i) for i in name_list]
    time_sorted_list = sorted(full_list, key=os.path.getmtime)

    sorted_filename_list = [ os.path.basename(i) for i in time_sorted_list]
    return sorted_filename_list[-1]#último elemtnos da lista, ficheiro mais recente

with open('/home/dbordo/config.json') as json_file: 
    data3 = json.load(json_file)

def aux ():
    #horas a que foi criado
    now = datetime.datetime.now()
    datadodia = ""
    #dia-mes-ano
    dia,mes,ano=str( now.day),str( now.month),str( now.year)
    ordem=(data3["formato de datas"]).split('-')
    for i in ordem:
        if "ano"==i:
            datadodia+=ano+"-"
        elif "mes"==i:
            datadodia+=mes+"-"
        else:
            datadodia+=dia+"-"
    datadodia=datadodia[:-1]
    #que aula o alno esta a ter
    #cadeira = horario.faztudo(datetime.datetime.today().weekday(),now.hour,now.minute,hor)
    cadeira = disciplinasdodia(datetime.datetime.today().weekday(),now.hour,now.minute)
    return now,datadodia,cadeira








with open('/home/dbordo/horario.json') as json_file: 
    data4 = json.load(json_file) 

def fimaula(dia,hora,minutos):
    dias = data4[diadasemana(dia)]

    for k in dias:
        horas = dias[k]

        for i in horas:
            a = i['hora final']
            ah,am = a.split(':')
            a=int(ah)*60+int(am)
            b = i['hora inicial']
            bh,bm = b.split(':')
            b=int(bh)*60+int(bm)
            if b<=hora*60+minutos<=a:
                return a
                break


def disciplinasdodia(dia,hora,minutos):
    
    try:
        dias = data4[diadasemana(dia)]
    
        for k in dias:
            horas = dias[k]

            for i in horas:
                a = i['hora final']
                ah,am = a.split(':')
                a=int(ah)*60+int(am)
                b = i['hora inicial']
                bh,bm = b.split(':')
                b=int(bh)*60+int(bm)
                if b<=hora*60+minutos<=a:
                    return str(k)
                    break
                    
        #se no ciclo for nao encontrar nenhuma disciplina é porque aquela hora nao tem nada
        return 'NADA'
    except:
        return "NADA"




def diadasemana (num):
    if num == 0:
        return 'segunda'
    elif num == 1:
        return 'terca'
    elif num == 2:
        return 'quarta'
    elif num == 3:
        return 'quinta'
    elif num == 4:
        return 'sexta'
    elif num == 5:
        return 'sabado'
    else:
        return 'domingo'





with open('/home/dbordo/config.json') as json_file:
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


if __name__ == "__main__":
    
    signal.signal(signal.SIGALRM, handler2)
    #signal.alarm(5)# segundos

    signal.signal(signal.SIGINT, handler)
    #signal.alarm(0)
    
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path=pics, recursive=False)
    observer.start()

    try:
        while True:
            sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
