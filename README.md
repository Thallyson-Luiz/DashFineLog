# 💰 DashFineLog

> **Dashboard inteligente para acompanhamento de finanças e criptomoedas**

[![Django](https://img.shields.io/badge/Django-5.2.5-green.svg)](https://djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://python.org/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED.svg)](https://docker.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 🚀 Sobre o Projeto

O **DashFineLog** é uma aplicação web moderna desenvolvida em Django que oferece um dashboard completo para acompanhamento de finanças pessoais e criptomoedas. Com uma interface intuitiva e dados em tempo real, você pode monitorar suas moedas favoritas, acompanhar variações de preços e ter uma visão geral do mercado.

### ✨ Principais Funcionalidades

- 📊 **Dashboard Personalizado**: Visualize suas criptomoedas em um painel centralizado
- 💱 **Cotações em Tempo Real**: Dados atualizados via AwesomeAPI
- 🔐 **Sistema de Autenticação**: Login e registro de usuários
- 📈 **Análise de Variações**: Acompanhe a performance das suas moedas
- 🎯 **Portfólio Personalizado**: Adicione e gerencie suas moedas favoritas
- 📱 **Interface Responsiva**: Funciona perfeitamente em desktop e mobile
- 🐳 **Containerização**: Deploy simplificado com Docker

### 🛠️ Tecnologias Utilizadas

- **Backend**: Django 5.2.5, Django REST Framework
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap
- **Banco de Dados**: SQLite (desenvolvimento) / PostgreSQL (produção)
- **APIs**: AwesomeAPI para cotações, AlternativeAPI para humor do mercado
- **Containerização**: Docker & Docker Compose
- **Autenticação**: JWT (JSON Web Tokens)

## 🚀 Início Rápido

### Pré-requisitos

- [Docker](https://docs.docker.com/get-started/) e Docker Compose
- [Git](https://git-scm.com/) (opcional)

### 🐳 Instalação com Docker (Recomendado)

1. **Clone o repositório**
   ```bash
   git clone https://github.com/Thallyson-Luiz/dashfinelog.git
   cd dashfinelog
   ```

2. **Configure as variáveis de ambiente**
   ```bash
   cp .env-example .env
   ```
   
   Edite o arquivo `.env` com suas configurações:
   ```env
   DEBUG=True
   SECRET_KEY=sua-chave-secreta-aqui
   ALLOWED_HOSTS=127.0.0.1, localhost
   ```

3. **Execute com Docker**
   ```bash
   docker compose up --build
   ```

4. **Acesse a aplicação**
   ```
   http://localhost:8000
   ```

### 💻 Instalação Local (Desenvolvimento)

Se preferir executar localmente sem Docker:

1. **Crie um ambiente virtual**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # ou
   venv\Scripts\activate     # Windows
   ```

2. **Instale as dependências**
   ```bash
   pip install -r src/requirements.txt
   ```

3. **Configure o banco de dados**
   ```bash
   cd src
   python manage.py migrate
   python manage.py createsuperuser
   ```

4. **Execute o servidor**
   ```bash
   python manage.py runserver
   ```

## 📖 Como Usar

### 🎯 Primeiros Passos

1. **Registre-se**: Crie sua conta na página de registro
2. **Faça Login**: Acesse sua conta na página de login
3. **Explore o Dashboard**: Visualize o resumo geral das finanças
4. **Adicione Moedas**: Vá em "Minhas Moedas" e adicione suas criptomoedas favoritas
5. **Acompanhe Cotações**: Monitore preços e variações em tempo real

### 🔧 Funcionalidades Detalhadas

#### 📊 Dashboard Principal
- Resumo geral das suas moedas
- Gráficos de performance
- Indicadores de mercado

#### 💰 Gerenciamento de Moedas
- Adicionar/remover criptomoedas
- Configurar pares de negociação
- Validação automática de tickers

#### 📈 Análise de Mercado
- Cotações em tempo real
- Cálculo de variações percentuais
- Humor do mercado (Fear & Greed Index)

## 🏗️ Estrutura do Projeto

```
dashfinelog/
├── src/
│   ├── dashfinelog/          # Configurações do Django
│   ├── home/                 # App principal
│   │   ├── models.py         # Modelos de dados
│   │   ├── views/            # Views organizadas
│   │   ├── templates/        # Templates HTML
│   │   └── static/           # Arquivos estáticos
│   ├── api/                  # API REST
│   ├── modules/              # Módulos de integração
│   │   ├── coins.py          # Integração com APIs de moedas
│   │   ├── cripto.py         # Dados de criptomoedas
│   │   └── dolar.py          # Dados do dólar
│   └── utils/                # Utilitários
├── docker-compose.yml        # Configuração Docker
├── Dockerfile               # Imagem Docker
└── requirements.txt         # Dependências Python
```

## 🔧 Configuração Avançada

### Variáveis de Ambiente

| Variável | Descrição | Padrão |
|----------|-----------|---------|
| `DEBUG` | Modo debug | `True` |
| `SECRET_KEY` | Chave secreta do Django | `CHANGE-ME` |
| `ALLOWED_HOSTS` | Hosts permitidos | `127.0.0.1, localhost` |
| `DB_NAME` | Nome do banco (produção) | - |
| `DB_USER` | Usuário do banco (produção) | - |
| `DB_PASSWORD` | Senha do banco (produção) | - |
| `DB_HOST` | Host do banco (produção) | `localhost` |
| `DB_PORT` | Porta do banco (produção) | `5432` |

### 🐳 Deploy em Produção

1. **Configure as variáveis de ambiente para produção**
2. **Use PostgreSQL como banco de dados**
3. **Configure um servidor web (Nginx + Gunicorn)**
4. **Configure SSL/HTTPS**

## 🤝 Contribuindo

Contribuições são sempre bem-vindas! Se você tem uma ideia que pode melhorar o projeto:

1. **Fork** o projeto
2. **Crie** uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. **Commit** suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. **Push** para a branch (`git push origin feature/AmazingFeature`)
5. **Abra** um Pull Request

### 📝 Padrões de Código

- Use **PEP 8** para Python
- Documente funções e classes
- Escreva testes para novas funcionalidades
- Mantenha commits descritivos

## 🐛 Reportando Bugs

Encontrou um bug? Ajude-nos a melhorar!

1. Verifique se o bug já foi reportado nas [Issues](../../issues)
2. Crie uma nova issue com:
   - Descrição detalhada do problema
   - Passos para reproduzir
   - Screenshots (se aplicável)
   - Informações do ambiente

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👨‍💻 Autor

**Thallyson** - [GitHub](https://github.com/Thallyson-Luiz)

## 🙏 Agradecimentos

- [AwesomeAPI](https://docs.awesomeapi.com.br/) - Dados de cotações
- [AlternativeAPI](https://alternative.me/) - Dados de humor do mercado
- [Django](https://djangoproject.com/) - Framework web
- [Bootstrap](https://getbootstrap.com/) - Framework CSS

---

<div align="center">

**⭐ Se este projeto te ajudou, considere dar uma estrela! ⭐**

[![GitHub stars](https://img.shields.io/github/stars/Thallyson-Luiz/dashfinelog?style=social)](https://github.com/Thallyson-Luiz/dashfinelog)
[![GitHub forks](https://img.shields.io/github/forks/Thallyson-Luiz/dashfinelog?style=social)](https://github.com/Thallyson-Luiz/dashfinelog)

</div>