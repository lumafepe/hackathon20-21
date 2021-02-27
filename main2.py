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
        #horas a que foi criado
        now = datetime.datetime.now()
        datadodia = ""
        #dia-mes-ano
        dia,mes,ano=str( now.day),str( now.month),str( now.year)
        ordem=(data["formato de datas"]).split('-')
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
        cadeira = horario.disciplinasdodia(datetime.datetime.today().weekday(),now.hour,now.minute)
        if cadeira!="NADA":
            base = f"{pathpasta}{cadeira}/{datadodia}"
            print(base)
            #cria pastas para essa aula
            os.system(f"mkdir -p {base}" )
                
            #nome da nova foto
            ficheirocriado = loader.up(pics)
            fc=ficheirocriado
            n=1
            while os.path.exists(base + '/' + fc):
                nome = fc.split('.')
                tipo=nome.pop()
                nome=""
                for i in nome:
                    nomes+=i+","
                nomes=nomes[:-1]
                fc = nomes+f"-{n}."+tipo
                n+=1
            # mover para o novo sitio
            os.system("mv " + pics + f'"{ficheirocriado}"' +" " + base +'/'+fc)
            # adicionado ficheiro de texto

            # obtem texto
            sleep(1)
                    
            ocr.inseretexto(base,ficheirocriado)
    
if __name__ == "__main__":
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
