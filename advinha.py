from random import randint


def defineModalidade():
    option = ""
    while option != "s" and option != "a":
        option = input("O que você quer ser no jogo? Sorteador (s) ou advinhador?(a)?: ")
        if option != "s" and option != "a":
            print("Opção inválida. Tente novamente.")
    return option


def defineIntervalo():
    global minimo, maximo
    minimo = int(input("Digite o valor mínimo do intervalo: "))
    limite = minimo + 100
    maximo = 0

    while maximo < limite:
        maximo = int(input("Digte o valor máximo que seja maior que {}: ".format(limite)))
        if maximo < limite:
            print("Valor inválido. Tente novamente.")


def defineAlvo():
    alvo = randint(minimo, maximo)
    return alvo


def criaPalpite(dica):
    global media, superior, inferior

    if dica == "":
        superior = maximo
        inferior = minimo
        media = int((inferior + superior) / 2)

    if dica == ">":
        inferior = media
        media = int((inferior + superior) / 2)

    if dica == "<":
        superior = media
        media = int((inferior + superior) / 2)

    return media


def verifica(palpite):
    if modalidade == 's':
        dica = input("O número é {}. Acertei? (a), Maior? (>), Menor? (<): ".format(palpite))

    if modalidade == 'a':
        if palpite == alvo:
            dica = 'a'

        if palpite > alvo:
            dica = '<'

        if palpite < alvo:
            dica = '>'

    return dica

def jogaComputador():
    resposta = ""

    while resposta != 'a':
        palpite = criaPalpite(resposta)
        resposta = verifica(palpite)

        if resposta == 'a':
            print("Eu acertei!")


def jogaHumano():
    global alvo
    alvo = defineAlvo()
    resposta = ""

    while resposta != 'a':
        palpite = int(input("Digite o seu palpite: "))
        resposta = verifica(palpite)

        if resposta == 'a':
            print("Você acertou!")

        if resposta == '>':
            print("Você errou! O número é maior que {}".format(palpite))

        if resposta == '<':
            print("Você errou! O número é menor que {}".format(palpite))


def main():
    global modalidade

    modalidade = defineModalidade()
    defineIntervalo()

    if modalidade == 's':
        jogaComputador()

    if modalidade == 'a':
        jogaHumano()


if __name__ == '__main__':
    main()
