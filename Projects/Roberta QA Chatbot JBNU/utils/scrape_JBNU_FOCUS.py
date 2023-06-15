import requests, re
from bs4 import BeautifulSoup

def scrape_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    text = soup.get_text()
    text = text.strip()
    text = text.replace("\n", "")
    pattern = re.compile("[\u3131-\u3163\uac00-\ud7a3]+")
    
    if text != "":
        print(text)
        return text

def scrape_recursive(url, output_file):
    text = scrape_page(url)
    if text is not None:
        with open(output_file, "w", encoding='utf-8') as f:
            f.write(text)


url = "https://www.jbnu.ac.kr/eng/?menuID=350&mode=view&no="

for k in range(1, 320):
    scrape_recursive(url+str(k), "data/output{}.txt".format(k))