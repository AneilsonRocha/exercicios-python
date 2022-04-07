def somar(elementos):
    somatorio = 0
    for i in elementos:
        somatorio += i["votos"]
    return somatorio    

def exibirMenu():
     print("1 - Candidato Alberto Antônio\n" +
            "2 - Candidato Bernardo Bezerra\n" +
            "3 - Candidata Cássia Cruz\n" +
            "4 - Candidata Daniela Donizetti\n" +
            "5 - Voto em BRANCO\n" +
            "0 - Parar a votação\n" +
            "Qualquer outro código - Voto NULO\n")

def calcPercent(qtdVotos, totalVotos):
    return qtdVotos / totalVotos * 100

def ranquear(lista):
    for i in range(len(lista)-1,0,-1):
        for j in range(i):
            if lista[j]["votos"]<lista[j+1]["votos"]:
                temp = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = temp


candidatos   = [{"nome":"Alberto Antônio", "votos":0},
                {"nome":"Bernardo Bezerra", "votos":0},
                {"nome":"Cássia Cruz", "votos":0},
                {"nome":"Daniela Donizetti", "votos":0}]
votosBrancos = 0
votosNulos   = 0

while True:
    exibirMenu()
    codigo = int(input("Digite o código desejado: "))
    if codigo == 0:
        break
    elif codigo >= 1 and codigo <= 4:
        candidatos[codigo-1]["votos"] += 1
    elif codigo == 5:
        votosBrancos += 1
    else:
        votosNulos += 1

totalEleitores = votosBrancos + votosNulos + somar(candidatos)

print("Número total de eleitores: ", totalEleitores)
ranquear(candidatos)

for i, candidato in enumerate(candidatos):
    nome = candidato["nome"]
    votos = candidato["votos"]
    percent = calcPercent(votos, totalEleitores)
    print(nome + ("- ELEITO" if i == 0 else ""), " obteve ", votos, " votos - ", percent, "%% do total. " )

percent = calcPercent(votosBrancos, totalEleitores)
print("BRANCOS obteve ", votosBrancos, " votos - ", percent, "%% do total. " )

percent = calcPercent(votosNulos, totalEleitores)
print("NULOS obteve ", votosNulos, " votos - ", percent, "%% do total. " )
