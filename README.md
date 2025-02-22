<h1 align="center" style="font-weight: bold;">Flix Api 💻</h1>

<p align="center">
 <a href="#technologies">Tecnologias</a> • 
 <a href="#started">Início</a> • 
 <a href="#routes">API Endpoints</a> •
 <a href="#contribute">Contribuições</a>
</p>

<b>O Flix Api é uma API desenvolvida em Django que permite realizar operações CRUD (Criar, Ler, Atualizar, Deletar) em um banco de dados de filmes.</b>

<h3>Funcionalidades</h3>

- Filmes: permite adicionar, visualizar, editar e deletar filmes.

- Gêneros: permite adicionar, visualizar, editar e deletar gêneros de filmes.

- Atores: permite adicionar, visualizar, editar e deletar atores.

- Avaliações: permite adicionar, visualizar, editar e deletar avaliações dos filmes.

- Estatísticas: permite visualizar o número total de filmes, quantos de cada gênero e o total e a média de análises. 

- Autenticação JWT: Implementação de autenticação e autorização utilizando JSON Web Tokens.

<h2 id="technologies">💻 Tecnologias</h2>

- Python
- Django

<h2 id="started">🚀 Início</h2>

Para acessar o projeto, é necessário cloná-lo do repositório do Github, criar o ambiente virtual, ativá-lo e instalar as suas dependências nele.

<h3>Clonando o projeto</h3>

Vá para o terminal e clone o repositório do Github:

```bash
git clone https://github.com/felipe-rods/flix_api.git
```

<h3>Criando e ativando o ambiente virtual</h3>

No mesmo terminal, vá para a página do projeto, crie e ative o ambiente virtual:

```bash
cd pasta-do-projeto
python -m venv venv

source venv/bin/activate # Linux e macOS
./venv/Scripts/activate # Windows
```

<h3>Iniciando o projeto</h3>

Instale os requisitos do projeto:

```bash
pip install requirements.txt
```
Então, ative o servidor:

```bash
python manage.py runserver
```

<h3>Endereço Base</h3>

Para acessar a API, use o seguinte endereço base:

```
http://localhost:8000/api/v1/
```

<h2 id="routes">📍 API Endpoints</h2>

<h3>Movies</h3>

- GET `movies/`
  - Descrição: retorna uma lista de filmes.

- POST `movies/`
  - Descrição: cria um novo filme. Os campos "genre" e "actors" necessitam de gêneros e atores já cadastrados anteriormente. É possível selecionar mais de um ator.
  - Parâmetros:

  ```Json
  {
        "title": "Nome do filme",
        "genre": {
            "id": "id do gênero"
        },
        "actors": [
            {
                "id": "id do ator 1"
            },
            {
                "id": "id do ator 2"
            }
            {
                "id": "id do ator 3"
            }
        ],
        "release_date": "YYYY-MM-DD",
        "synopsis": "Sinopse do filme"
    }
  ```

- GET `movies/{id}/`
  - Descrição: retorna os detalhes de um filme específico.

- PUT `movies/{id}/`
  - Descrição: atualiza um filme existente.

- DELETE `movies/{id}/`
  - Descrição: exclui um filme existente.

<h3>Gêneros</h3>

- GET `genres/`
  - Descrição: retorna uma lista de gêneros.

- POST `genres/`
  - Descrição: cria um novo gênero.
  - Parâmetros:

  ```Json
  {
    "genre": "Ação"
  }
  ```

- GET `genres/{id}/`
  - Descrição: retorna os detalhes de um gênero específico.

- PUT `genres/{id}/`
  - Descrição: atualiza um gênero existente.

- DELETE `genres/{id}/`
  - Descrição: exclui um gênero existente.

<h3>Atores</h3>

- GET `actors/`
  - Descrição: retorna uma lista de atores.

- POST `actors/`
  - Descrição: cria um novo ator. O campo "country" aceita os países determinados na variável COUNTRY_CHOICES, dentro de actors/models.py.
  - Parâmetros:

  ```Json
  {
    "name": "Nome do ator",
    "birthday": "YYYY/MM/DD",
    "country": "País de origem"
  }
  ```

- GET `actors/{id}/`
  - Descrição: retorna os detalhes de um ator específico.

- PUT `actors/{id}/`
  - Descrição: atualiza um ator existente.

- DELETE `actors/{id}/`
  - Descrição: exclui um ator existente.

<h3>Avaliações</h3>

- GET `reviews/`
  - Descrição: retorna uma lista de avaliações.

- POST `reviews/`
  - Descrição: cria uma nova avaliação. É necessário que o filme avaliado já esteja cadastrado, para o campo "movie".
  - Parâmetros:

```Json
{
  "movie": "Nome do filme avaliado",
  "rating": "Número inteiro de 1 a 5",
  "comment": "Comentários sobre o filme"
}
```

- GET `reviews/{id}/`
  - Descrição: retorna os detalhes de uma avaliação específico.

- PUT `reviews/{id}/`
  - Descrição: atualiza uma avaliação existente.

- DELETE `reviews/{id}/`
  - Descrição: exclui uma avaliação existente.

<h3>Estatísticas</h3>

- GET `movies/stats`
  - Descrição: visualiza as estatísticas de total de filmes, quantos de cada gênero e total e média das análises.

<h3>Authentication</h3>

A API oferece autenticação baseada em tokens para garantir a segurança das operações. Abaixo estão os endpoints disponíveis para o gerenciamento de tokens:

- POST `authentication/token/`
  - Descrição: gera um novo token de acesso. É necessário fornecer as credenciais de login (nome de usuário e senha).

  ```Json
  {
    "username": "nome_de_usuário",
    "password": "sua_senha"
  }
  ```

  - Exemplo de resposta:

  ```Json
  {
    "refresh": "token_de_refresh",
    "access": "token_de_acesso"
  }
  ```

- POST `authentication/token/verify/`
  - Descrição: verifica a validade de um token de acesso. É necessário fornecer o token de acesso que se deseja verificar.


  ```Json
  {
    "token": "token_de_acesso"
  }
  ```

    - Exemplo de resposta:
      - Sucesso: o token é válido.
      - Erro: o token é inválido ou expirou.

- POST `authentication/token/refresh/`
  - Descrição: gera um novo token de acesso utilizando um token de refresh válido. É necessário um token de refresh válido.

  ```Json
  {
    "refresh": "token_de_refresh"
  }
  ```
  - Exemplo de resposta:

  ```Json
  {
    "access": "novo_token_de_acesso"
  }
  ```


<h2 id="contribute">📫 Contribuições</h2>

Agradecemos o seu interesse em contribuir! Siga estas etapas:

1. Faça um fork e clone o repositório:

```bash
git clone https://github.com/felipe-rods/flix_api.git
cd flix_api
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

<h3>Documentações que podem ajudar</h3>

[📝 How to create a Pull Request](https://www.atlassian.com/br/git/tutorials/making-a-pull-request)

[💾 Commit pattern](https://gist.github.com/joshbuchea/6f47e86d2510bce28f8e7f42ae84c716)

<h3>Licença</h3>

Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.
