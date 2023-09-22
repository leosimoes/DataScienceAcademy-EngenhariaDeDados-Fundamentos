# DataScienceAcademy - Fundamentos de Engenharia de Dados
Atividades do curso "Fundamentos de Engenharia de Dados" da DataScienceAcademy.


## Atividades
- Demonstração Prática 1 - Funcionamento de um Sistema Distribuído
    * Definindo o Ambiente: Hadoop HDFS, cluster com 4 máquinas (1 master e 3 slaves);
    * Carga de Dados: a replicação do bloco vai depender do fator de replicação;
    * Comportamento do Sistema Distribuído quando um servidor fica indisponível: 
      tolerância a falhas já que pode usar outra máquina, se uma não estiver disponivel;
    * Acceso aos Dados.
- Demonstração Prática 2 - Implementando Um Data Lakehouse
    * Usamos o Data LakeHouse para armazenar um JSON e carregar dados semi-estruturados e analisá-los no formato tabular;
    * Airbyte (Ferramenta ELT) -> Amazon S3 (Data Lake) -> Dremio;
    * Airbyte pega o arquivo JSON da origin e carrega no Amazon S3, onde o Dremio busca e prepara os dados e retorna-os em formato tabular.
- Demonstração Prática 3 - Linhagem de Dados de Data Warehouse com SQLFlow.
    * Acessar via https://www.gudusoft.com/ ou https://sqlflow.gudusoft.com/#/
    * Use a versão completa por um período de teste que roda no navegador;
    * O software permite visualizar o histórico de mudanças nas tabelas a partir dos scripts SQL;
    * Crie Views para consultas específicas;
- Demonstração Prática 4 - Criação de Pipeline de Extração, Limpeza, Transformação e Enriquecimento de Dados.


## Referências
DataScienceAcademy - Fundamentos de Engenharia de Dados:
https://www.datascienceacademy.com.br/path-player?courseid=fundamentos-de-engenharia-de-dados , 
Acessado em 18/09/2023.