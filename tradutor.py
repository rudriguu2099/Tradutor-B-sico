def carregar_palavras(arquivo_pt, arquivo_en):
    with open(arquivo_pt, 'r') as f_pt, open(arquivo_en, 'r') as f_en:
        portugues = [linha.strip() for linha in f_pt]
        ingles = [linha.strip() for linha in f_en]
        return {portugues[i]: ingles[i] for i in range(len(portugues))}
        
def traduzir_frase(string, banco_de_palavras):
    for palavra in string:
        if palavra in banco_de_palavras:
            print(banco_de_palavras[palavra], end=' ')
        else:
            print("[Palavra não encontrada]", end=' ')
    print()

def main():
    print("Olá, seja bem vindo ao nosso tradutor colaborativo!!")
    banco_de_palavras = carregar_palavras('portugues.txt', 'ingles.txt')

    print("Para iniciarmos, escolha sua ação:")
    while True:
        acao = input("[1] Traduzir\n[2] Registrar palavra\n[3] Sair\n")
        if acao == '1':
            print("Ok! Digite abaixo o que você quer traduzir:")
            frase = input().split()
            traduzir_frase(frase, banco_de_palavras)
        elif acao == '2':
            print("Ok! Digite abaixo o que você quer registrar em português e inglês:")
            registerpt = input("português: ").strip()
            registeren = input("inglês: ").strip()
            banco_de_palavras[registerpt] = registeren
            print(f"Palavra '{registerpt}' registrada com sucesso!")
        elif acao == '3':
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()
