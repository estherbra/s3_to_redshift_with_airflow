CREATE TABLE IF NOT exists keycash_schema.LANDING_TABLE (
	id VARCHAR PRIMARY KEY,
	name VARCHAR ( 20 ) NULL,
	idade integer NULL,
	credito_solicitado integer NULL,
	data_solicitacao VARCHAR NULL
);

ALTER TABLE keycash_schema.landing_table ADD COLUMN new_date timestamptz;
UPDATE keycash_schema.landing_table SET new_date = to_timestamp(data_solicitacao, 'MM/DD/YYYY HH24:MI');
ALTER TABLE keycash_schema.landing_table DROP COLUMN data_solicitacao;
ALTER TABLE keycash_schema.landing_table RENAME COLUMN new_date TO data_solicitacao;