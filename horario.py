import json
with open('horario.json') as json_file: 
    data = json.load(json_file) 

def fimaula(dia,hora,minutos):
    dias = data[diadasemana(dia)]

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
        dias = data[diadasemana(dia)]
    
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


