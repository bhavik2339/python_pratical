# 49. Download an image from Internet
from urllib.request import urlretrieve

image_url = "https://www.python.org/static/community_logos/python-logo.png"
urlretrieve(image_url, "python-logo.png")

print("Image downloaded successfully.")
