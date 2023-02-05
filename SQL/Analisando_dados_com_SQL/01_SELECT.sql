--> SELECT

-- Consultando todas as colunas da tabela Game Of Thrones

SELECT * FROM got_charaters

-- Consultando colunas da tabela Game Of Thrones

SELECT character_name, person_id
FROM got_characters

-- Limitando linhas da tabela

SELECT character_name, person_id, birthyear, gender
FROM got_characters
LIMIT 10

-- Listar os 10 primeiros valores da tabela GOTCharacters com nome e gender

SELECT character_name, gender
FROM got_characters
ORDER BY character_name 
LIMIT 10

-- Traga-me a lista única de species da tabela GOTcreatures

SELECT DISTINCT species
FROM gotcreatures
ORDER BY species

-- Traga-me as primeiras 37 linhas da tabela GOTHouses

SELECT *
FROM gothouses
LIMIT 37

-- Qual a lista de filmes da tabela Netflix com title, rating e release_year

SELECT title, rating, release_year
FROM netflix
ORDER BY title

-- Qual os 100 primeiros resultados da lista de filmes da Netflix

SELECT *
FROM netflix
ORDER BY title
LIMIT 100

-- Qual a lista de filmes da tabela Netflix contendo title, rating, rating_description e release_year (apenas os 1000 primeiros)

SELECT title, rating, ratingdescription, release_year
FROM netflix
ORDER BY title
LIMIT 1000 

-- Qual a lista de todos os titles da Netflix ordenada por ordem alfabética

SELECT DISTINCT title
FROM netflix
ORDER BY title