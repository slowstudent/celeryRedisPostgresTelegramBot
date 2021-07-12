from celery import Celery
from bs4 import BeautifulSoup
import requests
from time import sleep


app = Celery('tasks', broker='redis://0.0.0.0:6379', backend='redis://0.0.0.0:6379')

@app.task
def parse(URL):
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(URL, headers = HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    htmlquantity = 0
    for child in soup.recursiveChildGenerator():
    
        if child.name:

            htmlquantity = htmlquantity + 1
    
    return(htmlquantity)

@app.task  #for checking purposes of celery
def add(x, y):
    sleep(3)
    return x + y
