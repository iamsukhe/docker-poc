deploy flask projectFROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

# Use Gunicorn for production
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]