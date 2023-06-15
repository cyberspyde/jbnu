import requests, re
from bs4 import BeautifulSoup

article_url = 'https://www.jbpresscenter.com/news/articleView.html?idxno='

def scrape_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    text = soup.get_text('a')
    text = text.strip()
    text = text.replace("\n", "")
    start_index = text.find("닫기")
    end_index = text.find("jbnu.ac.kr")
    text = text[start_index+15:end_index-25]
    return text

def has_korean_word(text):
    pattern = re.compile("[\u3131-\u3163\uac00-\ud7a3]+")
    match = re.search(pattern, text)
    if match:
        return True
    else:
        return False

def scrape_recursive(url, article_ids):
    for k in article_ids:
        text = scrape_page(url+k)
        if text is not None:
            print("working on file", k)
            with open(f'clean_data/NEWS/output{k}.txt', 'w', encoding='utf-8') as f:
                f.write(text)
    print("Files are written")

def scrape_id(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        links = soup.find_all('a', target='_top')
        article_ids = set()

        for link in links:
            href = link.get('href')
            article_id = extract_article_id(href)
            if article_id and int(article_id) > 200000:
                response = requests.get(article_url+article_id)
                soup = BeautifulSoup(response.content, "html.parser")
                text = soup.get_text('a')
                text = text.strip()
                text = text.replace("\n", "")
                start_index = text.find("닫기")
                end_index = text.find("jbnu.ac.kr")
                text = text[start_index+15:end_index-25]
                if has_korean_word(text):
                    pass
                else:
                    article_ids.add(article_id)
        return article_ids
    else:
        print("Failed to retrieve the page:", response.status_code)

def extract_article_id(href):
    pattern = r'\d+'  # Assuming the article ID is a sequence of digits
    match = re.search(pattern, href)
    if match:
        return match.group(0)
    else:
        return None


def scrape_recursive_pagination(start, end):
    for k in range(start, end+1):
    
        url = f"https://www.jbpresscenter.com/news/articleList.html?page={k}&box_idxno=&sc_sub_section_code=S2N18&view_type=sm"
        article_ids = scrape_id(url)
        print(article_ids, len(article_ids))

        url = 'https://www.jbpresscenter.com/news/articleView.html?idxno='
        scrape_recursive(url, article_ids)

scrape_recursive_pagination(6, 39)