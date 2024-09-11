
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
