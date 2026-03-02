FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy everything into /app
COPY . .

# Ensure the parent directory of cloud_brain is in the python path
ENV PYTHONPATH=/app

CMD ["python", "cloud_brain/main.py"]
