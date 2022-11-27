FROM arm64v8/python:3.10.8-slim-bullseye
WORKDIR /app
COPY . .

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip3 install -r requirements.txt
CMD ["python3", "src/bot.py"]
