

#vai ao horario verificar que aula está a ter a uma dada hora num dado dia
def faztudo(dia,hora,minuto,horario):
    d1= diadasemana(dia)
    d = separa(d1,horario)
    print(d1,horario)
    return (removedia(d,hora,minuto))

#Vai ao horário e retira de lá a string que corresponde ao dia pretendido
def separa (dia,lista):
    resultado = ''
    for x in lista:
        if dia in x:
            resultado = x[(len(dia)+3):]#FIXME
            resultado = resultado.split(',') 
            break
    return resultado

#Vai ao horario para um dado dia e verifica a aula que esta a ter a uma dada hora
def removedia(dia,hora,minutos):
    #if (dia == []) or (dia == [""]) or (dia[0].isspace()):
    if (dia == []) or (dia == [""]):
        return 'NADA'
    else:
        for i in dia:
            i = i[1:(len(i) - 1)]
            cadeira,hi,hf=i.split()
            hih,him=hi.split(':')
            hfh,hfm=hf.split(':')
            hih,him,hfh,hfm = map(int,[hih,him,hfh,hfm])
            hi = hih*60 + him
            hf = hfh*60 + hfm
            ha = hora*60 + minutos
            if (ha>=hi) and (ha<=hf):
                return cadeira
    return 'NADA'

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

