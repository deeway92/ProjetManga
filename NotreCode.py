import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import os
if __name__ == '__main__':
    def dossier():
        os.chdir("C://Users//deeps//Desktop//test")

    dossier()

path = r"C://Users//deeps//Desktop//test"
CompteurParcours = 0

url = "https://scantrad.net/mangas/the-second-coming-of-gluttony/30"

def Navigate(url):
    if url != "Fin du Manga":
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        ListeLiens = RecupListeLiens(soup)
    return [soup, ListeLiens]

def RecupListeLiens(soup):
    Div = soup.findAll('div')
    L = []
    Img=soup.findall('img')
    for item in Img:
        if'data-src' in item.attrs:
            print(item['data-src'])
    for item in Div:
        if ClasseDownload(item):
            L.append(item)
    ListeTag = []
    for item in L:
        ListeTag.append(item.find('img'))
    ListeLiens = []
    for item in ListeTag:
        t = item['src']
        n = t.find('https')
        ListeLiens.append(item['src'][n:])
    return ListeLiens

def Next(soup):
    NextUrl = ""
    A = soup.findAll('a')
    L = []
    for a in A:
        if 'class' in a.attrs and a['class'] == ['btn','next_page']:
            NextUrl = a['href']
    if NextUrl == "":
        NextUrl = "Fin du Manga"
    print(NextUrl)
    return NextUrl
