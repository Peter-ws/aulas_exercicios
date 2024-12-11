nome = 'Peterson'
altura = 1.74
peso = 53.3
imc = peso / (altura*altura)
print(nome,'tem',f'{altura:.1f}','de altura,','\npesa',peso, 'quilos e seu IMC é')
# print(f"{imc:.2f}") #exemplo de f-string
print(round(imc,2)) 
'''O round mais o argumento 2 faz com que o valor seja arredondado e exiba
2 casas decimais, porem, caso o valor das duas casas seja abaixo de 5 ele 
pode exibir apenas 1 casa decimal. Para corrigir isso, pode-se usar
o f-string'''

#outra forma:

print(f'{nome} tem {altura:.2f} de altura')