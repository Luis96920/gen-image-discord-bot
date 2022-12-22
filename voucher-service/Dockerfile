FROM arm64v8/python:3.11.1-slim-bullseye

WORKDIR /app
COPY requirements.txt .
RUN --mount=type=cache,target=/root/.cache/pip pip install -r requirements.txt
COPY . .
WORKDIR /app/src

CMD ["python3", "app.py"]
