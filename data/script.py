import requests
import json

API_KEY = "8711cc39b5ab4cf58b273b8fdbc6580b"
QUERY = "technology"     
URL = f"https://newsapi.org/v2/everything?q={QUERY}&language=en&pageSize=100&apiKey={API_KEY}"

def fetch_and_save_articles(file_path='newsapi_articles.json'):
    response = requests.get(URL)
    if response.status_code == 200:
        articles = response.json()['articles']
        results = []

        for article in articles:
            if article['title'] and article['content']:
                results.append({
                    "title": article['title'].strip(),
                    "content": article['content'].strip()
                })

        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        print(f"Sukses menyimpan {len(results)} artikel ke {file_path}")
    else:
        print("Gagal fetch artikel:", response.status_code)

# Jalankan ini
fetch_and_save_articles()
