from bs4 import BeautifulSoup as b
import requests as r
webby = "https://www.fide.com/category/chess-news/"
d = r.get(webby)
if d.status_code == 200:
    c = b(d.text , 'html.parser')
    print(f"Recent Chess News (from FIDE):\n")
    for link in c.find_all('a') [83:129]:
        tig = link.text.strip()
        h = link.get('href')
        if tig and "CHESS NEWS" not in tig:
            git = tig.encode('ascii' , 'ignore').decode('utf-8')
            print(f"{git}\n")
            print(f"URL to the news: {h}\n")
else:
    print(f"ERROR. CONNECTION FAILED. ERROR CODE - {r.status_code}")