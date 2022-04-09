FROM python:3.8
COPY requirements.txt requirements.txt
COPY .env /opt/.env
COPY api.py /opt/api.py
RUN pip3 install -r requirements.txt
WORKDIR /opt
EXPOSE 5000
CMD python api.py
