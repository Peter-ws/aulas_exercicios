a = 'A'
b = 'B'
c = 1.1
print('a={} b={} c={:.2f}'.format(a,b,c))
#OU
string = 'a={} b={} c={:.2f}'
print(string.format(a,b,c))
#INVERTENDO A ORDEM COM INDICES e repetindo valores
string = 'a={2:.2f} b={1} c={0} c={0}'
print(string.format(a,b,c))
#EXEMPLO COM PARAMETRO NOMEADO
string = 'a={letraC:.2f} b={1} c={0} c={0}'
print(string.format(a,b,letraC=c))
#TUDO QUE ESTIVER NA FRENTE DO P. NOMEADO PRECISA TB ESTAR NOMEADO. REGRA
print(2*'W')