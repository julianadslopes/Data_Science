-- BETWEEN

-- O comando BETWEEN nos mostra os dados ENTRE os valores a serem buscados.
-- Um detalhe no BETWEEN que ele inclui o primeiro valor e o último valor da pesquisa.
-- Quando estamos buscando 'strings' só é possível que ele encontre se buscarmos em ordem alfabética.

SELECT * 
FROM netflix
WHERE title BETWEEN "13 Reason Wh" AND "Baby Dadd"
ORDER BY title
LIMIT 100

SELECT *
FROM netflix
WHERE ratingdescription BETWEEN 80 AND 110
ORDER BY title
LIMIT 100


-- IN () e NOT IN ()

-- Diferente do BETWEEN, o IN e NOT in buscam valores que contam na tabela ou não.
-- Ex: IN(1, 3, 5)  mostra somente estes valores se estiverem na tabela.
-- Ex: IN(Pedro e Paulo) mostra somente estas palavras se estiverem na tabela.
-- EX: NOT IN(Pedro, Paulo) queremos todos os valores menos Pedro e Paulo. 

SELECT *
FROM netflix
WHERE ratingdescription IN (70, 80, 100)
ORDER BY title
LIMIT 100