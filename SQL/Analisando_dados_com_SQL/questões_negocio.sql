Respondendo perguntas de negócio em SQL

-- 1. Quantas pessoas submeteram uma aplicação e quantas pessoas não submeteram uma aplicação?
-- R. Submeteram = 1500, Não submeteram = 500

SELECT submitted_at, COUNT(applicant_id)
FROM applications_csv
WHERE submitted_at IS NULL;

-- 2. Quais são os 3 job titles com os mais altos salários médios (average salary) em São Francisco?
-- R. General Manager = 399.211, Chief Investment = 339.653, Chief of Police = 329.183

SELECT jobtitle, AVG(totalpay)
FROM san_francisco_salaries
GROUP BY jobtitle
ORDER BY totalpay DESC
LIMIT 30;

-- 3. Qual é o maior salário do funcinário que responde ao gerente Timothy Kring?
-- R. 102.596

SELECT a.employee_id, b.manager, a.salary
FROM employee_status a
JOIN employee_state_manager b
ON a.employee_id=b.employee_id
WHERE b.manager = 'Timothy Kring'
ORDER BY a.salary DESC

-- 4. Quantos shows tiveram o user_rating_score igual ou acima de 90 entre os anos de 2010 à 2017 de acordo com o rating?
-- R. 7 SHOWS

SELECT rating, COUNT(user_rating_score)
FROM netflix
WHERE user_rating_score >= 90 
AND release_year BETWEEN 2010 AND 2017
GROUP BY rating;

-- 5. Liste o título (title) de todas as séries ou filmes que possuem a o termo "scary images" no campo ratinglevel e que tenham sido lançadas de 2013 em diante (incluindo 2013).

SELECT DISTINCT title
FROM netflix
WHERE ratinglevel LIKE '%scary images%'
AND release_year >= 2013;

-- 6. Qual o navegador mais usado pelo total de visitas e quantas vezes ele foi usado?
-- R. Google - 64 Visistas

SELECT browser, COUNT(timestamp) 
FROM platform_usage
GROUP BY browser
ORDER BY COUNT(timestamp) DESC;

-- 7. Quantos usuários entre 18 e 35 anos (campo age) visitaram a nossa plataforma em um dispositivo móvel (mobile) em 2019?
-- R. 14 Usuários

SELECT p.device_type, COUNT (u.user_id)
FROM platform_usage p
JOIN user_info u
ON p.user_id = u.user_id
WHERE p.device_type = 'mobile'
AND u.age BETWEEN 18 AND 35
AND YEAR(p.timestamp) = 2019

-- 8. Usuários que acessaram a plataforma em todos os anos, axceto 2019.
-- R. 100001 a 100074

SELECT u.user_id
FROM platform_usage p
JOIN user_info u 
ON p.user_id = u.user_id
WHERE YEAR(p.`timestamp`) != 2019
ORDER BY u.user_id;