FROM python:3.12-slim

# Evita logs raros y mejora rendimiento
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Código
COPY . .

# Fly expone el 8080 típicamente
EXPOSE 8080

# Gunicorn (producción)
CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:8080", "app:app"]
