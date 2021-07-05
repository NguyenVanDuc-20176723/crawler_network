from lxml import html
import requests

url = 'https://cdn.shopify.com/s/files/1/0512/1566/3301/products/UPTO-16_800x.png?v=1624446996'
res = requests.get(url)
#tree = html.fromstring(res.content)
img = res.content
f = open("image.jpg", "wb")
f.write(img)