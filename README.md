<div style="font-size:20px">
  <h1>s3 to redshift with Apache Airflow - Case Keycash</h1>
</div>

# Sobre o Projeto

<br/>

## 🌐 Overview

Esse projeto foi feito com a linguagem de programação Python, utilizando o AWS SDK para Python Boto3 para facilitar a integração do script com o serviço de Cloud Storage da AWS (Amazon s3), além das bibliotecas json, pandas, os e glob.
Foi utilizado o orquestrador de fluxos Apache Airflow para a criação de um trigger com horário pré-definido e a ferramenta de administração de banco de dados multiplataforma Dbeaver, conectada ao Data Warehouse Amazon Redshift para execução de queries. O trigger é disparado num horário específico e copia todos os dados de uma vez do s3 Bucket para uma tabela chamada "landing_table" no Data Warehouse.
Por fim, o Data Warehouse é conectado á ferramenta Power BI, que consiste em um serviço de análise de negócios e fornece uma visualização da tabela credit_per_day.

<br/>

### Arquitetura do projeto:

![arquitetura do projeto](https://i.imgur.com/jepb5AO.png)

## Passo a passo 
1. A primeira etapa consiste em ajustar algumas permissões do bucket, como a inclusão da action "s3:PutObject" na política (caso necessário), para em seguida fazer a ingestão dos 50 arquivos semi-estruturados em um Bucket da Amazon s3 através de um script Python, no qual também é realizada a conversão do tipo json para csv por meio da biblioteca pandas.

![política bucket](https://i.imgur.com/FgASFtB.png)

![objetos s3 bucket](https://i.imgur.com/UuJ2kER.png)

2. Na segunda etapa, é criado o cluster redshift abaixo e conectado ao Dbeaver através do seu endpoint.

![Redshift Cluster](https://i.imgur.com/Whq71se.png)

![conexão Dbeaver](https://i.imgur.com/zs6cVj3.png)

3. Download do Apache Airflow e criação da DAG escrita em Python, a qual se conecta com o bucket e dispara o trigger que envia os arquivos contidos nele para a tabela "landing_table" no Amazon Redshift em um horário pré-determinado (19h30 do dia 21 de fevereiro) através de CRON expression '30 19 21 02 mon'. A DAG file está disponível neste repositório

![DAG](https://i.imgur.com/xMS8t4Q.png)

![DAG](https://i.imgur.com/KiGc6wG.png)

4. A partir da tabela landing_table foi criada uma nova chamada credit_per_day, agregando o somatório de Crédito Solicitado (credito_solicitado) por dia (data_solicitada), considerando que alguns clientes podem ter solicitado crédito mais de uma vez e apenas a solicitação mais recente é válida. As consultas estão disponíveis neste repositório.

![landing_table](https://i.imgur.com/CsqbOtG.png)

![credit_per_day](https://i.imgur.com/5Jt4qdd.png)

5. Por fim, com o objetivo de criar uma visualização da tabela credit_per_day, o Data Warehouse foi conectado á ferramenta Power BI, resultando no seguinte:

![power bi](https://i.imgur.com/nU7NvGr.png)


# Configurando o ambiente

### Requerimentos

- Python version 3.9
- Apache Airflow version 2.2.3
- Pandas version 1.1.3
- Dbeaver version 21.3.3


 <br/>

### Instalando as dependencias

```
pip install boto3
pip install pandas
```

<br/>

