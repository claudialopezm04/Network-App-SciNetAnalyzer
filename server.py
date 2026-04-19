import socket
import json
from article_search import search_articles
from excel_export import export_to_excel
from charts import generate_charts

HOST = "127.0.0.1"
PORT = 65432

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("Server is listening...")

conn, addr = server.accept()
print(f"Connected by {addr}")

data = conn.recv(4096).decode()
request = json.loads(data)

keyword = request["keyword"]
year_from = request["year_from"]
year_to = request["year_to"]

print("Received data:")
print(f"Keyword: {keyword}")
print(f"From year: {year_from}")
print(f"To year: {year_to}")

articles = search_articles(keyword, year_from, year_to)

print("\nArticles found:")
for article in articles:
    print(f"- {article['title']} ({article['year']})")

excel_file = export_to_excel(articles, keyword, year_from, year_to)
chart_files = generate_charts(articles, keyword, year_from, year_to)

response = {
    "message": f"Found {len(articles)} articles for keyword '{keyword}'",
    "articles": articles,
    "excel_file": excel_file,
    "chart_files": chart_files
}

conn.sendall(json.dumps(response).encode())

conn.close()
server.close()