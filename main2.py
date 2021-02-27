import getpass
import sys
import time
import os
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import loader
import datetime
import horario
import ocr
import json


#user
user = getpass.getuser()

# defenir diretorio das imagens
pics = f"/home/{user}/Pictures/"  

pics = f"/home/{user}/Pictures/"
#diretorio para guardar as aulas
pathpasta = f"/home/{user}/Documents/aulas/"

#cria a pasta da aulas se nao existir
os.system("mkdir -p " + pathpasta)

#horario em string
#a = open('Horarios/horario.txt', 'r')
#hor = (a.read()).split('\n') # horarios
#a.close()

#event logger
class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        #horas a que foi criado
        now = datetime.datetime.now()
                
        a,b,c=str( now.day),str( now.month),str( now.year)
        #que aula o alno esta a ter
        #cadeira = horario.faztudo(datetime.datetime.today().weekday(),now.hour,now.minute,hor)
        cadeira = horario.disciplinasdodia(datetime.datetime.today().weekday(),now.hour,now.minute)

        base = f"{pathpasta}{cadeira}/{a}-{b}-{c}"
        print(base)
        #cria pastas para essa aula
        os.system(f"mkdir -p {base}" )
                
        #nome da nova foto
        ficheirocriado = loader.up(pics)
        fc=ficheirocriado
        n=1
        while os.path.exists(base + '/' + fc):
            nome,tipo = fc.split('.')
            fc = nome+f"-v{n}."+tipo
            n+=1
        # mover para o novo sitio
        os.system("mv " + pics + f'"{ficheirocriado}"' +" " + base +'/'+fc)
        # adicionado ficheiro de texto

        # obtem texto
        time.sleep(1)
                
        ocr.inseretexto(base,ficheirocriado)
    
if __name__ == "__main__":
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path=pics, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
