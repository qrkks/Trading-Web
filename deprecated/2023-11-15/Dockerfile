FROM python:3.11-alpine3.18

RUN pip install --upgrade pip

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

COPY ./entrypoint.sh /
ENTRYPOINT [ "sh", "/entrypoint.sh" ]