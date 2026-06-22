# estudos-python-fastapi

O que é o venv?
Significa "Virtual Environment" (Ambiente Virtual). É uma ferramenta nativa do Python utilizada para criar espaços isolados para cada projeto.

Quando instalamos bibliotecas no nosso código, o "venv" garante que essas dependências fiquem restritas à pasta do projeto, impedindo que elas sejam instaladas no sistema operacional (Windows, por exemplo). Usamos o venv justamente para manter a máquina limpa e evitar que projetos diferentes entrem em conflito.


O que e .env?
 O arquivo .env ele e basicamente como se fosse um cofre local. Onde armazenaremos as configurações e dados sensiveis de projeto que nao deve ser mostrado. exemplo: Credenciais de banco de dados (usuário, senha, host, porta),  Chaves de API secretas (como chaves de pagamento ou mapas).

exemplo: DB_HOST=localhost
DB_USER=root
DB_PASSWORD=minha_senha_secreta_123
DB_NAME=meu_banco_de_dados
API_KEY=9a8b7c6d5e4f3g2h1i
PORT=3000

Curiosidades:

# Java/Spring Boot ➔ Python/FastAPI

| Conceito / Responsabilidade | Ecossistema Java (Spring Boot) | Ecossistema Python (FastAPI) |
| :--- | :--- | :--- |
| **O Framework Web** | Spring Boot | FastAPI |
| **Validação de Entrada e Saída** | DTOs + Bean Validation (`@NotNull`) | **Pydantic** (`BaseModel`) |
| **Mapeamento de Tabelas (ORM)** | Hibernate / JPA (`@Entity`, `@Table`) | **SQLAlchemy** (`Base`, `Column`) |
| **Operações de Banco (CRUD)** | `JpaRepository` (Spring Data JPA) | `Session` do SQLAlchemy (`db.query()`) |
| **Controladores e Rotas** | `@RestController`, `@PostMapping` | `APIRouter`, `@router.post()` |
| **Migrações de Banco** | Flyway ou Liquibase | Alembic |
| **Injeção de Dependências** | `@Autowired` | `Depends()` |

---        

### 1. Pydantic ➔ Eo  DTO "Turbinado"
No Java, quando o cliente envia um JSON pelo "Postman", você cria uma classe DTO (ou um `record`) e enche de anotações como `@NotBlank`, `@Min(18)` e usa o `@Valid` no Controller. O Jackson faz a conversão de JSON para Objeto.

No FastAPI, o **Pydantic** faz o papel do DTO e da validação ao mesmo tempo. 
* Ele pega o JSON que chega da web, olha para a sua classe `BaseModel` e converte automaticamente para um objeto Python.
* Se alguém enviar uma `String` no lugar de um `Integer`, o Pydantic bloqueia a requisição na porta e devolve um erro `422 Unprocessable Entity` de forma automática, sem a requisição sequer chegar na lógica do seu sistema. 

### 2. SQLAlchemy ➔ O seu Hibernate
No Spring, o Hibernate pega uma classe sua, lê a anotação `@Entity` e entende: "Ok, isso aqui é uma tabela no banco de dados".

No Python, o **SQLAlchemy** é o ORM (Object-Relational Mapper) dominante do mercado. 
* Em vez de anotações `@Entity`, você faz a sua classe herdar de uma classe `Base`.
* Em vez de `@Id` e `@Column(name="nome")`, você escreve `id = Column(Integer, primary_key=True)`.
* A maior diferença estrutural é na hora de buscar os dados. O Spring tem a magia do `JpaRepository` que te dá um `findById()` de graça. No SQLAlchemy, você escreve a query de forma um pouco mais explícita usando a Sessão do banco, como: `db.query(PetModel).filter(PetModel.id == 1).first()`. É um pouco mais manual, mas te dá um controle absurdo sobre a performance.

### 3. APIRouter ➔ O seu @RestController
No Spring Boot, você cria uma classe com `@RestController` e coloca `@RequestMapping("/pets")` para agrupar as rotas.
No FastAPI, usamos o `APIRouter`. Você cria um arquivo separado e escreve `@router.post("/pets")`. Depois, você "pluga" esse router no arquivo `main.py`. A lógica de separação de responsabilidades é rigorosamente a mesma.


PASSO A PASSO DO PROJETO?
1) vamos criar .env variaveis de ambiente de configuração para dados sensiveis.Não obrigatorio,mas e uma boa pratica.

2) Passo vamos criar a conexão com banco de dados;
O pacote database?
 - A classe database.py: E a famosa classe engessada e puramente "control C + Control V" E Puramente para a conexão do banco de dados.Trazendo a realidade do java/Spring Boot, Aqui seria semelhante la so que unica diferença que essa parte da conexão o Spring ja cria automaticamente lendo o application.properties, e não no extends JpaRepository (que serve so para operações de crud). Aqui e tudo manualmente feito como no java legado.

3) passo vamos criar a tabela que vai representar no banco de dados;
   - O pacote models que vai constar a classe pet_model.py que vai representar a tabela no banco de dados,Diferente no java usavamos anotação @Entity que vai indicar que a classe e no representção da tabela no banco de dados. Ja aqui no python usamos herança de classes. O "SQLAlchemy"("hibernate) lê essa classe e entende exatamente como moldar a tabela física dentro da base de dados crud_python no MySQL que nos criamos.


Obs: 

### O que faz o `from_attributes = True` no Pydantic?

No ecossistema Java/Spring, uma Entidade (`@Entity`) e um DTO são objetos completamente isolados. Para transferir os dados da Entidade (que veio do banco) para o DTO (que vai para a web), precisamos de um "tradutor". Geralmente, resolvemos isso criando uma interface extra com o `@Mapper` (via MapStruct) para copiar os dados de um lado para o outro.

No Python com FastAPI, **não criamos essa interface extra de conversão**. Nós resolvemos isso usando a configuração `from_attributes = True` (antigo `orm_mode`) diretamente dentro da classe DTO (o Schema).

**Em resumo (O Paralelo):**
Essa configuração é o nosso `@Mapper` embutido. Ela dá a permissão de conversão e avisa o Pydantic: *"Atenção, o objeto que vai chegar aqui não é um JSON padrão. É uma classe pesada que veio do banco de dados (SQLAlchemy). Você está autorizado a 'sugar' os dados lendo os atributos desta classe diretamente."*


4) passo vamos criar o equivalente aos DTOS RESPONSE E REQUEST NO JAVA que classe validar entrada e saida dos dados.Observação Que otima boa pratica jamais expor a classe que criou o banco de dados,usamos Dtos filtrar o que deve ser exposto entrada dados e saida; Pacote Schemas que seria O DTO(CLASSE Records no java)

Exemplo: vamos criar uma class response e request igual no java;

Apos isso iremos main.py e colocar esse comandos e iniciar servidor : 

# OBS: Você precisa importar a Model para o SQLAlchemy "enxergar" a classe, No Spring era so inicar servidor
from models.pet_model import PetModel

# Agora sim, quando ele rodar esta linha, ele já sabe que a classe PetModel existe
Base.metadata.create_all(bind=engine)


