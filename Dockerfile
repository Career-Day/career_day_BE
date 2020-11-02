FROM python:3.10.0a1-alpine

RUN apk add --no-cache postgresql-libs postgresql-dev gcc python3-dev musl-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 5000

ENTRYPOINT [ "flask" ]

CMD [ "run", "--host", "0.0.0.0"]
