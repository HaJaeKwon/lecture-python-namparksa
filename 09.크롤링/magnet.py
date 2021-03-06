import requests
from bs4 import BeautifulSoup
import re


def search_magnet(keyword, start_page, end_page=None):
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    header = {"user-agent": user_agent}

    url = "https://www.google.com/search?q={}+magnet%3F%3Axt%3D&start={}"
    # 브라우저, 모바일에 따라서 리턴해주는 결과물이 다르다 !!
    r = requests.get(url.format(keyword, start_page), headers=header)
    bs = BeautifulSoup(r.text, "lxml")
    links = bs.select("div.g > div > div.rc > div.r > a")

    results = []

    if end_page is None:
        count = int(bs.select("div#resultStats")[0].text.split("개")[0].replace("검색결과 약", "").strip())
        end_page = int(count)
        if end_page > 50:
            end_page = 50

    for link in links:
        href = link["href"]
        #print(link.text)
        text = link.select("h3 > span")
        if len(text) <= 0:
            continue
        title = text[0].text

        try:
            r = requests.get(href)
            bs = BeautifulSoup(r.text, "lxml")
            magnets = bs.find_all("a", href=re.compile(r'magnet:\?xt=*'))

            if len(magnets) > 0:
                magnet = magnets[0]["href"]
                results.append((title, magnet))
                print(title, magnet)
        except:
            pass

    if start_page < end_page:
        start_page += 10
        results.extend(search_magnet(keyword, start_page, end_page))

    return results


keyword = "linux"
results = search_magnet(keyword, 0)

for r in results:
    print(r)
