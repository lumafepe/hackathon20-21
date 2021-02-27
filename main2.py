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

"""
#testes para ja!
a=open("closeapp.dat",'w')
a.write("0")
a.close()
a=open("off.dat",'w')
a.write("1")
a.close()
os.system("python3 switch.py")
"""
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
a = open('Horarios/horario.txt', 'r')
hor = (a.read()).split('\n') # horarios
a.close()

#event logger
    
my_event_handler = PatternMatchingEventHandler("*","", True, True)
#novo ficheiro criado
def on_created(event):

    #horas a que foi criado
    now = datetime.datetime.now()
    
    a,b,c=str( now.day),str( now.month),str( now.year)
    #que aula o alno esta a ter
    cadeira = horario.faztudo(datetime.datetime.today().weekday(),now.hour,now.minute,hor)
    
    base = f"{pathpasta}{cadeira}/{a}-{b}-{b}"
    print(base)
    #cria pastas para essa aula
    os.system(f"mkdir -p {base}" )
    
    #nome da nova foto
    ficheirocriado = loader.up(pics)
    nome = len(os.listdir(base))
    if nome>1:
        nome=str(nome)
    else:
        nome = str(nome+1)
    # mover para o novo sitio
    os.system("mv " + pics + f'"{ficheirocriado}"' +" " + base)
    # adicionado ficheiro de texto
    os.system(f"touch {base}/texto.txt")

    # obtem texto
    time.sleep(1)
    
   
    ocr.inseretexto(base,ficheirocriado)




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
