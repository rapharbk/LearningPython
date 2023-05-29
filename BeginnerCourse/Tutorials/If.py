#If Statement

is_male = True
is_tall = True

#or = 1 dos 2 era verdadeiro para passar
#and = os 2 tem que ser verdadeiro para passar

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male but are tall") 
else:
    print("You are not a male and not tall")
print("")




#If Statements & Comparisons

# tipos de comparações:
# == Igual
# != Não é igual
# >= Maior igual
# <= Menor igual
# > Maior que
# < Menor que

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max_num(300, 5231, 14))
print("")