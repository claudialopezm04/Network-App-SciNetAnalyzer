import socket
import json
import os
from datetime import datetime
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

safe_keyword = keyword.replace(" ", "_").lower()
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_folder = os.path.join("results", f"{safe_keyword}_{year_from}_{year_to}_{timestamp}")

print("Received data:")
print(f"Keyword: {keyword}")
print(f"From year: {year_from}")
print(f"To year: {year_to}")

articles = search_articles(keyword, year_from, year_to)

print("\nArticles found:")
for article in articles:
    print(f"- {article['title']} ({article['year']})")

if len(articles) > 0:
    excel_file = export_to_excel(articles, output_folder, keyword, year_from, year_to, timestamp)
    chart_files = generate_charts(articles, output_folder, keyword, year_from, year_to, timestamp)
else:
    excel_file = None
    chart_files = []

response = {
    "message": f"Found {len(articles)} articles for keyword '{keyword}'",
    "articles": articles,
    "excel_file": excel_file,
    "chart_files": chart_files
}

conn.sendall(json.dumps(response).encode())

conn.close()
server.close()