FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

ENV FLASK_APP=API_Quiz.py
ENV FLASK_RUN_HOST=0.0.0.0

CMD ["python", "-m", "flask", "run"]