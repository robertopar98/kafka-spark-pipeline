FROM python:3.11-slim

WORKDIR /app

# Copy requirements and install
COPY docker/python/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY src /app/src

ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

# Default command, can override in docker-compose
CMD ["python", "-m", "src.producer.producer"]


HEALTHCHECK --interval=30s --timeout=10s --start-period=10s --retries=3 \
  CMD python -m src.health_check || exit 1