num1 = input("Enter a number: ")                                  #input gera String, para fazer a calcuradora precisamos converter essas strings em numeros
num2 = input("Enter another number: ")
result = float(num1) + float(num2)                                    #int() converte para numero, porém, INT serve apenas para numeros inteiros, numeros quebrados tipo 3.2 daria erro
                                                                      #agora com float() conseguimos calcular com numeros quebrados.
print(result)


#isso é só o basico do basico.