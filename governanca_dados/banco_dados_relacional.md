
## Banco de Dados Relacional

Os Bancos de Dados Relacionais (RDBMS) são projetados para armazenar dados de forma estruturada em tabelas, seguindo o modelo relacional. Esses bancos de dados utilizam a linguagem SQL (Structured Query Language) para manipulação e consulta dos dados.

### Elementos Básicos
- **Relações (Tabelas):** Estruturas que armazenam dados em formato de linhas e colunas.
- **Registros (Tuplas):** Cada linha de uma tabela que representa uma instância de dados.

### Características Fundamentais
- **Restrições de Integridade:** Regras que garantem a precisão e consistência dos dados. Exemplos incluem:
  - **PK (Primary Key):** Identificador único para cada registro na tabela.
  - **FK (Foreign Key):** Chave que estabelece uma relação entre tabelas.
  - **UK (Unique Key):** Garante que todos os valores em uma coluna sejam únicos.
  - **CK (Check Key):** Restrições que validam dados inseridos.
  - **NN (Not Null):** Garante que uma coluna não possa ter valores nulos.

### Exemplos

```sql
CREATE TABLE Clientes (
    ClienteID INT PRIMARY KEY,
    Nome VARCHAR(100),
    Email VARCHAR(100)
);

CREATE TABLE Pedidos (
    PedidoID INT PRIMARY KEY,
    ClienteID INT,
    Data DATE,
    FOREIGN KEY (ClienteID) REFERENCES Clientes(ClienteID)
);
```

# Documentação de Modelos de Dados

## Modelo Conceitual

### Descrição

O Modelo Conceitual é uma representação de alto nível de um sistema de banco de dados, focado na estrutura das entidades e seus relacionamentos. É uma visão independente da tecnologia e do sistema de gerenciamento de banco de dados (DBMS) usado. O objetivo principal é definir os requisitos e o escopo do banco de dados.

### Componentes Principais

- **Entidades**: Representam objetos ou conceitos do mundo real que têm uma existência independente e são importantes para o sistema.
- **Relacionamentos**: Mostram como as entidades estão relacionadas entre si.
- **Atributos**: Características ou propriedades das entidades.

### Benefícios

- Facilita a comunicação entre analistas, designers e usuários finais.
- Ajuda a identificar os requisitos e definir o escopo do banco de dados.

### Referência

Para mais informações, consulte [Modelo Conceitual - Visual Paradigm](https://www.visual-paradigm.com/support/documents/vpuserguide/3563/3564/85378_conceptual,l.html).

## Modelo Lógico

### Descrição

O Modelo Lógico é uma representação detalhada das entidades e relacionamentos identificados no Modelo Conceitual. Ele traduz o modelo conceitual em uma estrutura mais específica, que é independente da tecnologia de banco de dados, mas inclui detalhes suficientes para a criação de um modelo físico.

### Componentes Principais

- **Entidades**: Definidas com mais detalhes, incluindo tipos de dados e restrições.
- **Relacionamentos**: Definidos com cardinalidade e outras propriedades.
- **Atributos**: Especificados com detalhes sobre tipos e formatos.

### Benefícios

- Oferece uma visão mais detalhada das estruturas de dados.
- Serve como um guia para o desenvolvimento do Modelo Físico.

### Referência

Para mais informações, consulte [Modelo Lógico - Visual Paradigm](https://www.visual-paradigm.com/support/documents/vpuserguide/3563/3564/85378_conceptual,l.html).

## Modelo Físico

### Descrição

O Modelo Físico é a implementação detalhada do Modelo Lógico em um sistema de gerenciamento de banco de dados específico. Ele descreve como os dados serão armazenados, acessados e gerenciados no banco de dados físico.

### Componentes Principais

- **Tabelas**: Representam as entidades do Modelo Lógico como tabelas em um banco de dados.
- **Colunas**: Definem os atributos das tabelas, incluindo tipos de dados e restrições.
- **Índices**: Usados para melhorar o desempenho das consultas.
- **Chaves**: Incluem chaves primárias e estrangeiras para garantir integridade referencial.

### Benefícios

- Fornece uma especificação clara e detalhada para a implementação no DBMS.
- Inclui otimizações para melhorar o desempenho e garantir a integridade dos dados.

### Referência

Para mais informações, consulte [Modelo Físico - Visual Paradigm](https://www.visual-paradigm.com/support/documents/vpuserguide/3563/3564/85378_conceptual,l.html).
