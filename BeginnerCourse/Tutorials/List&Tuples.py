#working with list
#usamos [] para criar Listas
friends = ["Fabio", "Hique", "Lenon", "thiago", 24, True]                                                #é possivel colocar de tudo, string, numeros, boolean
             #0       #1       #2        #3     #4    #5                                             #todos as coisas na lista tem uma posição index
             #-6      #-5      #-4       #-3    #-2   #-1

print("")
print(friends)                                                                     #fazendo assim acessamos TUDO da lista
print(friends[2])                                                                  #colocando o numero index eu consigo pegar só uma coisa de posição especifica
print(friends[-4])                                                                 #é possivel pegar uma coisa especifica de trás pra frente, nesse caso não tem o 0, começa no -1
print(friends[0:4])                                                   #assim posso pegar alguns de determinada posições do 0 ao 4 porem o correto seria #0 ao #3, mas não é assim. 
print("")


friends[0] = "Ema"
print(friends[0])                                                         #é possivel alterar 1 elemento da lista
print(friends)                                                           #nesse caso substitue o fabio pela ema o resto continua o mesmo
print("")


#List Functions / funções de lista
lucky_numbers = [3, 7, 8, 9, 24, 27, 69]
newfriends = ["Maikon", "Kotaka", "Gus", "Gus", "Franscisco", "Raluca", "Diggo", "JeanL"]
newfriends.extend(lucky_numbers)                                                                    #extend como o nome já diz, ele extende da lista com outra
print(newfriends)
print("")

newfriends.append("Yanny")                                                                          #append ele adiciona algo no final da lista ja existente
print(newfriends)
print("")

newfriends.insert(2, "Vulto")                                                                   #com inset, é colocado na posição especifica e empurra o resto pra trás
print(newfriends)
print("")

newfriends.remove("Raluca")                                              #como o proprio nome diz remove
print(newfriends)
print("")

newfriends.pop()                                                         #pop tira o ultimo item da lista e joga no limbo
print(newfriends)
print("")

print(newfriends.index("Gus"))                                           #vai procurar posiçao expecifica da pessoa/item/numero
print("")

print(newfriends.count("Gus"))                                            #count ele conta quantas vezes a pessoa/item/numero passou na list
print("")

newfriends.clear()                                                        #limpa completamente a lista
print(newfriends)
print("")

#Numeros e nomes juntos não da pra usar sort() não pode ter misturado
amigos = ["Mccree", "Mccree", "Doomfist", "Genji", "Hanzo"]

amigos.sort()                                                        #com sort() podemos organizar a lista de forma alfabetica
print(amigos)
print("")


lucky_numbers.append(1)                                            #só pra teste adicionai o numero 1 no final da lista
print(lucky_numbers)
lucky_numbers.sort()                                               #como eu disse, separados funcionam
print(lucky_numbers)
lucky_numbers.reverse()                                           #podemos reverter, deixar de trás pra frente
print(lucky_numbers)
print("")


amigos2 = amigos.copy()                                          #com copy() podemos copiar uma lista
print(amigos2)
print("")


#Tuples, usamos () em Tuples
coordenates = (3, 7)                                            #tuples é um tipo de lista, porem com algumas diferenças: Ela é imutavel! não pode ser alterada dps de criada, não conseguimos alterar ela. 
              #0  #1                                           #exemplo: coordenates[1] = 10  isso não funcionará porque os valores não podem ser alterados
           
print(coordenates[0])

#Tuples são usamos para dados que nunca serão mudados, por isso coordenadas são um otimo exemplo.
#Tuples are used for data that will never change, so coordinates are a great example.

#é possivel criar uma lista de Tuples | is possible to create a list of tuples.
listcoordenates = [(3,7), (9,13), (24,42)]
