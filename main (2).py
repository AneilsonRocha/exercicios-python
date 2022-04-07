equipamentos=[]
valores=[]
seriais=[]
departamentos=[]
resposta= 'S'

while resposta == 'S':
    equipamentos.append(input("digite o equipamento :"))
    valores.append(input("informe o valor :"))
    seriais.append(input("informe o numro do serial :"))
    departamentos.append(input(" departamento :"))
    resposta=input("digite 'S' para continuar : ").upper()


for indice in range (0,len(valores)):
    print('\n Equipamentos ....',(indice+ 1))
    print('Nome.................',equipamentos[indice])
    print('valor.................',valores[indice])
    print('Serial.................',seriais[indice])
    print('Nome.................',equipamentos[indice])
    print('departamento.................',departamentos[indice])