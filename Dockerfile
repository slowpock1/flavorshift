FROM python:3.11-slim
 
RUN apt-get update && apt-get install -y \
    libmariadb-dev-compat \
    libmariadb-dev \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*https://pastebin.com/
 
WORKDIR /app
 
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
 
COPY ./src ./src
COPY ./config.yaml ./config.yaml
 
CMD ["python3", "src/main.py"]