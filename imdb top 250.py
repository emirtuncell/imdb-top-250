import requests

from bs4 import  BeautifulSoup

url = "https://www.imdb.com/chart/top/"
headers = { #web sitesinden veri çekebilmek için bu lazım. yoksa bot zannedildim.
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

response = requests.get(url, headers=headers)

html_icerigi = response.content

soup =BeautifulSoup(html_icerigi,"html.parser")

basliklar = list()
ratingler = list()

for i in soup.find_all("li",{"class":"ipc-metadata-list-summary-item"}):
    basliklar.append(i.text) # burada f12 kısmından başlıkların yazdığı html elementini bulup verileri çektim ve bir listede depoladım.



for a in soup.find_all("li", {"class": "ipc-metadata-list-summary-item"}):
    rating = a.find("span", {"class": "ipc-rating-star--rating"})
    ratingler.append(rating.text.strip())
# burada da f12 kısmından reytinglerin yazdığı html elementini bulup verileri çektim ve bir listede depoladım.

for x in zip(basliklar,ratingler):#burada zip ile aynı uzunluktaki iki listenin elemanlarını yazdırdım.
    for c in x:
        print(c)
    print("---------------------------------------------------")
