# This python file extract data about the passengers of Titanic from the Wikipedia.org sources.  
# There is 3 relevant tables about the passengers
# 0 First Class, 1 Second Class, 2 Third Class

import bs4 as bs
import urllib.request
import csv
import FuntionCSV as fc

sauce = urllib.request.urlopen('https://en.wikipedia.org/wiki/Passengers_of_the_RMS_Titanic').read()
soup = bs.BeautifulSoup(sauce,'lxml')
tables = soup.find_all('table')


# Throw in CSV 
csv_file = open('Titanic_Wiki.csv','w',newline='',encoding='utf-8')
writer = csv.writer(csv_file)
writer.writerow(('Name','Age', 'Hometown','Country','Boarded','Destination','Lifeboat','Class','Gender'))

# Put table contents in list "passagers" / Use make_list to transform table in a list
passengers = []
i_a = 0
while i_a < 3:
    passengers = passengers + fc.make_list(tables[i_a],i_a)
    i_a = i_a + 1
    
for i in passengers:
    if len(i) == 10:
        hometown = str(i[2])
        country = str(i[3])
        boarded = i[4]
        destination = i[5]
        lifeboat = i[6]
        classes = i[8]
        gender = i[9]

    else:
        hometown = i[2]
        country = fc.country_city(hometown)
        boarded = i[3]
        destination = i[4]
        lifeboat = i[5]
        classes = i[7]
        gender = i[8]
    name = i[0]
    age = i[1]

# CVC dont accept ''    
    if lifeboat == '':
        lifeboat = 'dead'

    writer.writerow((name,age,hometown,country,boarded,destination,lifeboat,classes,gender))

