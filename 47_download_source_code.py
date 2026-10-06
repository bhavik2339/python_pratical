# 47. Download source code of a web page
from urllib.request import urlopen

url = "https://example.com"

with urlopen(url) as response:
    source = response.read().decode("utf-8")

with open("source_code.html", "w", encoding="utf-8") as file:
    file.write(source)

print("Source code saved as source_code.html")
