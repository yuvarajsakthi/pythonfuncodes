from urllib.request import urlopen

page = urlopen('https://google.com')
print(page.headers)
