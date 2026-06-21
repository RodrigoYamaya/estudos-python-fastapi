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