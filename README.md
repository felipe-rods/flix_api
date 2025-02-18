# Flix-Api

## Descrição
Flix-Api é uma API Restful que faz o CRUD de filmes, gêneros, atores e reviews, utilizando Python e Django Rest Framework.

## Instalação

1. Clone o repositório:
    ```sh
    git clone https://github.com/seu-usuario/flix-api.git
    cd flix-api
    ```

2. Crie um ambiente virtual e ative-o:
    ```sh
    python -m venv venv
    source venv/bin/activate  # Para Linux/Mac
    ./venv/Scripts/activate  # Para Windows
    ```

3. Instale as dependências a partir do arquivo `requirements.txt`:
    ```sh
    pip install -r requirements.txt
    ```

## Uso

Para rodar a aplicação, use o comando:
```sh
python manage.py runserver
```

A aplicação estará disponível no endereço `localhost:8000/api/v1/`.

## Endpoints da API

- `movies/` - CRUD de filmes.
- `actors/` - CRUD de atores.
- `genres/` - CRUD de gêneros.
- `reviews/` - CRUD de reviews.
- `authentication/token/` - Autenticação e obtenção de tokens.

## Contribuição

Se você quiser contribuir com este projeto, siga os passos abaixo:

1. Faça um fork do repositório.
2. Crie um branch para sua feature (`git checkout -b feature/nova-feature`).
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`).
4. Faça um push para o branch (`git push origin feature/nova-feature`).
5. Abra uma Pull Request.

## Contato

Para suporte ou dúvidas, entre em contato através do email: [felipe.rs991@gmail.com](mailto:email@example.com).
