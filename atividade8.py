# 8. Crie um programa em que o usuário informe uma quantidade desejada de números decimais de, no mínimo 0 e no máximo 10, e o programa calcula a média desses números.
numeros = []
while True: 
    
    novo_numero = input('Informe um numero ou f para fechar a lista de numeros: ').lower()
    if novo_numero == 'f':
        break
    else:
        novo_numero = int(novo_numero)
        numeros.append(novo_numero)

media = sum(numeros)/len(numeros)

print(f'Resultado da media: {media:,.2f}.')     
  