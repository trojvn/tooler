FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-root

COPY . /app

CMD ["python3", "-m", "pytest", "-v", "tests"]