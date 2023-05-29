#transformar em uma lingua fictícia


#Lingua do A   Transformar vogais em -> A
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "eiou":
            if letter.isupper():
                translation = translation + "A"
            else:
                translation = translation + "a"
        else:
            translation = translation + letter
    return translation


print(translate(input("Coloque uma frase: ")))
