def maiorDaLista(numeros):
    maior = numeros[0]
    for i in range(1,len(numeros)):
        if numeros[i] > maior:
            maior = numeros[i]
    return maior

def numDeOcorrencias(n, numeros):
    ocorrencias = []
    for i, e in enumerate(numeros):
        if e == n:
            ocorrencias.append([e,i])
    return ocorrencias

lista = []

num = -1
while num != 0:
    num = int(input("Digite um número: "))
    lista.append(num)
del lista[-1] #tira o zero

maiorNumero = maiorDaLista(lista)
ocorrencias = numDeOcorrencias(maiorNumero, lista) 
print("O maior número lido foi o ", maiorNumero)
print("O %d apareceu %d vezes." % (maiorNumero, len(ocorrencias)))
print("O %d apareceu nas posições: " % maiorNumero, end="")
for elem in ocorrencias:
    print(elem[1]+1, end = ", ") 
