# DashFineLog

## Introdução

💲 Site que oferece um dashboard sobre finanças e situações econômicas de diferentes moedas, consultas e receitas econômicas
    ❗ ATENÇÃO: O site ainda esta em desenvolvimento e não encontra-se pronto para uso. pois assim como ele, estou em constante aprendizado!


## Instalação

Use o gerenciador de pacotes [pip](https://pip.pypa.io/en/stable/) para instalar as dependencias.

```bash
pip install -r src/requirements.txt
```

## Variaveis de ambiente


1. **Copie o arquivo de exemplo do `.env`**  
   O projeto já vem com um arquivo de exemplo chamado `.env-example`. Para configurar suas variáveis de ambiente, você precisa criar um arquivo `.env` baseado nesse exemplo. Execute:

   ```bash
   cp .env-example .env
   ```

2. **dite as variáveis de ambiente**
    Abra o arquivo .env e altere os valores das variáveis para os seus próprios dados. Por exemplo:

    ```.env
    DEBUG= True # (False para produção)

    # chave secreta
    SECRET_KEY= "exemplo123"

    ALLOWED_HOSTS= 127.0.0.1, localhost
    ```

## Usage

Inicie a build do projeto com [docker](https://docs.docker.com/get-started/), rode.

```bash
docker compose up --build
```

## Contributing

Solicitações de pull são bem-vindas Para alterações significativas, abra uma issue primeiro
para discutir o que você gostaria de alterar.

Certifique-se de manter os termos conforme apropriado.

## License

[MIT](LICENSE)