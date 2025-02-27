FROM python:3.12.4-slim

WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app

EXPOSE 11111

CMD ["flask", "run", "--host=0.0.0.0", "--port=11111"]
