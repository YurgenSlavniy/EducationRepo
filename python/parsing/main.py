import requests

headers = {"user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36"}

response = requests.get("https://www.google.ru", headers=headers)

response.headers

if response.status_code == 200:
    pass

if response.ok:
    pass

print(response.encoding)

response.text

response.content

with open('page.html', 'w', encoding="UTF-8") as f:
    f.write(response.text)


with open('page2.html', 'wb') as f:
    f.write(response.content)

