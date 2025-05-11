FROM python:3


WORKDIR /app

COPY "requirements.txt" .

COPY app .

COPY docker_start_script.sh .
COPY database.db .

RUN pip install -r requirements.txt
RUN curl -fsSL https://ollama.com/install.sh | sh
CMD ./docker_start_script.sh