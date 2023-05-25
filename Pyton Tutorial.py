#Drawing in python
print("   /|")
print("  / |")
print(" /  |")
print("/___|")
print(" ")


#Variable & Data
character_name = "john"       #tambem chamado de String 
chatacter_age = "35"
is_male = True                #usar boolean (verdadeiro e falso)

print("There once was a man named " + character_name + ", ")
print("he was "+ chatacter_age + " years old.")

character_name = "mike"       #posso mudar a variavel no meio
print("he really liked the name " + character_name +", ")
print("but didn't like being "+ chatacter_age +".")
print(" ")


#Working with String and Function
print("Giraffe\nAcademy")    #pular linha na string com \n ou \"
print(" ")

phrase = "Giraffe Academy"
print(phrase.lower())      #.lower deixa tudo minusculo
print(phrase.upper())      #.upper deixa tudo maiusculo
print(" ")

print(phrase.isupper())    #nesse caso ele vai verificar SE é ou não é maiusculo, retornando um True ou False
print(phrase.upper().isupper())   #posso juntar funções e rodar.
print(" ")

print(len(phrase))                                  #len() funcuina para descobrir o numero de caracteries na variavel
print(phrase[0])                                    #[0] posso fazer aparecer apenas o caracterie da posição numerada, sempre começa do 0. Giraffe = 01234567
print(phrase.index("A"))                            #usando .index() e colocando a letra que você quer, ele descobrirá a posição. #posso usar exemplo: .index("Acade") e ele dará o numero que essa frase começará.
print(phrase.replace("Giraffe", "Elephant"))        #usando .replace() posso trocar alguma parte que eu queira.
print(" ")


#Working with Numbers 
print("git test")
