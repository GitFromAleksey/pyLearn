from bs4 import BeautifulSoup

FILE_NAME = 'content.html'

with open(FILE_NAME) as file:
    src = file.read()

##print(src)

soup = BeautifulSoup(src, 'lxml')

title = soup.title

print(title)
print(title.text)
print(title.string)

##div = soup.find('div')
##print(div)
##print(div.attrs)
##print(len(div.contents))
##for child in div.children:
##    print('.',child)
##div_all = soup.find_all('div')
##for div in div_all:
##    print(div)

##class_data = soup.find('div', class_='data')
##print(class_data)
##print(class_data.)

##input_data = soup.find('input', id='A1')
##print(input_data)
##print(input_data.attrs)

####<div class="caps" unselectable="on">[Caps Lock]</div>
##caps_data = soup.find('div', class_='caps')
##print(caps_data)
##print(caps_data.attrs)
##print(caps_data.contents)
##print(caps_data.string)
##print(caps_data.text)
##
##caps_data = soup.find('div', {'class' : 'caps', 'unselectable' : 'on'})
##print(caps_data)

##def PrintDivs(indent, div):
##    print(indent, div.attrs)
##    for divs in div.find_all('div'):
##        PrintDivs(indent+' ',divs)
##
##div_data = soup.find('div')
##PrintDivs(' ',div_data)

##all_a = soup.find_all('a')
##print(all_a)
##for item in all_a:
##    print(item.get('href'), item.text)

class_data = soup.find('div', class_='data')
print(class_data)
##class_data_parent = class_data.find_parent()
##print(class_data_parent)
class_data_parents = class_data.find_parents()
print(class_data_parents)

