import json

semana=""
fim=""
horario = {}
while semana!="fim":
    print("Escreva fim para acabar")
    semana = input("Introduza o dia da semana: ")
    semana=semana.lower()
    print('\n')
    dia = {}
    if semana!="fim":
        a=""
        while a!="FIM":
            print("Escreva fim em cadeira para acabar")
            a = input('Nome da cadeira : ')
            a = a.upper()
            aula = {}
            if a!= 'FIM':
                b = input('Escreva a hora inicial com o seguinte formato  hora:minutos : ')
                c = input('Escreva a hora final com o seguinte formato  hora:minutos : ')
                if a!="FIM":
                    aula["hora inicial"] = b
                    aula["hora final"] = c
                    dia[a] = aula
                    horario[semana] = dia
                    print('\n')
                else:
                    horario[semana] = dia
                    print('\n')
            else:
                horario[semana] = dia
                print('\n')

json_object = json.dumps(horario, indent = 4)

with open("horario.json", "w") as outfile: 
    outfile.write(json_object) 

print("Horário criado")