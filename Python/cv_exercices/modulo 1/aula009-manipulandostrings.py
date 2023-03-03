# Fatiamento
frase = 'Curso em Video Python'
print(frase[9])
print(frase[9:14])
print(frase[:5])
print(frase[9::3])
print(frase[13:])
print(frase[9:21:2])

#Análise
print(len(frase))
print(frase.upper().count('o'))
print(frase.count('Curso'))
print(frase.count('o',0,13))
print(frase.lower().count('thon'))
print(frase.count('Bruno'))
print(frase.find('Python'))
print(frase.find('Script'))
print('Curso' in frase)

# Transformação

frase2 = '   Aprenda python  '
print(frase2.strip()) # remove caracteres em branco do inicio e final da frase.
print(frase2.rstrip()) # remove caracteres em branco do lado direito.
print(frase2.lstrip()) # remove caracteres em branco do lado esquerdo.
print(frase2.upper()) # transforma a frase em letras maiusculas.
print(frase2.lower()) # transforma a frase em letras minusculas.
print(frase2.capitalize()) # transforma o primeiro caracter em maiusculo e o restante da frase em minusculo.
print(frase2.title()) # transforma a primeira letra de cada palavra em maiuscula;
print(frase2.replace('Aprenda','Programe'))
#frase2 = frase2.replace('Aprenda','Programe') para atribuir o valor alterado na variável.

# Divisão
# Junção

frase3 = 'Curso de Python'
dividido = frase.split()
print(frase3.split()) # divide a frase em listas, cada palavra é agrupada separadamente com novos índices.
print(dividido[0])
print(dividido[3][1])
print('-'.join(frase3)) # junta a frase separando com traço

# Para dar print em texto muito grandes usa-se """ antes e no final do texto """



