import os
import datetime
import json
import horario

#devolve o último ficheiro editado na diretoria dos screenshots
def up(path):
    # return os.system("ls -t /home/" + user + "/Pictures  |  head -n1")

    name_list = os.listdir(path)
    full_list = [os.path.join(path,i) for i in name_list]
    time_sorted_list = sorted(full_list, key=os.path.getmtime)

    sorted_filename_list = [ os.path.basename(i) for i in time_sorted_list]
    return sorted_filename_list[-1]#último elemtnos da lista, ficheiro mais recente

with open('config.json') as json_file: 
    data = json.load(json_file)

def aux ():
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
    return now,datadodia,cadeira