FROM python:2

WORKDIR /

RUN mkdir boinc_stopper

WORKDIR /boinc_stopper

COPY mac ./mac
COPY server ./server
COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 5020

CMD ["python", "./server/server_main.py"]