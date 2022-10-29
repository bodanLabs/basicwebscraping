#import libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup

#declare the link
url = "https://en.wikipedia.org/wiki/Python_(programming_language)"

#get the html code
html_code = urlopen(url).read().decode("utf-8")

#declare the soup
soup = BeautifulSoup(html_code,'lxml')

#find the table and declare its body & rows
type_table = soup.find(class_='wikitable')
body = type_table.find("tbody")
rows = body.find_all("tr")[1:]

#create empty lists
mutable_types = []
immutable_types = []

#read through rows to save the values
for row in rows:
    data = row.find_all("td")
    #if condition for mutable
    if data[1].get_text() == "mutable\n":
        #add to the empty list
        mutable_types.append(data[0].get_text())
    #else (if not mutable)
    else:
        #add to the empty list
        immutable_types.append(data[0].get_text())

#print the values
print(f"Mutable Types: {mutable_types}\n"
      f"Immutable Types: {immutable_types}")

#find the class
thumb_box = soup.find(class_="thumbinner")
#find the source of the image
thumb_img_src = thumb_box.find("img")['src']
#print the source
print(thumb_img_src)

#find the table of contents class
toc = soup.find(class_="toc")
#get all elements from it
toc_text = [a.get_text() for a in toc.find_all('a')]
#print the elements
print(toc_text)


