#Functions 

#def to start a function,   "name of the function" in my case "say_hi",    and parameter, my case(name and age)
#def para começar a função     "nome da função" no meu caso chama "say_i"    e parametros se desejar, no meu caso(name e age)

#if you are going to pass age together, you need to convert the int to a string
#se for passar idade junto é preciso converter a int para string

def say_hi(name, age):
    print("Hello" + name + " , you are " + str(age))


#to callout a function
say_hi("mike", 32)
say_hi("scooby", 21)
print("")



#Return Statement

def cube(num):
    return num*num*num


result = cube(4)
print(result)
print("")


