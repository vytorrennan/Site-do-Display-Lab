# Site-do-Display-Lab
Website oficial do laboratório Display do Instituto Federal do Norte de Minas Gerais - Campus Januária

# Criação do ambiente virtual

Passo a passo para criar o ambiente virtual caso vc não tenha ainda na sua máquina.

## Passo 1

No terminal digite: `python3 -m venv .venv`

## Passo 2

No terminal digite: `source .venv/bin/activate`

## Passo 3

No terminal digite: `pip install -r requirements.txt`

# Atualização do ambiente virtual

# Caso 1

Caso você precise instalar uma nova biblioteca no ambiente virtual é só rodar 
os seguintes comandos(vale ressaltar que você deve estar dentro do ambiente 
virtual `source .venv/bin/activate`):

Instalar uma nova biblioteca. `pip install {nome_da_biblioteca}`

Atualizar o arquivo `requirements.txt`: `pip freeze > requiriments.txt`

# Caso 2

Caso alguém da equipe tenha atualizado o ambiente virtual, você deve atualizar o repositório em
sua máquina com o comando: `git pull origin {nome_da_branch}`, e depois executar os seguintes 
comandos `source .venv/bin/activate` para ativar o ambiente virtual e o
`pip install -r requirements.txt` para atualizar o ambiente virtual

# Para executar a aplicação

Para executar a aplicação você deve entrar no terminal e ir para o diretório onde se encontra o 
arquivo `app.py`, e executar os sequintes comandos `source .venv/bin/activate` e para rodar a 
aplicação `python3 app.py` que ele já executa a aplicação em rede.

Vale ressaltar que o comando `python3 app.py` é o que roda no sistema operacional linux caso você 
use outro sistema operacional execute pelo comando apropriado para o seu sistema





