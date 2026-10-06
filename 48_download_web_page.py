# 48. Download a web page from Internet
from urllib.request import urlretrieve

url = "https://example.com"
urlretrieve(url, "downloaded_page.html")

print("Web page downloaded successfully.")
