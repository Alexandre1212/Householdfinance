import requests
#from bs4 import BeautifulSoup4
import csv

HOST='https://minfin.com.ua/'
URL='https://minfin.com.ua/cards/'
HEADERS={
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
}


def get_html(url,params=''):
    r=requests.get(url,headers=HEADERS,params=params)
    return(r)

html=get_html(URL)



def get_content(get_html):
    soup = BeautifulSoup(html,'html.parser')
    items = soup.find_all()
    cards= []



    for item in items:
        card.append(
            {
                'title':item.find()
            }
        )
