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

# CMD runs the API server via the entry point defined in pyproject.toml
# "server" points to app:start_server
CMD ["uv", "run", "server"]