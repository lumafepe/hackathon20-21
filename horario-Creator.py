a=open("Horarios/horario.txt","w")
semana=""
fim=""
print("escreva fim para acabar")
while semana!="fim":
    semana = input("dia da semana: ")
    semana=semana.lower()
    if semana!="fim":
        fim+=semana +" ; "
        a=""
        print("escreva fim em cadeira para acabar")
        while a!="FIM":
            a = input('cadeira: ')
            a = a.upper()
            b = input('hora:minutos de inicio: ')
            c = input('hora:minutos de fim: ')
            if a!="FIM":
                fim+="("+a+" "+b+" "+c+"),"
            else:
                fim=(fim[:-1]+"\n")
a.write(fim)
a.close()
print("horario criado")