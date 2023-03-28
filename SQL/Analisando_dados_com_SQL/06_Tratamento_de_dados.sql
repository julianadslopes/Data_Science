-- Instrução CASE ( De, Para)

-- Verificando a quantidade de registros na tabela
SELECT COUNT(*)
FROM tb_pacientes;

-- Binarização variável classe (0/1)
-- Contabilizar o total de registros distintos
-- Utilizando 0 para eventos negativos e 1 para eventos positivos

SELECT DISTINCT classe 
FROM tb_pacientes;

SELECT
	CASE
		WHEN classe = 'no-recurrence-events' THEN 0
        WHEN classe = 'recurrence-events' THEN 1
	END as classe
FROM tb_pacientes;

SELECT DISTINCT irradiando
FROM tb_pacientes;

SELECT
	CASE
		WHEN irradiando = 'no' THEN 0
        WHEN irradiando = 'yes' THEN 1
	END as irradiando
FROM tb_pacientes;

-- Tratando valores ausentes utilizando o número 2

SELECT DISTINCT node_caps 
FROM tb_pacientes;

SELECT
	CASE
		WHEN node_caps = 'no' THEN 0
        WHEN node_caps = 'yes' THEN 1
        ELSE 2
	END as node_caps
FROM tb_pacientes;

-- -- Categorização

SELECT DISTINCT seio
FROM tb_pacientes;

SELECT
	CASE
		WHEN seio = 'left' THEN 'E'
        WHEN seio = 'right' THEN 'D'
	END as seio
FROM tb_pacientes;

SELECT DISTINCT tamanho_tumor
FROM tb_pacientes;

SELECT
	CASE
		WHEN tamanho_tumor = '0-4' OR tamanho_tumor = 'muito pequeno'
        WHEN tamanho_tumor = '10-14' OR tamanho_tumor = '15-19' THEN 'pequeno'
        WHEN tamanho_tumor = '20-24' OR tamanho_tumor = '25-29' THEN 'medio'
        WHEN tamanho_tumor = '30-34' OR tamanho_tumor = '35-39' THEN 'grande'
        WHEN tamanho_tumor = '40-44' OR tamanho_tumor = '45-49' THEN 'muito grande'
        ELSE 'urgente'
	END as tamanho_tumor
FROM tb_pacientes;

-- Label Encoding

SELECT
	CASE
		WHEN quadrante = 'left_low' THEN 1
        WHEN quadrante = 'right_low' THEN 2
        WHEN quadrante = 'left_up' THEN 3
        WHEN quadrante = 'right_up' THEN 4
        WHEN quadrante = 'central' THEN 5
        ELSE 0
	END as quadrante
FROM tb_pacientes;

-- Criando um novo dataset com as modificações realizadas

SELECT
	CASE
		WHEN classe = 'no-recurrence-events' THEN 0
        WHEN classe = 'recurrence-events' THEN 1
	END as classe,
	idade,
	menopausa,
	CASE
		WHEN irradiando = 'no' THEN 0
        WHEN irradiando = 'yes' THEN 1
	END as irradiando,
	inv_nodes,
	CASE
		WHEN node_caps = 'no' THEN 0
        WHEN node_caps = 'yes' THEN 1
        ELSE 2
	END as node_caps,
	deg_malig,
	CASE
		WHEN seio = 'left' THEN 'E'
        WHEN seio = 'right' THEN 'D'
	END as seio,
	CASE
		WHEN tamanho_tumor = '0-4' AND '5-9' THEN 'muito pequeno'
        WHEN tamanho_tumor = '10-14' AND '15-19' THEN 'pequeno'
        WHEN tamanho_tumor = '20-24' AND '25-29' THEN 'medio'
        WHEN tamanho_tumor = '30-34' AND '35-39' THEN 'grande'
        WHEN tamanho_tumor = '40-44' AND '45-49' THEN 'muito grande'
        ELSE 'urgente'
	END as tamanho_tumor,
	CASE
		WHEN quadrante = 'left_low' THEN 1
        WHEN quadrante = 'right_low' THEN 2
        WHEN quadrante = 'left_up' THEN 3
        WHEN quadrante = 'right_up' THEN 4
        WHEN quadrante = 'central' THEN 5
        ELSE 0
	END as quadrante
FROM tb_pacientes;

-- Criando um arquivo .CSV da nova tabela para envio ao Cientista de Dados

-- Botão direito na tabela - Table Data Export Wizard - Browser

-- Trabalhando com o dataset versão final após as transformações feitas durante as aulas 
-- neste capítulo, crie instruções SQL que resolvam às questões abaixo:

-- 1- Aplique label encoding à variável menopausa.
SELECT DISTINCT menopausa
FROM tb_pacientes2;

SELECT
	CASE
		WHEN menopausa = 'premeno' THEN 1
        WHEN menopausa = 'ge40' THEN 2
        WHEN menopausa = 'lt40' THEN 3
	END as menopausa
FROM tb_pacientes2;

-- Criando uma nova tabela aplicando Label-Encoding na variável 'menopausa'

CREATE TABLE db_cancer.tb_pacientes3
AS
SELECT
	classe,
	idade,
	CASE
		WHEN menopausa = 'premeno' THEN 1
		WHEN menopausa = 'ge40' THEN 2
		WHEN menopausa = 'lt40' THEN 3
	END as menopausa,
	irradiando,
	inv_nodes,
	node_caps,
	deg_malig,
	seio,
	tamanho_tumor,
	quadrante
FROM db_cancer.tb_pacientes2;

SELECT * FROM tb_pacientes3;

-- 2- [Desafio] Crie uma nova coluna chamada posicao_tumor concatenando as colunas inv_nodes e quadrante.
ALTER TABLE db_cancer.tb_pacientes2 
ADD COLUMN posicao_tumor INT 
AFTER quadrante;

-- 3- [Desafio] Aplique One-Hot-Encoding à coluna deg_malig.
SELECT DISTINCT deg_malig
FROM tb_pacientes3;

SELECT 
	CASE
		WHEN deg_malig = 1 THEN 'baixo'
        WHEN deg_malig = 2 THEN 'medio'
        WHEN deg_malig = 3 THEN 'alto'
	END as deg_malig
FROM tb_pacientes3;

-- 4- Crie um novo dataset com todas as variáveis após as transformações anteriores

