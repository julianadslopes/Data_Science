# Crie um progama que leia o nome de uma cidade e diga se ela começa ou não com a palavra "SANTO".

cidade = str(input('Digite o nome de uma cidade: ')).strip()
print(cidade[0:5].upper() == 'SANTO')