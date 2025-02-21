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

<h3>Pré-requisitos</h3>

Aqui você lista todos os pré-requisitos para rodar o seu projeto. Por exemplo:
Here you list all prerequisites necessary for running your project. For example:

- [NodeJS](https://github.com/)
- [Git 2](https://github.com)

<h3>Clonando</h3>

Como clonar o seu projeto do github.
How to clone your project

```bash
git clone your-project-url-in-github
```

<h3>Configuração das variáveis .env</h2>

Use o `.env.example` como referência para criar o seu arquivo de configuração `.env` com as suas credenciais.
Use the `.env.example` as reference to create your configuration file `.env` with your AWS Credentials

```yaml
NODE_AWS_REGION=us-east-1
NODE_AWS_KEY_ID={YOUR_AWS_KEY_ID}
NODE_AWS_SECRET={YOUR_AWS_SECRET}
```

<h3>Iniciando o projeto</h3>

How to start your project

```bash
cd project-name
npm some-command-to-run
```

<h2 id="routes">📍 API Endpoints</h2>

Aqui você pode listar as principais rotas de sua API, e quais as respostas esperadas.
Here you can list the main routes of your API, and what are their expected request bodies.
​
| route                | description                                          
|----------------------|-----------------------------------------------------
| <kbd>GET /authenticate</kbd>     | retrieves user info see [response details](#get-auth-detail)
| <kbd>POST /authenticate</kbd>    | authenticate user into the api see [request details](#post-auth-detail)

<h3 id="get-auth-detail">GET /authenticate</h3>

**RESPONSE**
```json
{
  "name": "Fernanda Kipper",
  "age": 20,
  "email": "her-email@gmail.com"
}
```

<h3 id="post-auth-detail">POST /authenticate</h3>

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

Aqui você vai explicar como outros desenvolvedores podem contribuir com o seu projeto. Por exemplo, explicando como podem criar suas branches, quais padrões seguirem e como abrirem um pull request.
Here you will explain how other developers can contribute to your project. For example, explaining how can create their branches, which patterns to follow and how to open an pull request

1. `git clone https://github.com/Fernanda-Kipper/text-editor.git`
2. `git checkout -b feature/NAME`
3. Follow commit patterns
4. Open a Pull Request explaining the problem solved or feature made, if exists, append screenshot of visual modifications and wait for the review!

<h3>Documentações que podem ajudar</h3>

[📝 How to create a Pull Request](https://www.atlassian.com/br/git/tutorials/making-a-pull-request)

[💾 Commit pattern](https://gist.github.com/joshbuchea/6f47e86d2510bce28f8e7f42ae84c716)

<h3>Licensa</h3>

Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.
