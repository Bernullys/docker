FROM python:3.12-slim

RUN apt-get update && \
    apt-get install -y python3-venv && \
    python3 -m venv /opt/venv

# Upgrade pip and install FastAPI + Uvicorn
RUN /opt/venv/bin/pip install --upgrade pip && \
    /opt/venv/bin/pip install fastapi uvicorn

# Set working directory
WORKDIR /app

# Copy your main.py into the container
COPY main.py .

# Run the app from the working directory
CMD ["/opt/venv/bin/uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]