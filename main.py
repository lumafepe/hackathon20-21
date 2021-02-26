import getpass
import sys
import time
import os
import logging
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler 
import loader
import datetime
import horario
import ocr

#user
user = getpass.getuser()

# defenir diretorio das imagens
pics = f"/home/{user}/Pictures/"  

pics = f"/home/{user}/Pictures/"
#diretorio para guardar as aulas
pathpasta = "/home/{}/Documents/aulas/".format(user)

#cria a pasta da aulas se nao existir
os.system("mkdir -p " + pathpasta)

#horario em string
a = open('Horarios/horario1.txt', 'r')
hor = (a.read()).split('\n') # horarios
a.close()

#event logger
if __name__ == "__main__": 
    my_event_handler = PatternMatchingEventHandler("*","", True, True)
    #novo ficheiro criado
    def on_created(event):

        #horas a que foi criado
        now = datetime.datetime.now()
        #que aula o alno esta a ter
        cadeira = horario.faztudo(datetime.datetime.today().weekday(),now.hour,now.minute,hor)
        #cria pastas para essa aula
        a,b,c=str( now.day),str( now.month),str( now.year)
        os.system("mkdir -p "+ pathpasta + cadeira + '/' + a+'-'+b+'-'+c )
        #nome da nova foto
        ficheirocriado = loader.up(pics)
        # mover para o novo sitio
        os.system("mv " + pics + f'"{ficheirocriado}"' +" " + pathpasta + cadeira + '/' + a+'-'+b+'-'+c)
        #adicionado ficheiro de texto
        os.system("touch " + pathpasta + cadeira + '/' + a+'-'+b+'-'+c + "/texto.txt")
        #obtem texto
        time.sleep(1)
        ocr.inseretexto(pathpasta + cadeira + '/' + a+'-'+b+'-'+c + "/" + f'{ficheirocriado}')



    my_event_handler.on_created = on_created

    go_recursively = True
    my_observer = Observer()
    my_observer.schedule(my_event_handler, pics, recursive=go_recursively)

    my_observer.start()
    try:
        while True:
            time.sleep(5)
    except:
        my_observer.stop()
    my_observer.join()
