FROM python:3.9
RUN apt-get update -y
RUN apt-get upgrade -y

WORKDIR /proj

COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY ./ ./

CMD ["python", "./bot.py"]