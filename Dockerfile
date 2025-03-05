# Utilizziamo un'immagine base di Python
FROM python:3.9-slim

# Impostiamo la directory di lavoro
WORKDIR /app

# Copiamo i file necessari nel container
COPY requirements.txt ./
COPY tracker_luna.py ./

# Installiamo le dipendenze necessarie
RUN pip install --no-cache-dir -r requirements.txt

# Comando per eseguire il tracker della luna
CMD ["python", "tracker_luna.py"]

