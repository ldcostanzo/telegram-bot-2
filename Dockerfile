# Usa Python come immagine base
FROM python:3.11-slim

# Imposta la cartella di lavoro
WORKDIR /app

# Copia solo requirements.txt e installa le dipendenze
COPY requirements.txt requirements.txt
COPY bot.py bot.py
RUN pip install -r requirements.txt

EXPOSE 443

# Comando per avviare il bot
CMD ["python", "bot.py"]
