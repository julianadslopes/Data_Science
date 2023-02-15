-- LIKE 

-- O comando LIKE nos mostra um resultado que 'contém' na tabela.
-- o Like é usado com % ou com __
-- % é para buscar o os valores que contém a palavra ou letra na em alguma posição na 'string'.
-- _ é para mostrar quantidade de resultados de acordo com a quantidade de _ que você colocar antes ou após a 'string'

-- Selecionando os filmes que terminam com a palavra world

SELECT title, rating, ratinglevel 
FROM netflix
WHERE title LIKE '%world'
ORDER BY title
LIMIt 100; 

SELECT nome_pais, cod_pais, cidade_pais
FROM paises
WHERE nome_pais LIKE 'BR%'
ORDER BY nome_pais
LIMIT 100;

/* Mostre-me todos os personagens (characters) da Família Stark por ordem crescente de nome (character_name) - Tabela got_characters
Mostre-me todos os personagens (characters) cujo nome começa com Jon - got_characters
Mostre-me todos os personagens (characters) cujo nome contenha 'ae' - got_characters
Mostre-me todos os nomes das criaturas cinzentas (grey creatures) - gotcreatures
Mostre-me o número de batalhas em que o rei atacante (attracker_king1) era um Baratheon e o rei defensor (defender_king1) era um Stark - battles (got_battles)
Dê-me tudo de todas as batalhas de verão (summer) em que o atacante (attracker_king1) foi Joffrey
*/