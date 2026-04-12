FROM python:3.11-slim

WORKDIR /app

# Copy project files
COPY . .

# Install dependencies globally
RUN pip install --no-cache-dir -r requirements.txt

# Expose port for FastAPI
EXPOSE 7860

# CMD launches the API server by default
# We use standard python to ensure compatibility with all entry points
CMD ["python", "-m", "uvicorn", "server.app:app", "--host", "0.0.0.0", "--port", "7860"]