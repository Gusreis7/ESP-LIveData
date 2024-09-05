FROM python:3.9

# Defina o diretório de trabalho
WORKDIR /app

# Copie o arquivo requirements.txt primeiro para aproveitar o cache do Docker
COPY requirements.txt ./

# Instale as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copie o código da aplicação para o diretório de trabalho
COPY flaskapp/ ./

# Defina o comando de entrada do container
CMD ["python3", "app.py"]
