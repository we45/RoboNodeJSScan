FROM python:2
MAINTAINER Abhay Bhargav (info@we45.com)
RUN mkdir -p /code/
COPY NodeJsScan/  /code/
RUN pip install -r /code/requirements.txt
WORKDIR /code/
RUN mkdir -p /results/
RUN mkdir -p /src/
CMD ["python", "cli.py", "-d", "/src/", "-r", "/results/nodejsscan"]
