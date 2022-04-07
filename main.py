lista=[1,4,5,6,11,15,22,67]

rst=list(filter(lambda a:a>10,lista))
print(rst)

menorQue10 = lambda n: n < 10
maiorQue10 = lambda n: n > 10

def main():
    lista = [5, 16, 4, 2, 21, 47, 1, 14]     
    resultado = list( filter(maiorQue10, lista) )    
    print(resultado)

#Invocando a função main()
main()

numeros = [3, 1, 5, 6, 2, 5, 6, 5, 4, 2]

resultado = len(list(filter(lambda n: n == 5, numeros)))

print(f"O 5 foi lançado {resultado} vezes")
 
numeros = [3, 1, 5, 6, 2, 5, 6, 5, 4, 2]

resultado = list( map(lambda n: n * 2, numeros) )

print( resultado )