--> CONSULTAS E FILTROS

--> Usando a tabela Netlix, solucione os seguintes problemas:

/* 1. Selecione os filmes com o title, rating, release_year de todos os filmes em que o rating seja PG-13 */

SELECT title, rating, release_year
FROM netflix
WHERE rating = 'PG-13'

/* 2. Selecione os filmes com o title, rating, release_year de todos os filmes em que o ratingdescription seja maior ou igual a 100 */

SELECT title, ratng, release_year
FROM netflix
WHERE ratingdescription >= 100

/* 3. Selecione os filmes com o title, rating, release_year de todos os filmes em que o release_year seja 2012 */

SELECT title, rating, release_year 
FROM netflix
WHERE date = '2012'

/* 4. Selecione os filmes com o title, rating, release_year de todos os filmes em que o release_year seja anterior a 2000 */

SELECT title, rating, release_year
FROM netflix
WHERE release_year = '2000'

/* 5. Selecione a lista distinta de filmes com title, rating e release_year de todos os filmes */

SELECT DISTINCT title, rating, release_year
FROM netflix