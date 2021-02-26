a = open('/home/tbag/hack/Horarios/horario2.txt', 'r')

b = a.read().split('\n')

#Vai ao horário e retira de lá a string que corresponde ao dia pretendido
def separa (dia,lista):
    resultado = ''
    while resultado == '':
        for x in lista:
            if dia in x:
                resultado = x[(len(dia)+3):]
                resultado = resultado.split(',') 
    return resultado

#Vai ao horario para um dado dia e verifica a aula que esta a ter a uma dada hora
def removedia(dia,hora,minutos):
    if (dia == []) or (dia == [""]) or (dia.isspace() == True):
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

#vai ao horario verificar que aula está a ter a uma dada hora num dado dia
def faztudo(dia,hora,minuto,horario):
    d = separa(dia,horario)
    return (removedia(d,hora,minuto))

a.close
