CREATE TABLE IF NOT exists keycash_schema.CREDIT_PER_DAY (
	data_solicitacao date PRIMARY KEY,
	credito_solicitado integer NULL
);


insert into keycash_schema.CREDIT_PER_DAY (
select data_solicitacao, SUM(credito_solicitado) from (
SELECT credito_solicitado, date(data_solicitacao) as data_solicitacao 
FROM  keycash_schema.landing_table
WHERE data_solicitacao IN (
    SELECT MAX(data_solicitacao)
    FROM keycash_schema.landing_table
    GROUP BY name
) order by data_solicitacao asc) group by data_solicitacao order by data_solicitacao)
