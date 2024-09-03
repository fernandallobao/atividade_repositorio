# 5. Crie uma lista de 10 nomes (informados dentro do programa). Em seguida, o usuário informa um número inteiro equivalente a um índice, e o programa retorna o nome equivalente ao índice informado pelo usuário.

#lista
nomes = ['Maria','Joaninha','Mariana','Flavia','Elis','Joaquim','Leonidas','Pedro','Andre','Alex']

for i in range(len(nomes)):
    print(f'{i + 1}º nome: {nomes[i]}.')

while True:
    op = input('Informe o índice do nome que deseja ou E para sair: ').lower()
    match op:
        case '1':
            print('Maria')
        case '2':
            print('Joaninha')
        case '3':
            print('Mariana')
        case '4':
            print('Flavia')
        case '5':
            print('Elis')
        case '6':
            print('Joaquim')
        case '7':
            print('Leonidas')
        case '8':
            print('Pedro')
        case '9':
            print('Andre')
        case '10':
            print('Alex')
        case 'e':
            break
        case _:
            print('Opção inválida!')

print('Programa encerrado!')