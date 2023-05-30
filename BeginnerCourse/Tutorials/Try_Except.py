#Try / Except

try:
    # value = 10/0                                                                 # se eu ativar esse aqui, o except de ZeroDivisonError vai pegar
    number = int(input("Enter a Number: "))
    print(number)
except ZeroDivisionError as err:
    print("err")
except ValueError:
    print("Invalid Input")