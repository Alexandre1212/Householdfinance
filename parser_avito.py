import requests
from bs4 import BeautifulSoup


def get_html(url):
    r = requests.get(url)
    return r.text


def get_total_pages(html):
    soup = BeautifulSoup(html,'lxml')
    pages =soup.find('div',class_='pagination-pages').find_all('a',class_='pagination-pages')[1].get('href')
    total_pages = pages.split('=')[1].split('&')[0]
    return int(total_pages)



def get_page_data(html):
    soup = BeautifulSoup(html,'lxml')
    ads = soup.find()




    #find('div',class)
    #find_all('div',class)


    write_cvs(data)
    else:
        continue   

def main():
  #  https://www.avito.ru/sankt-peterburg/telefony?p=1&q=HTC
     pass


if __name__ == "__main__":
    main()