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

data = client.recv(4096).decode()
response = json.loads(data)

print("\nServer response:")
print(response["message"])

print("\nArticles received:")
for article in response["articles"]:
    print(f"- {article['title']} ({article['year']})")

print(f"\nExcel file created: {response['excel_file']}")

print("\nChart files created:")
for chart in response["chart_files"]:
    print(f"- {chart}")

client.close()