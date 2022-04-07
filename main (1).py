conjuntos_num=[0,-1,-2,-3, 4,5,-6,-7-8,-9,10]

def retiraNegativos(conjuntos_num) :
    retirar=lambda n: n >= 0 
    resultado=list(filter(retirar,conjuntos_num))
    print(resultado)

print(conjuntos_num,'\n')
print('RETIRANDO NUMEROS NEGATIVOS.......\n')

retiraNegativos(conjuntos_num)

    
