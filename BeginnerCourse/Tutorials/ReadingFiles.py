#Reading Files


# "r" -> only read file  /  lê o arquivo
# "w" -> write new informations, edit informations  /  adicionar ou alterar informaçãos do documento 
# "a" -> Append infomations to the end of the file   /  acrescenta informações para o final do arquivo
# "r+" -> Read and Write  /  Lê o arquivo e escreve nele


#sempre que abrir o arquivo fechar ele
#para abrir
employee_file = open("BeginnerCourse/Tutorials/ReadingFiles.txt", "r")

print(employee_file.readable())       #Check if files if readable, if it's respond True it's okay
print(employee_file.read())           #lê e imprime todas as informações do documento
print("")

print(employee_file.readline())       #lê a primeira linha do documento
print(employee_file.readline())       #como é a segunda vez usando, vai ler a segunda linha do documento
print("")

print(employee_file.readlines())      #lê o documento e transforma tudo em uma lista 
print(employee_file.readlines()[0])   #podemos acessar coisas especificas da lista colocando o numero do item na lista. Lembrando a lista sempre começa no 0
print("")

for employee in employee_file.readlines():         #podemos criar um loop com isso e ir chamando cada item da lista um por um em loop
    print(employee)

#para fechar
employee_file.close()




#Writing Files
employee_file = open("BeginnerCourse/Tutorials/ReadingFiles.txt", "a")

employee_file.write("\nCj - Chef of Security")                                   #\n para escrever na linha debaixo no arquivo que a gente ta escrevendo

employee_file.close()



#Wrint Files - Porem inves de usar "a" eu usar "w"
#se eu executasse isso, todo o meu arquivo seria reescrito só sobrando Cj - Chef of Security, tomar cuidado com o uso do "w" 
employee_file = open("BeginnerCourse/Tutorials/ReadingFiles2.txt", "w")

employee_file.write("\nCj - Chef of Security")                            

employee_file.close()