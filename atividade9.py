# 9. Crie um programa onde o usuário cadastre uma quantidade desejada de eventos (nome do evento e classificação indicativa) e após o cadastro dos eventos, o usuário possa informar o nome e a idade, e se inscrever em um dos eventos. Caso o usuário não tenha idade mínima, o programa proíbe a inscrição e pede para o mesmo se inscrever em outro evento. Caso o usuário tenha a idade mínima, o programa inscreve o usuário exibindo a data da inscrição e encerra.
eventos = []

while True:
    op = input('Deseja cadastrar um novo evento (s/n)?').lower()

    if op == 's':
        evento = {}
        evento['nome_evento'] = input('Informe o nome do evento: ')
        evento['classificacao'] = input('Informe a classificação do evento: ')
        eventos.append(evento)
    else:
        break

print('Estes são os eventos disponíveis: ')
for evento in eventos:
    print(evento)

idade = int(input('Informe sua idade'))

if idade <= :
    

