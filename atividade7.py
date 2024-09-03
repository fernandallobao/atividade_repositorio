# 7. Crie um programa onde o usuário possa digitar uma lista de nomes (quantos ele quiser) e no final exiba a lista de nomes em ordem alfabética na tela, mostrando também o número de nomes digitado pelo usuário.
nomes = []

while True: 
    novo_nome = input('Informe um nome ou S para sair: ').lower()
    if novo_nome == 's':
        break
    else:
        nomes.append(novo_nome)
        nomes.sort()

    for nome in nomes:
        print(nome)
