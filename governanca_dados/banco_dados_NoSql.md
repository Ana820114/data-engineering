# Bancos de Dados NoSQL e Relacionais

## Bancos de Dados NoSQL

### Descrição
NoSQL é um termo genérico que define bancos de dados não-relacionais. Desenvolvido por empresas líderes da Internet como Google, Facebook, Amazon e LinkedIn, a tecnologia NoSQL surgiu para superar as limitações dos bancos de dados relacionais, especialmente para aplicações web modernas. Não significa que seus modelos não possuam relacionamentos, mas sim que não são orientados a tabelas. O termo "NoSQL" é uma abreviação de "Not Only SQL" (não apenas SQL).

### Características
- **Escalabilidade Horizontal**: Permite a adição de mais servidores para lidar com o aumento de carga, ao contrário da escalabilidade vertical dos bancos relacionais.
- **Ausência de Esquema ou Esquema Flexível**: Não requer um esquema fixo, facilitando a adaptação a mudanças na estrutura de dados.
- **Suporte a Replicação**: Permite a cópia dos dados em múltiplos servidores para garantir alta disponibilidade e redundância.
- **API Simples**: Geralmente possui interfaces mais simples para operações de leitura e escrita.
- **Consistência Eventual**: Nem sempre prioriza a consistência imediata dos dados em favor da disponibilidade e partição.

### Ausência de Esquema
A ausência de esquema ou esquema flexível é uma característica fundamental dos bancos de dados NoSQL. Esta característica permite uma alta escalabilidade e disponibilidade, pois os dados podem ser armazenados sem a necessidade de um esquema fixo. No entanto, essa flexibilidade pode comprometer a integridade dos dados, um aspecto que é garantido no modelo relacional.

### Exemplos de Bancos de Dados NoSQL
- **Aerospike**: Famoso por sua velocidade de memória, ideal para empresas que precisam de respostas em milissegundos, como aquelas em anúncios e jogos.
- **Apache Cassandra**: Destaca-se pela modelagem de dados NoSQL e escalabilidade linear flexível, utilizando clusters.
- **Amazon DynamoDB**: Desenvolvido pela Amazon para suportar seu e-commerce com alta escalabilidade, inspirou outros projetos NoSQL.
- **MongoDB**: O banco de dados NoSQL mais popular, conhecido por sua facilidade de desenvolvimento e manejo flexível dos dados.
- **HBase**: Funciona sobre o HDFS (Hadoop Distributed File System), oferecendo grande escalabilidade e integração com Hadoop.
- **Redis**: Um banco de dados NoSQL do tipo chave-valor, amplamente utilizado para cache e armazenamento rápido.

## Bancos de Dados Relacionais

### Descrição
Os Bancos de Dados Relacionais (RDBMS) são projetados para armazenar dados de forma estruturada em tabelas, seguindo o modelo relacional. Utilizam a linguagem SQL (Structured Query Language) para manipulação e consulta dos dados.

### Elementos Básicos
- **Relações (Tabelas)**: Estruturas que armazenam dados em formato de linhas e colunas.
- **Registros (Tuplas)**: Cada linha de uma tabela que representa uma instância de dados.

### Características Fundamentais
- **Restrições de Integridade**: Regras que garantem a precisão e consistência dos dados, como:
  - **PK (Primary Key)**: Identificador único para cada registro.
  - **FK (Foreign Key)**: Estabelece relações entre tabelas.
  - **UK (Unique Key)**: Garante valores únicos em uma coluna.
  - **CK (Check Key)**: Valida dados inseridos.
  - **NN (Not Null)**: Garante que uma coluna não tenha valores nulos.

### Exemplos de Bancos de Dados Relacionais
- **MySQL**: Sistema de gerenciamento de banco de dados relacional open-source, amplamente utilizado em aplicações web.
- **PostgreSQL**: Conhecido por sua conformidade com os padrões SQL e extensibilidade.
- **Oracle Database**: Um dos principais sistemas de banco de dados comerciais, com ampla gama de funcionalidades e ferramentas.
- **Microsoft SQL Server**: Oferece integração com o ambiente Microsoft e suporte a grandes volumes de dados.

## Referências

- [NoSQL Tutorial - Guru99](https://www.guru99.com/nosql-tutorial.html)
- [Comparação entre Bancos de Dados Relacionais e NoSQL - OpenClassrooms](https://openclassrooms.com/en/courses/5671741-design-the-logical-model-of-your-relational-database/6255746-compare-relational-and-nosql-databases)
- [Bancos de Dados NoSQL - FileCloud](https://www.filecloud.com/blog/2014/08/leading-nosql-databases-to-consider/)
