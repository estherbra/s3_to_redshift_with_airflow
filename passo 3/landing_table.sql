ALTER TABLE keycash_schema.landing_table ADD COLUMN new_date timestamptz;
UPDATE keycash_schema.landing_table SET new_date = to_timestamp(data_solicitacao, 'MM/DD/YYYY HH24:MI');
ALTER TABLE keycash_schema.landing_table DROP COLUMN data_solicitacao;
ALTER TABLE keycash_schema.landing_table RENAME COLUMN new_date TO data_solicitacao;