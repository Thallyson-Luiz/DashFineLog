FROM python:3.12-slim

WORKDIR /app

# intalando dependências do sistema
RUN apt-get update && apt-get install -y \
    build-essential libpq-dev gcc && \
    rm -rf /var/lib/apt/lists/*


    
COPY . /app/

RUN pip install --no-cache-dir -r src/requirements.txt && \
    python src/manage.py makemigrations && \
    python src/manage.py migrate && \
    python src/manage.py collectstatic

# Para executar em desenvolvimento
CMD [ "python", "src/manage.py", "runserver", "0.0.0.0:8000" ]

# Para executar em produção
# CMD [ "gunicorn", "--bind", "0.0.0.0:8000", "src.dashfinelog.wsgi:application" ] 

