FROM python:3.12-slim

WORKDIR /app

# Install uv.
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Copy the application into the container.
COPY ./app/main.py /app/app/main.py
COPY pyproject.toml /app/pyproject.toml
COPY uv.lock /app/uv.lock

# Install the application dependencies.
RUN uv sync --frozen --no-cache

# ENV PYTHONUNFUFFERED=1
EXPOSE 8010

# Run the application.
# CMD ["/app/.venv/bin/fastapi", "run", "app/main.py", "--port", "8010", "--host", "0.0.0.0"]
CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8010"]
