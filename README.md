# Game Library

Bem-vindo ao repositório Game Library! Este projeto foi desenvolvido como parte do curso "Flask: avançando no desenvolvimento web com Python" da Alura.

## Descrição do Projeto

O Game Library é uma aplicação web em Flask que oferece funcionalidades básicas para cadastro, edição, remoção e listagem de jogos. Além disso, inclui um sistema de autenticação com login e senha do usuário.

## Pré-requisitos

Certifique-se de ter o Python instalado em sua máquina. Você pode instalá-lo [aqui](https://www.python.org/).

## Instalação

### 1. Clone o repositório:
```bash
git clone https://github.com/robertossoares/GameLibrary.git
```
### 2. Crie um ambiente virtual:
```bash
python -m venv venv
```
### 3. Ative o ambiente virtual:
No Windows:
```bash
venv\Scripts\activate
```
No Linux/macOS:
```bash
source venv/bin/activate
```
### 4. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Configuração

### Copie o arquivo de exemplo de configuração:
```bash
cp config.example.py config.py
```
Edite o arquivo config.py com as configurações apropriadas de chave secreta e banco de dados.

## Executando o aplicativo:

### Execute o seguinte comando para iniciar o servidor:
```bash
python gamelibrary.py
```
