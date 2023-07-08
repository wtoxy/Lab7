FROM python:3.9.13

WORKDIR /app

COPY requirement.txt ./

RUN pip install -r requirement.txt

COPY . .

EXPOSE 5000

CMD [ "flask", "run", "--host=0.0.0.0", "--port=5000"]