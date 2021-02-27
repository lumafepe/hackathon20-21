
def concat(l):
    a=""
    for i in l:
        if l.index(i) == (len(i)-1):
            a+=i
        else:
            a+=i+"\n"
    return a
#serve para editar os elementos
def editarelems(diaAEditar):
    a = []
    a = diaAEditar.split(',')
    b=a.pop(0)
    dia,e,f,g,h = b.split() # separa a 1 por partes
    a.insert(0,f+" "+g+" "+h) # adiciona a primeira
    print(concat(a))   # q cadeiras existem
    ioIn=input("Cadeira a editar(1-{}) : ".format(len(a)))#numero da cadeira a editar
    a.pop(int(ioIn)-1)#qual a remover para adicionar uma nova
    cad = input('nova cadeira: ')
    cad = cad.upper()
    cad = cad + " " + input('nova hora:minutos de inicio : ')
    cad = cad + " " +input('nova hora:minutos de fim : ')
    cad="("+cad+")"
    a.append(cad)#junta a nova cadeira
    b=""
    for i in a:
        b+=i+","
    return dia+" ; "+b[:-1]

a=open("Horarios/horario.txt","r")
b = a.read()
a.close()
print(b)
oqfazer=input("o que quer fazer ELIMINAR TUDO/EDITAR DIA/ADICIONAR DIA: ")
if oqfazer=="ELIMINAR TUDO":
    a=open("Horarios/horario.txt","w")
    a.write("")
    a.close()
    print("removido")
elif oqfazer=="EDITAR DIA":
    ioIn = input("linha a editar(1-{}): ".format(len(b.split('\n'))-1))
    assert(ioIn.isdigit())
    b=b.split('\n')
    diaAEditar=b.pop(int(ioIn)-1)
    oqfazer=input("o que quer fazer ELIMINAR/EDITAR ELEMENTOS/ADICIONAR: ")
    if oqfazer=="ELIMINAR":
        diaAEditar=""
    elif oqfazer=="EDITAR ELEMENTOS":
        diaAEditar=editarelems(diaAEditar)
    else:
        cad = input('cadeira: ')
        cad = cad.upper()
        cad = cad + " " + input('hora:minutos de inicio: ')
        cad = cad + " " +input('hora:minutos de fim: ')
        cad=",("+cad+")"
        diaAEditar=diaAEditar+cad
    b.insert(int(ioIn)-1, diaAEditar)
    a=open("Horarios/horario.txt","w")
    a.write(concat(b))
    a.close()
    print("editado")
else:
    semana = input("dia da semana: ")
    semana=semana.lower()
    fim=semana +" ; "
    a=""
    print("escreva fim em cadeira para acabar")
    while a!="FIM":
        a = input('cadeira: ')
        a = a.upper()
        if a!="FIM":
            be = input('hora:minutos de inicio: ')
            c = input('hora:minutos de fim: ')
            fim+="("+a+" "+be+" "+c+"),"
        else:
            fim=(fim[:-1]+"\n")
    a=open("Horarios/horario.txt","w")
    a.write(b+fim)
    a.close()
    print("adicionado")
    
