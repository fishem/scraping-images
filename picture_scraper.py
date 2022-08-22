import random
import time 
import urllib.request

# from bs4 import BeautifulSoup

# Optional - Download html file
# with open('fhtmlfile.html', 'rb') as html:
#     soup = BeautifulSoup(html, 'lxml')

# Generate links (3640) to download 
x = range(0,70)
y = range(0,52)

list_of_url = []
for first_nb in x:
    for snd_nb in y:
        image_url = f'https://storage.googleapis.com/raremaps/img/dzi/img_66046_files/15/{first_nb}_{snd_nb}.jpg'
        list_of_url.append(image_url)

# Download links
for link in list_of_url[3336:]:
    filename = str(link.split('/')[-2]+'_'+link.split('/')[-1])
    try:
        urllib.request.urlretrieve(link, f'Pictures/{filename}')
    except urllib.error.HTTPError:
        continue
    time.sleep(random. randint(0,5)) # To avoid being blocked by the server
    print('Done: ', filename)


