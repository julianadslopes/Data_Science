-- And e OR

-- 1. Selecione o name, host_name e host_response_rate 
-- para propriedades que possuem a host_response_rate de 100%
-- e a host_acceptance_rate acima de 90%

SELECT name, host_name, host_response_rate
FROM boston_airbnb_listings
WHERE host_response_rate = 1 
AND host_acceptance_rate > 0.9


-- 2. Selecione name, host_name e host_response_time
-- para propriedades em que o host_response_time é 'within an hour'
-- ou host_is_superhost = TRUE

SELECT name, host_name, host_response_time, host_is_superhost
FROM boston_airbnb_listings
WHERE host_response_time = 'within an hour'
OR host_is_superhost = 'true'

-- 3. Selecione name, host_name de propriedades em (host_neighbourhood)
-- 'South End' ou 'Jamaica Plain'

SELECT name, host_name
FROM boston_airbnb_listings
WHERE host_neighbourhood in 'South End'
OR host_neighbourhood in 'Jamaica Plain'

-- 4. Selecione name, host_name de propriedades em 'South End' ou 'Jamaica Plain'
-- em que host_is_superhost = true

SELECT name, host_name, host_is_superhost, host_neighbourhood
FROM boston_airbnb_listings
WHERE host_is_superhost = 'true'
AND host_neighbourhood = 'South End' OR host_neighbourhood = 'Jamaica Plain'
 

-- 5. Selecione name, host_name de propriedades em 'South End' ou 'Jamaica Plain'
-- que acomodam (accommodates) mais de 4 pessoas

SELECT name, host_name
FROM boston_airbnb_listings
WHERE accommodates > 4
AND host_neighbourhood = 'South End'OR 'host_neighbourhood = 'Jamaica Plain'

-- 6.Selecione name, host_name de peopriedades em 'South End' de 2 dormitórios
-- (bedrooms) em que o preço (price) seja inferior a $ 150.

SELECT name, host_name
FROM boston_airbnb_listings
WHERE host_neighbourhood = 'South End'
AND bedrooms = 2
AND price < 150