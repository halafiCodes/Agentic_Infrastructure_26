FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml README.md /app/
COPY tests /app/tests
COPY specs /app/specs
COPY skills /app/skills
COPY research /app/research
COPY scripts /app/scripts

RUN python -m pip install --upgrade pip \
    && pip install "pytest>=8.0.0"

CMD ["pytest"]
