FROM python:3.11-slim

WORKDIR /app
ENV PYTHONPATH=/app

COPY . /app

RUN python -m pip install --upgrade pip \
    && pip install "pytest>=8.0.0" "pydantic>=2.0"

CMD ["pytest"]
