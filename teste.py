sexo = input('Escolha o sexo (H)omem ou (M)ulher: ').upper()
raca = input('Escolha a raça (Humano ou Elfo): ').capitalize
nome = input('Nome do personagem: ')

if sexo == 'H':
    print('Você escolheu Homem')
elif sexo == 'M':
    print('Você escolheu Mulher')
else:
    print('Sexo inválido')

if raca == 'Humano':
    print('Você escolheu Humano')
elif raca == 'Elfo':
    print('Você escolheu Elfo')
else:
    print('Raça inválida')

print(f'Nome do personagem: {nome}')