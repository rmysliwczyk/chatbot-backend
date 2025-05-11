FROM python:3


WORKDIR /app

COPY "requirements.txt" .

COPY app .

COPY database.db .

RUN pip install -r requirements.txt
RUN curl -fsSL https://ollama.com/install.sh | sh
ENTRYPOINT [ "fastapi", "dev", "--host", "0.0.0.0" ]