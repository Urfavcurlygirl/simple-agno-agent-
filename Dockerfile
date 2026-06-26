FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Create tmp directory for sqlite
RUN mkdir -p tmp

# Run uvicorn on port 7860 (Hugging Face Spaces default port)
CMD ["uvicorn", "main:router", "--host", "0.0.0.0", "--port", "7860"]
