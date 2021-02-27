import json

semana=""
fim=""
horario = {}
print("escreva fim para acabar")
while semana!="fim":
    semana = input("dia da semana: ")
    semana=semana.lower()
    dia = {}
    if semana!="fim":
        a=""
        print("escreva fim em cadeira para acabar")
        while a!="FIM":
            a = input('cadeira: ')
            a = a.upper()
            aula = {}
            if a!= 'FIM':
                b = input('hora:minutos de inicio: ')
                c = input('hora:minutos de fim: ')
                if a!="FIM":
                    aula["hora inicial"] = b
                    aula["hora final"] = c
                    dia[a] = aula
                    horario[semana] = dia
                else:
                    horario[semana] = dia
            else:
                horario[semana] = dia

json_object = json.dumps(horario, indent = 4)

with open("horario.json", "w") as outfile: 
    outfile.write(json_object) 

print("horario criado")