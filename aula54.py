"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
# num_int = input('Digite um num inteiro: ')
# if num_int.isdigit():
#     if int(num_int) % 2 == 0:
#         print('Numero par')
#     else:
#         print('Numero impar')
# else:
#     print('Numero nao é inteiro')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
# try:
#     horario = input('Digite as horas (números inteiros): ')
#     horario = int(horario)  # Tenta converter diretamente
#     if 0 <= horario <= 11:
#         print('Bom dia')
#     elif 12 <= horario <= 17:
#         print('Boa tarde')
#     elif 18 <= horario <= 23:
#         print('Boa noite')
#     else:
#         print('Horário fora do intervalo esperado.')
# except ValueError:
#     print('Erro: Digite apenas números inteiros (sem decimais ou outros caracteres).')
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
try:
    nome = input('Digite seu nome: ')
    if not nome.isalpha():
        raise ValueError('Isso nao é um nome')
    elif len(nome) <= 4:
        print('Nome curto')
    elif 5 <= len(nome) <=6:
        print('Nome normal')
    else:
        print('Nome muito grande')
except ValueError as e:
    print(f'Erro: {e}')