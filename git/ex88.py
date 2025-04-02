ficha = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    m = (nota1+nota2)/2
    ficha.append([nome,[nota1,nota2],m])
    r = str(input('Quer continuar? [S/N]: ')).upper().strip()
    if r == 'N':
        break
print(f'{'N°':<4}{'Nome':<10}{'Média':>8}')
for i,a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8}')
while True:
    opt = int(input(('Digite o codigo do aluno para saber sua nota. [-1 cancela]: ')))
    if opt < 0:
        break
    if opt <= len(ficha):
        print(f'As nota do aluno(a) {ficha[opt][0]} são {ficha[opt][1]}')
    else:
        print('Erro. Código não encontrado')
print('FIM DO PROGRAMA')
