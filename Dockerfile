# Use uma imagem base do Python
FROM python:3.8

# Define o diretório de trabalho no contêiner
WORKDIR /app

# Copia o conteúdo do diretório atual para o diretório de trabalho
COPY . /app

# Instala as dependências do projeto
RUN pip install -r requirements.txt

# Expõe a porta que a aplicação Flask utiliza
EXPOSE 5000

# Comando para executar a aplicação quando o contêiner iniciar
CMD ["python", "main.py"]

# docker build -t nome_da_imagem .
# docker build -t mentoria_image .

# docker run -p 5000:5000 -v caminho_local:/app nome_da_imagem
# docker run -p 5000:5000 -v $(pwd):/app mentoria_image