# Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase sem espaços em branco no início e no fim e em letras minúsculas.
frase = input('Escreva uma frase: ')
frase = frase.strip().lower()
print(frase)