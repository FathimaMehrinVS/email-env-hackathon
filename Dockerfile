FROM python:3.11-slim

WORKDIR /app

# Install uv
RUN pip install --no-cache-dir uv

# Copy project files
COPY . .

# Install dependencies using uv
# --frozen ensures we use the uv.lock file
RUN uv sync --frozen

# Expose port for FastAPI
EXPOSE 7860

# CMD launches the API server by default
# uvicorn runs the FastAPI app from the server package
CMD ["uv", "run", "uvicorn", "server.app:app", "--host", "0.0.0.0", "--port", "7860"]