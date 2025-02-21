<<<<<<< HEAD
<h1 align="center" style="font-weight: bold;">Flix Api 💻</h1>

<p align="center">
 <a href="#tech">Tecnologias</a> • 
 <a href="#started">Iniciando</a> • 
 <a href="#routes">API Endpoints</a> •
 <a href="#contribute">Contribuições</a>
</p>

<p align="center">
    <b>Descrição simples do que o seu projeto faz ou como usá-lo.</b>
</p>

<h2 id="technologies">💻 Tecnologias</h2>

- Lista de todas as tecnologias que você usou
=======
<h1 align="center" style="font-weight: bold;">Project name 💻</h1>

<p align="center">
 <a href="#tech">Technologies</a> • 
 <a href="#started">Getting Started</a> • 
  <a href="#routes">API Endpoints</a> •
 <a href="#colab">Collaborators</a> •
 <a href="#contribute">Contribute</a>
</p>

<p align="center">
    <b>Simple description of what your project do or how to use it.</b>
</p>

<h2 id="technologies">💻 Technologies</h2>

>>>>>>> 5530a4dacf95f05154df5b1450ec8ea0f7ba4606
- list of all technologies you used
- Java
- MongoDB
- NodeJS

<<<<<<< HEAD
<h2 id="started">🚀 Início</h2>

Aqui você descreve como rodar o seu projeto localmente.
Here you describe how to run your project locally.

<h3>Pré-requisitos</h3>

Aqui você lista todos os pré-requisitos para rodar o seu projeto. Por exemplo:
=======
<h2 id="started">🚀 Getting started</h2>

Here you describe how to run your project locally

<h3>Prerequisites</h3>

>>>>>>> 5530a4dacf95f05154df5b1450ec8ea0f7ba4606
Here you list all prerequisites necessary for running your project. For example:

- [NodeJS](https://github.com/)
- [Git 2](https://github.com)

<<<<<<< HEAD
<h3>Clonando</h3>

Como clonar o seu projeto do github.
=======
<h3>Cloning</h3>

>>>>>>> 5530a4dacf95f05154df5b1450ec8ea0f7ba4606
How to clone your project

```bash
git clone your-project-url-in-github
```

<<<<<<< HEAD
<h3>Configuração das variáveis .env</h2>

Use o `.env.example` como referência para criar o seu arquivo de configuração `.env` com as suas credenciais.
=======
<h3>Config .env variables</h2>

>>>>>>> 5530a4dacf95f05154df5b1450ec8ea0f7ba4606
Use the `.env.example` as reference to create your configuration file `.env` with your AWS Credentials

```yaml
NODE_AWS_REGION=us-east-1
NODE_AWS_KEY_ID={YOUR_AWS_KEY_ID}
NODE_AWS_SECRET={YOUR_AWS_SECRET}
```

<<<<<<< HEAD
<h3>Iniciando o projeto</h3>
=======
<h3>Starting</h3>
>>>>>>> 5530a4dacf95f05154df5b1450ec8ea0f7ba4606

How to start your project

```bash
cd project-name
npm some-command-to-run
```

<h2 id="routes">📍 API Endpoints</h2>

<<<<<<< HEAD
Aqui você pode listar as principais rotas de sua API, e quais as respostas esperadas.
Here you can list the main routes of your API, and what are their expected request bodies.
​
| route                | description                                          
|----------------------|-----------------------------------------------------
| <kbd>GET /authenticate</kbd>     | retrieves user info see [response details](#get-auth-detail)
| <kbd>POST /authenticate</kbd>    | authenticate user into the api see [request details](#post-auth-detail)
=======
Here you can list the main routes of your API, and what are their expected request bodies.
​
| route               | description                                          
|----------------------|-----------------------------------------------------
| <kbd>GET /authenticate</kbd>     | retrieves user info see [response details](#get-auth-detail)
| <kbd>POST /authenticate</kbd>     | authenticate user into the api see [request details](#post-auth-detail)
>>>>>>> 5530a4dacf95f05154df5b1450ec8ea0f7ba4606

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

<<<<<<< HEAD
<h2 id="colab">🤝 Colaboradores</h2>

Agradecimento especial para todos vocês que contribuíram com este projeto.
=======
<h2 id="colab">🤝 Collaborators</h2>

>>>>>>> 5530a4dacf95f05154df5b1450ec8ea0f7ba4606
Special thank you for all people that contributed for this project.

<table>
  <tr>
    <td align="center">
      <a href="#">
        <img src="https://avatars.githubusercontent.com/u/61896274?v=4" width="100px;" alt="Fernanda Kipper Profile Picture"/><br>
        <sub>
          <b>Fernanda Kipper</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="#">
        <img src="https://t.ctcdn.com.br/n7eZ74KAcU3iYwnQ89-ul9txVxc=/400x400/smart/filters:format(webp)/i490769.jpeg" width="100px;" alt="Elon Musk Picture"/><br>
        <sub>
          <b>Elon Musk</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="#">
        <img src="https://miro.medium.com/max/360/0*1SkS3mSorArvY9kS.jpg" width="100px;" alt="Foto do Steve Jobs"/><br>
        <sub>
          <b>Steve Jobs</b>
        </sub>
      </a>
    </td>
  </tr>
</table>

<<<<<<< HEAD
<h2 id="contribute">📫 Contribuições</h2>

Aqui você vai explicar como outros desenvolvedores podem contribuir com o seu projeto. Por exemplo, explicando como podem criar suas branches, quais padrões seguirem e como abrirem um pull request.
=======
<h2 id="contribute">📫 Contribute</h2>

>>>>>>> 5530a4dacf95f05154df5b1450ec8ea0f7ba4606
Here you will explain how other developers can contribute to your project. For example, explaining how can create their branches, which patterns to follow and how to open an pull request

1. `git clone https://github.com/Fernanda-Kipper/text-editor.git`
2. `git checkout -b feature/NAME`
3. Follow commit patterns
4. Open a Pull Request explaining the problem solved or feature made, if exists, append screenshot of visual modifications and wait for the review!

<<<<<<< HEAD
<h3>Documentações que podem ajudar</h3>
=======
<h3>Documentations that might help</h3>
>>>>>>> 5530a4dacf95f05154df5b1450ec8ea0f7ba4606

[📝 How to create a Pull Request](https://www.atlassian.com/br/git/tutorials/making-a-pull-request)

[💾 Commit pattern](https://gist.github.com/joshbuchea/6f47e86d2510bce28f8e7f42ae84c716)
<<<<<<< HEAD

<h3>Licensa</h3>
=======
>>>>>>> 5530a4dacf95f05154df5b1450ec8ea0f7ba4606
