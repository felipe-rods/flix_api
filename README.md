<h1 align="center" style="font-weight: bold;">Flix Api 💻</h1>

<p align="center">
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

Aqui você descreve como rodar o seu projeto localmente.
Here you describe how to run your project locally.

<h2>Clonando</h2>

```bash
git clone https://github.com/felipe-rods/flix_api.git
```

<h2>Iniciando o projeto</h2>

Primeiramente, instale os requisitos:

```bash
pip install requirements.txt
```
Então, ative o servidor:

```bash
cd project-name
python manage.py runserver
```

<h2 id="routes">📍 API Endpoints</h2>

​
| route                | description                                          
|----------------------|-----------------------------------------------------
| <kbd>GET /authenticate</kbd>     | retrieves user info see [response details](#get-auth-detail)
| <kbd>POST /authenticate</kbd>    | authenticate user into the api see [request details](#post-auth-detail)

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
