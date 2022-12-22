FROM arm64v8/python:3.11.1-slim-bullseye

WORKDIR /app
COPY requirements.txt .
RUN --mount=type=cache,target=/root/.cache/pip pip install -r requirements.txt
COPY . .

CMD ["python3", "src/main.py"]
