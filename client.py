import socket
import json

HOST = "127.0.0.1"
PORT = 65432

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

keyword = input("Enter keyword: ")
year_from = input("Enter start year: ")
year_to = input("Enter end year: ")

request = {
    "keyword": keyword,
    "year_from": year_from,
    "year_to": year_to
}

client.sendall(json.dumps(request).encode())

chunks = []
while True:
    part = client.recv(4096)
    if not part:
        break
    chunks.append(part)

data = b"".join(chunks).decode()
response = json.loads(data)

print("\nServer response:")
print(response["message"])

print("\nArticles received:")
for article in response["articles"]:
    print(f"- {article['title']} ({article['year']})")

if response["excel_file"]:
    print(f"\nExcel file created: {response['excel_file']}")

if response["chart_files"]:
    print("\nChart files created:")
    for chart in response["chart_files"]:
        print(f"- {chart}")
client.close()