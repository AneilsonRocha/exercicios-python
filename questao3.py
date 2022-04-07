def somar(elementos):
    somatorio = 0
    for i in elementos:
        somatorio += i
    return somatorio

def somaTrios(lista):
    listaSomada = []
    for e in lista:
        listaSomada.append(somar(e))
    return listaSomada

# Testando a função
print(somaTrios([[1,2,3],[3,4,5],[5,6,7],[7,8,9],[9,10,11]]))