import requests
import json

API_KEY = "8711cc39b5ab4cf58b273b8fdbc6580b"
QUERY = "technology, AI"     
URL = f"https://newsapi.org/v2/everything?q={QUERY}&language=en&pageSize=100&apiKey={API_KEY}"

queries = ["technology", "AI", "robotics", "machine learning", "startup", "data", "cloud", "bitcoin"]

def fetch_multiple_queries(queries, file_path='newsapi_articles.json'):
    all_results = []
    for query in queries:
        url = f"https://newsapi.org/v2/everything?q={query}&language=en&pageSize=100&apiKey={API_KEY}"
        response = requests.get(url)
        if response.status_code == 200:
            articles = response.json()['articles']
            for article in articles:
                if article['title'] and article['content']:
                    all_results.append({
                        "title": article['title'].strip(),
                        "content": article['content'].strip()
                    })
            print(f"✅ {query}: {len(articles)} artikel diambil.")
        else:
            print(f"❌ {query}: Request gagal dengan kode {response.status_code}")

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(all_results, f, indent=2, ensure_ascii=False)
    print(f"Total artikel disimpan: {len(all_results)}")

fetch_multiple_queries(queries)
