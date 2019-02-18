from urllib.request import urlopen
from bs4 import BeautifulSoup


def Oldalbeolvasas():
    # Bekér egy url címet
    x = input("Kerem az URL-t: ")

    html = urlopen("http://"+x)
    vizsgalat = BeautifulSoup(html, "html.parser")
    # Megkeresi az összes title tag-ot és kíirja a console-ra.
    for title in vizsgalat.find_all("title"):
        # Kiírja tag-gel együtt
        print(title)
        # Kiírja tag nélkül
        print(title.text)
        
        
Oldalbeolvasas()