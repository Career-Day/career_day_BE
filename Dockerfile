FROM python:3.9.0-alpine

RUN apk add --no-cache postgresql-libs postgresql-dev gcc python3-dev musl-dev

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 5000

ENTRYPOINT [ "flask" ]

CMD [ "run", "--host", "0.0.0.0"]
