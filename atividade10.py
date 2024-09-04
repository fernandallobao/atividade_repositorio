# 10.  Crie um programa em que o usuário cadastre quantos cursos ele quiser (nome do curso, duração do curso em horas, Período do dia, quantidade de vagas) e exiba na tela.

chaves = ('Nome do curso','Duração do curso em horas', 'Período do dia', 'Quantidade de vagas')
cursos = []
while True:
    curso = {}
    for chave in chaves:
        curso[chave] = input(f'Informe o/a {chave}: ')
    cursos.append(curso)
    print('\nCurso cadastrado com sucesso!')
    opcao = input('Deseja cadastrar outro curso (s/n): ')
    if opcao == 'n':
        print(f'\n{"="*10} LISTA DE CURSOS {"="*10}\n')
        for curso in cursos:
            for chave in chaves:
                if chave in curso:
                    print(f'{chave}: {curso[chave]}')
            print(f'\n{"-"*10}\n')
        break
    else:
        continue 	