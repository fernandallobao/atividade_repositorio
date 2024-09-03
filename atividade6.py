# 6. Crie um programa que possua uma lista com números de 1 a 20, e informe quais deles são primos

numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(numeros)

num_primos = [] #lista de numeros primos

for num in numeros: 
    if num > 1:  
        primo = True
        for i in range(2, num): #ve se o numero é divisivel por algum numero entre 2 e o ultimo numero da lista
            if num % i == 0: #se o resto da divizao for 0 não é 
                primo = False
                break
        if primo:
            num_primos.append(num)

print("Números num_primos entre 1 e 20:", num_primos)