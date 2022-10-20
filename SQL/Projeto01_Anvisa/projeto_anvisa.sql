CREATE TABLE tb_navios (
nome_navio VARCHAR(50),
mes_ano VARCHAR(10),
classificacao_risco VARCHAR(15),
indice_conformidade VARCHAR(15),
pontuacao_risco INT,
temporada VARCHAR(200)
)

USE db_anvisa;

SELECT * FROM db_anvisa.tb_navios;

SELECT nome_navio, mes_ano FROM db_anvisa.tb_navios;

SELECT DISTINCT classificacao_risco FROM db_anvisa.tb_navios; -- (mostra os valores únicos da coluna)

SELECT nome_navio, classificacao_risco, pontuacao_risco, temporada 
FROM tb_navios
WHERE classificacao_risco = 'D' AND pontuacao_risco > 900
ORDER BY nome_navio;

SELECT nome_navio, classificacao_risco, pontuacao_risco, temporada 
FROM tb_navios
WHERE classificacao_risco = 'D' OR pontuacao_risco > 3000
ORDER BY nome_navio;

SELECT nome_navio, classificacao_risco, indice_conformidade, temporada
FROM tb_navios
WHERE classificacao_risco IN ('A', 'B') AND indice_conformidade > 90
ORDER BY indice_conformidade, nome_navio
LIMIT 10;

-- Em Março de 2015 alguma embarcação teve índice de conformidade de 100% e pontuação de risco igual a 0?

SELECT nome_navio, mes_ano, classificacao_risco, indice_conformidade, pontuacao_risco, temporada
FROM tb_navios
WHERE indice_conformidade > 90 AND pontuacao_risco = 0 AND mes_ano = 'mar/15'
ORDER BY nome_navio, indice_conformidade;

-- Mesma consulta usando SUB QUERY (maior carga no banco de dados, prejudica o desempenho)

SELECT nome_navio, mes_ano, classificacao_risco, indice_conformidade, pontuacao_risco, temporada
FROM tb_navios
WHERE indice_conformidade IN (SELECT indice_conformidade
								FROM db_anvisa.tb_navios
                                WHERE indice_conformidade > 90)
                                AND pontuacao_risco = 0
                                AND mes_ano = 'mar/15'
ORDER BY nome_navio, indice_conformidade;








