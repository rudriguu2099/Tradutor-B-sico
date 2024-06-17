#tradutor
banco_de_palavras = {}

def traduzir_frase(string):
    for palavra in string:
        if palavra in banco_de_palavras:
            print(banco_de_palavras[palavra], end= ' ')
        else:
            print("Frase fora do banco de dados, Por Favor, registre ela antes de querer traduzi-la.")
    print(" ")
def main():
    print("Olá, seja bem vindo ao nosso tradutor colaborativo!!")
    print("Para iniciarmos, escolha sua ação:")
    while True:
        acao = int(input("[1] Traduzir\n[2] Registrar palavra\n[3] Sair\n"))
        if acao == 1:
            print("Ok! Digite abaixo o que você quer traduzir:")
            frase = input().split()
            traduzir_frase(frase)
        if acao == 2:
            print("Ok! Digite abaixo o que você quer registrar em inglês e português:")
            registerpt = input("português: ").strip()
            registeren = input("inglês: ").strip()
            banco_de_palavras[registerpt] = registeren
        if acao == 3:
            print("Encerrando o programa...")
            break
main()