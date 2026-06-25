# 1. Python (A Base Completa) - Com Exemplos

# 🔹 Fundamentos

# **Variáveis e tipos**
Em Python, você não precisa declarar o tipo (como `int x = 10` no Java). A tipagem é dinâmica.

Python

```python
**nome = "Rodrigo"      # str (String)
idade = 22            # int (Inteiro)
peso = 65.5           # float (Decimal)
is_estudante = True   # bool (Booleano)**
```

**Condicionais e Operadores (O detalhe da "Truthiness")**
**A avaliação de condições lógicas no Python tem particularidades importantes. Qualquer número diferente de zero é considerado verdadeiro.**

Python

```python
**numero = -1

# Em Python, -1 é avaliado como True. O código abaixo VAI imprimir a mensagem.
if numero:
    print("O número -1 é considerado verdadeiro (True) em condições lógicas!")
elif numero == 0:
    print("Zero é False.")
else:
    print("Outros casos.")**
```

# **Laços (for, while)**
O `for` no Python é como o `foreach` do Java. Ele iterage diretamente sobre os itens.

Python

```python
# Iterando uma lista (for)
pets = ["Cachorro", "Gato", "Papagaio"]
for pet in pets:
    print(f"Eu tenho um {pet}")

# Laço com contador (while)
contador = 0
while contador < 3:
    print(f"Processando item {contador}...")
    contador += 1
```

# 🔹 Estruturas de Dados

**Listas (Mutáveis)**
Equivalente a um `ArrayList`. Podem ser alteradas a qualquer momento.

Python

```python
tecnologias = ["Java", "Spring"]
tecnologias.append("Python") # Adiciona no final
tecnologias.remove("Java")   # Remove um item
```

**Tuplas (Imutáveis)**
Uma vez criadas, **não podem** ser alteradas. Excelentes para dados fixos (ex: configurações).

Python

```python
coordenadas_rj = (-22.9068, -43.1729)
# coordenadas_rj[0] = -23.0 -> Isso geraria um ERRO!
```

**Dicionários (Chave: Valor)**
O formato mais importante para APIs. É o equivalente perfeito do `HashMap` ou de um JSON.

Python

```python
usuario = {
    "nome": "Rodrigo",
    "stack": "Backend",
    "periodo": 6
}
print(usuario["stack"]) # Imprime: Backend
```

**List Comprehension (A Mágica do Python)**
Cria listas aplicando regras em uma única linha. Super performático.

Python

```python
**numeros = [1, 2, 3, 4, 5]
# Cria uma nova lista apenas com os números pares
pares = [x for x in numeros if x % 2 == 0]**
```

### 🔹 Funções

**Definição, Parâmetros e Retorno**
Usamos `def`. É boa prática usar *Type Hints* (dicas de tipo) para ajudar a IDE, mesmo a tipagem sendo dinâmica.

Python

```
def somar_numeros(a: int, b: int) -> int:
    return a + b

resultado = somar_numeros(10, 5)
```

**Flexibilidade com `*args` e `kwargs`**
Para quando você não sabe quantos parâmetros a função vai receber.

Python

```
# *args recebe múltiplos valores como uma Tupla
def listar_tecnologias(*args):
    print(args)

listar_tecnologias("Java", "Python", "Docker")

# **kwargs recebe chaves e valores como um Dicionário
def criar_perfil(**kwargs):
    print(kwargs)

criar_perfil(nome="Rodrigo", linguagem="Python", framework="FastAPI")
```

# **🔹 Orientação a Objetos (POO)**

#### **Classes, Construtor (`__init__`) e Encapsulamento**
**O `self` é obrigatório nos métodos e equivale ao `this` do Java. Para atributos privados, usamos `__`.**

Python

```python
class ContaBancaria:
    def __init__(self, titular):
        self.titular = titular       # Atributo público
        self.__saldo = 0.0           # Atributo privado (Encapsulado)

    def depositar(self, valor):
        self.__saldo += valor
```

#### **Herança e Sobrescrita de Métodos (Override)**
Como o comportamento de uma classe mãe é modificado na classe filha.

Python

```python
class ClasseA:
    def mostrar_mensagem(self):
        return "TestA"

class ClasseB(ClasseA):
    # Sobrescreve o método da classe pai
    def mostrar_mensagem(self):
        return "TestB"

obj = ClasseB()
# A chamada vai priorizar o método sobrescrito na classe filha
print(obj.mostrar_mensagem()) # Saída: TestB
```

# **🔹 Manipulação de Arquivos e JSON**

**Escrita e Leitura (Modos `w` e `r`)
O comando `with` garante que o arquivo seja fechado automaticamente após o uso.**

Python

```python
# Escrevendo em um arquivo de texto
with open("log.txt", "w") as arquivo:
    arquivo.write("Sistema iniciado com sucesso.")

# Lendo um arquivo de texto
with open("log.txt", "r") as arquivo:
    conteudo = arquivo.read()
```

# **Lidando com JSON**

Python

```python
import json

# Convertendo um dicionário Python para String JSON (para enviar pra web)
dados = {"status": "ok", "codigo": 200}
json_string = json.dumps(dados)

# Convertendo uma String JSON para Dicionário Python (para o backend processar)
json_recebido = '{"nome": "API", "versao": "1.0"}'
dict_python = json.loads(json_recebido)
```

# **🔹 Tratamento de Exceções**

#### **Blocos try / except / finally**
**Impede que a aplicação caia (crash) quando algo der errado.**

Python

```python
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero!")
except Exception as e:
    print(f"Um erro inesperado ocorreu: {e}")
finally:
    print("Essa linha sempre executa, dando erro ou não (ótimo para fechar conexões).")
```

```markdown
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

# 🗺️ O Grande Mapa: Java/Spring Boot ➔ Python/FastAPI

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

### 1. Pydantic ➔ O seu DTO "Turbinado"
No Java, quando o cliente envia um JSON pelo Insomnia/Postman, você cria uma classe DTO (ou um `record` moderno) e enche de anotações como `@NotBlank`, `@Min(18)` e usa o `@Valid` no Controller. O Jackson faz a conversão de JSON para Objeto.

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
```

# Construindo uma API com FastAPI: Do Zero ao Banco de Dados

## 🛠️ 1. O Ambiente de Trabalho (Preparação)

Antes de escrever qualquer código em Python, precisamos preparar o terreno para não bagunçar o nosso computador.

### O que é o `venv`?

Significa **"Virtual Environment" (Ambiente Virtual)**. É uma ferramenta nativa do Python utilizada para criar espaços isolados para cada projeto.

- **O Problema:** Se você instalar o FastAPI diretamente no seu Windows/Mac, ele vai ficar lá para sempre. Se amanhã você criar outro projeto que precisa de uma versão mais antiga, vai dar conflito.
- **A Solução:** O `venv` cria uma "bolha". Quando instalamos bibliotecas, elas ficam restritas à pasta do projeto atual, mantendo o seu sistema operacional limpo.

### O que é o `.env`?

O arquivo `.env` é o **cofre local do seu projeto**. É onde armazenamos as configurações e dados sensíveis que jamais devem ir para o GitHub.

- **Exemplos:** Credenciais de banco de dados (usuário, senha, host), Chaves de API secretas, etc.

Snippet de código

```
# Exemplo de arquivo .env na raiz do projeto
DB_USER=root
DB_PASSWORD=minha_senha_secreta_123
DB_HOST=localhost
DB_NAME=crud_python
```

## ☕Curiosidade: Java/Spring Boot ➔ Python/FastAPI

Se você vem do mundo Java, o ecossistema Python tem correspondentes exatos para tudo o que você já conhece:

| **Conceito / Responsabilidade** | **Ecossistema Java (Spring Boot)** | **Ecossistema Python (FastAPI)** |
| --- | --- | --- |
| **O Framework Web** | Spring Boot | **FastAPI** |
| **Validação de Entrada e Saída** | DTOs + Bean Validation (`@NotNull`) | **Pydantic** (`BaseModel`) |
| **Mapeamento de Tabelas (ORM)** | Hibernate / JPA (`@Entity`, `@Table`) | **SQLAlchemy** (`Base`, `Column`) |
| **Operações de Banco (CRUD)** | `JpaRepository` | `Session` do SQLAlchemy (`db.query()`) |
| **Controladores e Rotas** | `@RestController`, `@PostMapping` | `APIRouter`, `@router.post()` |
| **Injeção de Dependências** | `@Autowired` | `Depends()` |

## 🏗️ O Passo a Passo do Projeto (Arquitetura em Camadas)

Para criar uma API profissional, não jogamos tudo em um arquivo só. Dividimos o projeto em responsabilidades claras.

### Passo 1: A Conexão com o Banco de Dados (`database.py`)

No Java, o Spring lê o `application.properties` e cria a conexão sozinho. No Python (com SQLAlchemy), nós configuramos isso manualmente. É um arquivo de configuração ("Control C + Control V") que ensina o sistema a conversar com o MySQL.

- **Onde fica:** Pasta `database/database.py`

### Passo 2: Criando a Tabela no Banco (`models`)

No Java, você usaria `@Entity`. No Python, usamos **Herança de Classes**. O SQLAlchemy lê essa classe e entende exatamente como moldar a tabela física dentro do MySQL.

Python

```python
**# models/pet_model.py
from sqlalchemy import Column, Integer, String, Float, Boolean
from database.database import Base

class PetModel(Base):
    __tablename__ = "tb_pets"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(50), nullable=False)
    especie = Column(String(50), nullable=False)
    idade = Column(Integer)**
```

**⚠️ Passo Crucial no `main.py`:**

Para que o banco de dados seja criado de fato quando você rodar o servidor, você precisa importar o `PetModel` no seu `main.py` e avisar o motor do banco:

Python

```python
# main.py
from fastapi import FastAPI
from database.database import engine, Base

# OBS: Você PRECISA importar a Model para o SQLAlchemy "enxergar" a classe
from models.pet_model import PetModel

# Agora sim, ele lê a classe PetModel e cria a tabela no MySQL
Base.metadata.create_all(bind=engine)

app = FastAPI()
```

### Passo 3: Os Filtros de Entrada e Saída (`schemas` / Pydantic)

**Jamais exponha a sua classe de Banco de Dados (`PetModel`) diretamente para a internet.** Nós criamos os Schemas (os famosos DTOs / Records no Java) para ditar as regras do que pode entrar e do que pode sair.

Python

```python
**# schemas/pet_schema.py
from pydantic import BaseModel
from typing import Optional

# DTO de Entrada (O que o usuário envia no POST)
class PetRequestSchema(BaseModel):
    nome: str
    especie: str
    idade: int

# DTO de Saída (O que o sistema devolve, agora com ID)
class PetResponseSchema(BaseModel):
    id: int
    nome: str
    especie: str
    idade: int

    class Config:
        from_attributes = True**
```

💡 **O que faz o `from_attributes = True`?**

No Java, para copiar dados do Banco (`@Entity`) para a Web (DTO), você precisa de um "tradutor" (como o MapStruct / `@Mapper`).

No FastAPI, essa única linha resolve tudo! Ela avisa o Pydantic: *"Atenção, o objeto que vai chegar aqui é pesado e veio do banco de dados (SQLAlchemy). Você está autorizado a ler os atributos dessa classe automaticamente e converter em JSON"*.

### Passo 4: O Repository (As Operações de Banco)

Aqui não existe `JpaRepository` com mágica automática. Nós criamos as funções que vão inserir, buscar e deletar usando a Sessão (`db`) do SQLAlchemy.

**O Desafio do Mapeamento e o Poder do `model_dump()`:**

O SQLAlchemy não sabe o que é um Objeto do Pydantic (Schema). Precisamos traduzir.

**A Jornada Completa do Dado:**

1. **JSON (Texto):** O Postman envia `{"nome": "Rex", "idade": 3}`.
2. **Pydantic (Objeto):** O FastAPI converte esse texto no `PetRequestSchema` (valida se a idade é realmente número).
3. **Dicionário (HashMap):** Usamos o `model_dump()`. Ele rebaixa o objeto Pydantic para um Dicionário nativo do Python (idêntico a um HashMap).
4. **Desempacotamento ():** O Python injeta esse dicionário direto na Entidade do Banco (`PetModel`) e salva!

Python

```python
# repositories/pet_repository.py
from sqlalchemy.orm import Session
from models.pet_model import PetModel
from schemas.pet_schema import PetRequestSchema

def salvar_pet(db: Session, pet_dto: PetRequestSchema):
    # 1. model_dump() transforma o DTO em dicionário
    # 2. Os ** desempacotam o dicionário para dentro da Entidade
    novo_pet = PetModel(**pet_dto.model_dump())

    db.add(novo_pet)
    db.commit()
    db.refresh(novo_pet)
    return novo_pet
```

### Passo 5: O Service (O Cérebro da Operação)

O Repository é "burro" (só salva e deleta). O Router (Controlador) também é burro (só recebe internet). É o **Service** que aplica as regras de negócio e lança os Erros.

Python

```python
**# services/pet_service.py
from fastapi import HTTPException
from sqlalchemy.orm import Session
import repositories.pet_repository as pet_repo

def buscar_pet_por_id(db: Session, pet_id: int):
    pet = pet_repo.buscar_pet_por_id(db, pet_id)

    # Regra de Negócio: Se o banco não achar nada, estoure um erro HTTP 404!
    if not pet:
        raise HTTPException(status_code=404, detail="Pet não encontrado no sistema.")

    return pet**
```

### Passo 6: O Router / Controller (A Porta de Entrada)

É o equivalente ao `@RestController` do Java. Ele gerencia os Endpoints (`GET`, `POST`, `PUT`, `DELETE`). Seu único trabalho é receber a requisição e passar para o Service resolver.

Python

```python
**# routers/pet_router.py
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from database.database import get_db
from schemas.pet_schema import PetRequestSchema, PetResponseSchema
import services.pet_service as pet_service

router = APIRouter(prefix="/pets", tags=["Pets"])

# Equivalente ao @PostMapping do Java
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=PetResponseSchema)
def criar_pet(pet_dto: PetRequestSchema, db: Session = Depends(get_db)):
    # Recebe o JSON (pet_dto) e a conexão com o banco (db)
    return pet_service.criar_pet(db, pet_dto)**
```