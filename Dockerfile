FROM python:latest
WORKDIR /app
ENV FLASK_RUN_HOST = 0.0.0.0
ENV FLASK_APP = server.py
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /app
EXPOSE 5000
CMD ["python", "server.py","runserver","--host=0.0.0.0"]
