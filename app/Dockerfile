FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY static/ /app/static/  # Ensure the static folder is copied
COPY templates/ /app/templates/  # Ensure the templates folder is copied
COPY app.py app.py

EXPOSE 5000

CMD ["python", "app.py"]
