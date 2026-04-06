import requests
from bs4 import BeautifulSoup
import sqlite3

class BlogArcticle:
    def __init__(self, title, text):
        self.title = title
        self.text = text

    def to_dict(self):
        return {'titile': self.title, 'text': self.text}
    
    @classmethod
    def from_dict(cls, data):
        return cls(data['title'], data['text'])
    
class BlogParser:
    def __init__(self, base_url):
        self.base_url = base_url
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }
    
    def get_article_links(self):
        response = requests.get(self.base_url, headers=self.headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = []
        for a in soup.find_all('a', href=True):
            # links.append(a)
            if '/articles/' in a['href']:
                full_url = a['href']
                if not full_url.startswith('http'):
                    full_url = "https://msk.top_academy.ru" + full_url
                if full_url not in links:
                    links.append(full_url)
        return links

    def parse_article(self, url):
        try:
            respons = requests.get(url, headers= self.headers)
            soup = BeautifulSoup(respons.text, 'html.parser')
            card_body = soup.find(class_ = "styles_cardBody__qP0jN")
            if card_body:
                title = card_body.find('h1').get_text(strip=True) if card_body.find('h1') else 'Без заголовка'
                paragraph = card_body.find_all('p')
                text = ' '.join([p.get_text(strip=True) for p in paragraph])
                return BlogArcticle(title, text)
        except Exception as e:
            print(f'Error: {e}')
            return None

class DatabaseManager:
    def __init__(self, db_name):
        self.db_name = db_name
        self.create_table()
    
    def create_table(self):
        with sqlite3.connect(self.db_name) as conn:
            query = '''
                CREATE TABLE IF NOT EXISTS articles (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT UNIQUE,
                text TEXT);
    '''
            conn.execute(query)
            conn.commit()

    def save_articles(self, articles):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            saved_count = 0
            for art in articles:
                try:
                    cursor.execute('''
                                INSERT OF IGNORE INTO articles(title, text)
                                VALUES (?, ?)''', (art.title, art.text))
                    if cursor.rowcount > 0:
                        saved_count += 1
                except Exception as e:
                    print(f'Error BD {e}')
            conn.commit()
            return saved_count
    
    def get_top_arlicles(self, limit=5):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()

            cursor.execute('''
                            SELECT title, text
                            FROM articles
                            ORDER BY id DESC LIMIT ?;
''', (limit, ))
            return cursor.fetchall()
    
def main():
    url = 'https://msk.top-academy.ru/blog'
    print(f'Парсинг страницы {url}')
    parser = BlogParser(url)
    db = DatabaseManager('top_academy_blog.db')
    links = parser.get_article_links()
    articles_data = []
    for link in links:
        article = parser.parse_article(link)
        articles_data.append(article)
    print(f'Найдено {len(articles_data)} статей')
    saved_count = db.save_articles(articles_data)
    print(f'Добавлено {saved_count} статей')
    for i, title, text in enumerate(db.get_top_arlicles(), 1):
        short_text = text[:40] + '...' if len(text) > 40 else text
        print(f'{i} {title}\n     {short_text}\n')

if __name__ == '__main__':
    main()