import bs4 as bs
import urllib.request
import csv

sauce = urllib.request.urlopen('https://en.wikipedia.org/wiki/Crew_of_the_RMS_Titanic').read()
soup = bs.BeautifulSoup(sauce,'lxml')

tables = soup.find_all('table')


# there is 8 tables
# 0 Ship's officers ,1 Deck crew ,2 Engineering crew, 3 Victualling crew, 4 Restaurant staff, 5 Postal clerks, 6 Guarantee group, 7 Ship's orchestra

# func recebe uma tabela e transforma em uma lista 
def make_list (x):
    tab = tables[x]
    rows = tab.find_all('tr')
    lista = []
    for tr in rows:
        elements = tr.find_all('td')
        # (strip = true) gets /n off the mix
        row = [i.get_text(strip=True)  for i in elements]
        if len(row) != 0:
            lista.append(row)
    return(lista)

#Throw in CSV 
csv_file = open('Titanic_Wiki_CREW.csv','w',newline='',encoding='utf-8')
writer = csv.writer(csv_file)
writer.writerow(('name','age','hometown','boarded','position','lifeboat'))

# Create a list with all crew then 
i_a = 0
crew = []
while i_a < 8:
    crew = crew + make_list(i_a)
    i_a = i_a + 1

for i in crew:
    if len(i) == 7:
        hometown = i[2]
        boarded = i[3]
        position = i[4]
        lifeboat = i[5]

    elif len(i) == 6:
        hometown = i[3]
        boarded = i[4]
        position = i[5]
        lifeboat = ''

    else:
        hometown = i[2]
        position = i[3]
        lifeboat = ''
        boarded = 'Southampton'
    
    name = i[0]
    age = i[1]

    if lifeboat == '':
        lifeboat = 'dead'

    writer.writerow((name,age,hometown,boarded,position,lifeboat))