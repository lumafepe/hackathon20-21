#!/usr/bin/env python3
from getpass import getuser
from time import sleep
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import loader
import datetime
import horario
import ocr
import json
import subprocess 
import signal    
import sys    
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
            
            opções: -h --help
                    -c --create   , ajuda a inserir horários

            Se no nome do fichiero tiver expressão regular 'ocr'
            vai ser adicionado a imagem e o texto

            """)
    quit()

if "-c" in opcs:
    os.system("dbordo_creator")
    quit()
oqueestaaestudar = sys.argv



#user
user = getuser()


#configs
with open('config.json') as json_file: 
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
        now,datadodia,cadeira = loader.aux()
        
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
            ficheirocriado = loader.up(pics)
            fc=ficheirocriado
            n=1
            nomes = ""
            while os.path.exists(base + '/' + fc):
                nome = fc.split('.')
                tipo=nome.pop()
                nome1=nome
                nome=""
                for i in nome:
                    nomes+=i+"."
                nomes=nomes[:-1]
                fc = nome1+f"-{n}."+tipo
                n+=1
            if len(oqueestaaestudar)==1:#data["nome base para usar o horario"]:
                signal.alarm((horario.fimaula(datetime.datetime.today().weekday(),now.hour,now.minute))*60 - ((now.hour*60+now.minute)*60+now.second))
            



            # mover para o novo sitio
            #os.system("mv " + pics + f'"{ficheirocriado}"' +" " + base +'/'+fc)
            sleep(1)
            pathinput  = os.path.join( pics,ficheirocriado)
            pathoutput = os.path.join( base,fc)

            subprocess.run(["mv",pathinput,pathoutput])
            # adicionado ficheiro de texto

            # obtem texto
            sleep(1)
                    
            ocr.inseretexto(base,fc)
    


def handler(sig, frame):
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
