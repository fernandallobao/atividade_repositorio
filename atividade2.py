# 2. Crie um programa que receba o peso (em gramas) de um bebê recém-nascido, e indique se o bebê está normal ou se precisa ficar internado, caso o bebê tenha menos que 2500g.
peso = int(input('Informe o peso do bebê em gramas: '))

if peso < 2500:
    print('O bebê não pode ir para casa. Precisa de mais tempo na incubadora')
else:
    print('O bebê pode ir para casa.')

print('O bebê pode ir pra casa!' if peso >= 2500 else 'O bebê precisa ser internado!') #ternário