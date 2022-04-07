lista=[2,5,4,8,1]
def geralista(lista):
    par=list(filter(lambda p: p % 2 == 0,lista))
    impar=list(filter(lambda i: i % 2 != 0,lista))
    nvlista=list(map(lambda m: m * 2,par))
    lista_impar=list(map(lambda a: a - 1,impar))
    nvlista = nvlista + lista_impar
    print(nvlista)


geralista(lista)