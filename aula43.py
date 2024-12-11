nome = input('Digite seu nome: ')
encontrar = input( 'Digite oque deseja encontrar: ')
if encontrar in nome:
    print(f'{encontrar} está dentro de {nome}')
else:
    print(f'{encontrar} não esta dentro de {nome}')