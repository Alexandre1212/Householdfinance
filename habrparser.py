from bs4 import BeautifulSoup
import requests as req
import xlrd
import pandas as pd

link = 'https://habr.com/ru/top/page50/'


def make_hyperlink(text, link):
    return '=HYPERLINK("%s","%s")'%(link.format(link),text)

def goParse(link):
    titles = []
    links = []
    times = []
    counter = 1
    while(True):
        print(counter)
        res = req.get(link + str(counter))
        html = BeautifulSoup(res.text,'lxml')
        times = html.find_all('span',class_='post_time')
        links_a = html.find_all('a',class_ ='post_title_link')
        page = html.find('a','next-page')

        if page == None:
            break
        counter += 1

        for i,times  in enumerate(times):
            titles.append(a.text)
            times[i] = time.next
        df = pd.DataFrame()
        df['Time'] = times
        df['News headers'] = titles
        df['News links'] = links
            

        writer = pd.ExcelWriter('./habr.xlsx',engine='xlsxwriter')
        df.to_excel(writer,sheet_name ='List1',index=False)


        writer.sheets['List1'].set_column('A:A',20)
        writer.sheets['List1'].set_column('B:B',100)
        writer.sheets['List1'].set_column('C:C',50)
            

        writer.save()

goParse(link)
