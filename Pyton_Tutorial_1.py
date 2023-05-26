#Drawing in python
print("   /|")
print("  / |")
print(" /  |")
print("/___|")
print(" ")


#Variable & Data
character_name = "john"                              #tambem chamado de String 
chatacter_age = "35"
is_male = True                                       #usar boolean (verdadeiro e falso)

print("There once was a man named " + character_name + ", ")
print("he was "+ chatacter_age + " years old.")

character_name = "mike"                             #posso mudar a variavel no meio
print("he really liked the name " + character_name +", ")
print("but didn't like being "+ chatacter_age +".")
print(" ")


#Working with String and Function
print("Giraffe\nAcademy")                           #pular linha na string com \n ou \"
print(" ")

phrase = "Giraffe Academy"
print(phrase.lower())                               #.lower deixa tudo minusculo
print(phrase.upper())                               #.upper deixa tudo maiusculo
print(" ")

print(phrase.isupper())                             #nesse caso ele vai verificar SE é ou não é maiusculo, retornando um True ou False
print(phrase.upper().isupper())                     #posso juntar funções e rodar.
print(" ")

print(len(phrase))                                  #len() funcuina para descobrir o numero de caracteries na variavel
print(phrase[0])                                    #[0] posso fazer aparecer apenas o caracterie da posição numerada, sempre começa do 0. Giraffe = 01234567
print(phrase.index("A"))                            #usando .index() e colocando a letra que você quer, ele descobrirá a posição. #posso usar exemplo: .index("Acade") e ele dará o numero que essa frase começará.
print(phrase.replace("Giraffe", "Elephant"))        #usando .replace() posso trocar alguma parte que eu queira.
print(" ")


#Working with Numbers 
print(-3.6969)
print(3 + 3)
print(3 * 3)
print(3 / 3)
print(" ")

print(3 * (4 + 5))                                   #é possivel fazer contas até mais complicadas usando.
print(10 % 3)                                        #nessa conta o resultado será 1 pois a "%" faz com o que ele sobre apenas o Resto da conta, 10/3 da pra dividir por 3, porém sobra o 1. e esse 1 é a sobra!
print(" ")

my_num = 5                                           #podemos armazeram ela em uma variavel também
print(my_num)
print(str(my_num) + " my luck number")               #podemos converter um numero para uma String. numeros não podem se misturar com string, fazendo isso podemos adicionar um texto
print(" ")

my_num2 = -5
print(abs(my_num2))                                 #ele da a base absoluta do meu numero
print(pow(3, 2))                                    #Pow é o numero elevado. 3^2 ou 3².
print(pow(5, 3))
print(max(4, 6))                                    #com isso irá imprimir o Maior numero, no caso o 6
print(min(4, 6))                                    #com isso irá imprimir o Menor numero, o numero 4
print(round(3.2))                                   #round() é Arredondar o numero, logo 3.2 = 3      se fosse 3.8 = 4
print(" ")


#For some mathematical calculations it is necessary to import a "library"
from math import *

print(floor(3.7))                                   #com isso ele cortará os numeros dps da virgura. dirou o .7
print(ceil(3.7))                                    #como se fosse o de arrendondar, tenho que produrar a diferença
print(sqrt(36))                                     #sqrt() derá a raiz quadrada do numero. raiz quadrada de 36 = 6.
print(" ")


#Getting input from users
name = input("Enter your name: ")                   #o "input" vai armazenar na variavel "name"
age = input("Enter your age: ")
print("Hello " + name + "! you are " + age)

