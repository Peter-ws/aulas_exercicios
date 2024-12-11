print(type(20),type('frase'))

#Escape (\)
print("Peterson \"Warley\"") #dessa forma ele nao le essas aspas como parte da função e sim como parte do texto

#r
print(r"Peterson \"Warley\"") #Colocando o r faz com que possa ser exibido o \ que é o escape, caso precise

#Forma mais simples é colocar a string dentro de aspas simples e usar as aspas duplas ou vice-versa

print("'texto com aspas simples'")

def print_com_tipo(argumento):
    print(f"Tipo do argumento: {type(argumento)}"), 
#o f faz com que funçoes, operaçoes e etc que estejam dentro das chaves na string sejam executadas
    #print(argumento)
    return argumento


print(print_com_tipo(12))


