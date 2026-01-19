FROM python:3.12-slim

WORKDIR /app

# Install uv.
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Copy the application into the container.
COPY ./src/ /app/src
COPY pyproject.toml /app/pyproject.toml
COPY uv.lock /app/uv.lock
COPY README.md /app/README.md

# Install the application dependencies.
RUN uv sync --frozen --no-cache

# ENV PYTHONUNFUFFERED=1
EXPOSE 8010

# Run the application.
# CMD ["/app/.venv/bin/fastapi", "run", "app/main.py", "--port", "8010", "--host", "0.0.0.0"]
CMD ["uv", "run", "uvicorn", "joke_app.main:app", "--host", "0.0.0.0", "--port", "8010"]
