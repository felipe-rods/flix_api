<h1 style="font-weight: bold;">Flix Api 💻</h1>

<p>
 <a href="#technologies">Tecnologias</a> • 
 <a href="#started">Iniciando</a> • 
 <a href="#routes">API Endpoints</a> •
 <a href="#contribute">Contribuições</a>
</p>

<b>O Flix Api é uma API desenvolvida em Django que permite realizar operações CRUD (Criar, Ler, Atualizar, Deletar) em um banco de dados de filmes. Além dos filmes, a API também gerencia informações sobre gêneros, atores e avaliações dos filmes, utilizando autenticação JWT.</b>

<h2>Funcionalidades</h2>

- Filmes: Permite adicionar, visualizar, editar e deletar filmes.

- Gêneros: Permite adicionar, visualizar, editar e deletar gêneros de filmes.

- Atores: Permite adicionar, visualizar, editar e deletar atores.

- Avaliações: Permite adicionar, visualizar, editar e deletar avaliações dos filmes.

- Autenticação JWT: Implementação de autenticação e autorização utilizando JSON Web Tokens.

<h2 id="technologies">💻 Tecnologias</h2>

- Python
- Django

<h2 id="started">🚀 Início</h2>

Para acessar o projeto, é necessário cloná-lo do repositório do Github, criar o ambiente virtual, ativá-lo e instalar as suas dependências nele.

<h2>Clonando</h2>

Vá para o terminal e clone o repositório do Github:

```bash
git clone https://github.com/felipe-rods/flix_api.git
```

<h2>Criando e ativando o ambiente virtual</h2>

No mesmo terminal, vá para a página do projeto, crie e ative o ambiente virtual:

```bash
cd pasta-do-projeto
python -m venv venv

source venv/bin/activate #ativar o ambiente virtual no Linux e macOS
./venv/Scripts/activate #ativar o ambiente virtual no Windows
```

<h2>Iniciando o projeto</h2>

Instale os requisitos do projeto:

```bash
pip install requirements.txt
```
Então, ative o servidor:

```bash
python manage.py runserver
```

<h2>Endereço Base</h2>

Para acessar a API, use o seguinte endereço base:

```
http://localhost:8000/api/v1/
```

<h2 id="routes">📍 API Endpoints</h2>

### Movies

- GET /movies/

- - Descrição: Retorna uma lista de filmes.

- GET /movies/{id}/

- - Descrição: Retorna os detalhes de um filme específico.

- POST /movies/

- - Descrição: Cria um novo filme.

- - Parâmetros:

```Json
{
  "titulo": "Nome do Filme",
  "genero": "Ação",
  "ano": 2025
}
```

<h2 id="get-auth-detail">GET /authenticate</h2>

**RESPONSE**
```json
{
  "name": "Fernanda Kipper",
  "age": 20,
  "email": "her-email@gmail.com"
}
```

<h2 id="post-auth-detail">POST /authenticate</h2>

**REQUEST**
```json
{
  "username": "fernandakipper",
  "password": "4444444"
}
```

**RESPONSE**
```json
{
  "token": "OwoMRHsaQwyAgVoc3OXmL1JhMVUYXGGBbCTK0GBgiYitwQwjf0gVoBmkbuyy0pSi"
}
```

<h2 id="contribute">📫 Contribuições</h2>

Agradecemos o seu interesse em contribuir! Siga estas etapas:

1. Faça um fork e clone o repositório:

```bash
git clone https://github.com/felipe-rods/flix_api.git
cd seu-projeto
```

2. Crie uma nova branch:

```bash
git checkout -b feature/NAME
```

3. Faça suas modificações e commits, seguindo um padrão:

```bash
git add .
git commit -m "Descrição do que foi alterado"
```

4. Envie para o Github:
```bash
git push origin nome-da-branch
```

5. Abra um Pull Request detalhando as suas modificações. Adicione uma captura de tela das mudanças e espere pela análise.

<h2>Documentações que podem ajudar</h2>

[📝 How to create a Pull Request](https://www.atlassian.com/br/git/tutorials/making-a-pull-request)

[💾 Commit pattern](https://gist.github.com/joshbuchea/6f47e86d2510bce28f8e7f42ae84c716)

<h2>Licensa</h2>

Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.
