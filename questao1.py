nome = input("Digite seu nome: ")

dec = len(nome) - 1
inc = 1

while dec >= 0:
    print( (dec*" ") + nome[dec:] + nome[::-1][1:inc])
    dec -= 1
    inc += 1