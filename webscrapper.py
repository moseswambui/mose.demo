from urllib.request import urlopen

html=urlopen('http://pythonscrapping.com/pages/page1.html')
print(html.read())