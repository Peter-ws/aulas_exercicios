'''Interpolação de strings
s == string
d e i == int
f == float
x e X == Hexadecimal (ABCDEF0123456789)
'''
nome = 'Peterson'
preco = 1000.846844
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %04X' % (1500, 9832131)) 
'''COloquei um valor grande em exadecimal e coloquei para aparecer pelo menos 
4 digitos, caso o valor seja maior, ele colocara todo o valor'''