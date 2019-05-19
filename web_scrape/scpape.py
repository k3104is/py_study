import urllib.request
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, site):
        self.site = site  # URLを受け取る

    def scrape(self):
        r = urllib.request.urlopen(self.site)   # ウェブサイトへリクエストし、レスポンスが変える
        html = r.read()  # レスポンスからHTMLデータを抜き取りhtmlへ入れる
        parser = "html.parser"  # BeautifulSoupにHTMLをパースしてほしいことを伝える文字列
        sp = BeautifulSoup(html, parser)  # HTMLをパースする
        for tag in sp.find_all("a"):  # <a></a>タグをすべて集めて返す
            url = tag.get("href")  # URLが代入されているhrefを取り出す
            print(url)
            # if url is None:
            #     continue
            # if "html" in url:
            #     print("\n" + url)


news = "https://news.google.com/"
Scraper(news).scrape()
