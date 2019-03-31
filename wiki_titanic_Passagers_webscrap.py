import bs4 as bs
import urllib.request
import csv

sauce = urllib.request.urlopen('https://en.wikipedia.org/wiki/Passengers_of_the_RMS_Titanic').read()
soup = bs.BeautifulSoup(sauce,'lxml')

tables = soup.find_all('table')
# table[0] = FirstClass / table[1] = SecondClass / table[2] = thirdClass
firstClass = tables[0]
secondClass = tables[1]
thirdClass = tables[2]

# func recebe uma tabela e transforma em uma lista 
def make_list (tab,classy):
    rows = tab.find_all('tr')
    lista = []
    for tr in rows:
        elements = tr.find_all('td')
        # (strip = true) gets /n off the mix
        row = [i.get_text(strip=True)  for i in elements]
        if len(row) != 0:
            row.append(classy)
            lista.append(row)
    return(lista)


# Throw in CSV 
csv_file = open('Titanic_Wiki.csv','w',newline='',encoding='utf-8')
writer = csv.writer(csv_file)
writer.writerow(('Name','Age', 'Hometown','Boarded','Destination','Lifeboat','Classes'))


# put everything in big-list with tables "Alive"
alive = make_list(firstClass,'1') + make_list(secondClass,'2') + make_list(thirdClass,'3')
    
for i in alive:
    if len(i) == 9:
        hometown = str(i[2]) + ", " + str(i[3])
        boarded = i[4]
        destination = i[5]
        lifeboat = i[6]
        classes = i[8]

    else:
        hometown = i[2]
        boarded = i[3]
        destination = i[4]
        lifeboat = i[5]
        classes = i[7]
    name = i[0]
    age = i[1]

# CVC dont accept ''    
    if lifeboat == '':
        lifeboat = 'dead'

    writer.writerow((name,age,hometown,boarded,destination,lifeboat,classes))

