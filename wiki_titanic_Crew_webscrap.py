# This python file extract data about the crew members of Titanic from the Wikipedia.org sources.  
# There is 8 relevant tables about the Crew members
# 0 Ship's officers ,1 Deck crew ,2 Engineering crew, 3 Victualling crew, 4 Restaurant staff, 
# 5 Postal clerks, 6 Guarantee group, 7 Ship's orchestra

import bs4 as bs
import urllib.request
import csv
import FuntionCSV as fc

sauce = urllib.request.urlopen('https://en.wikipedia.org/wiki/Crew_of_the_RMS_Titanic').read()
soup = bs.BeautifulSoup(sauce,'lxml')
tables = soup.find_all('table')


# Create CSV and write first line. 
csv_file = open('Titanic_Wiki_CREW.csv','w',newline='',encoding='utf-8')
writer = csv.writer(csv_file)
writer.writerow(('Name','Age','Hometown','Boarded','Position','Lifeboat','Gender','Country'))

# Create a list (crew) with all table contents and throw them in the CSV
i_a = 0
crew = []
while i_a < 8:
    crew = crew + fc.make_list(tables[i_a])
    i_a = i_a + 1

for i in crew:
    if len(i) == 8:
        hometown = i[2]
        boarded = i[3]
        position = i[4]
        lifeboat = i[5]
        gender = i[7]

    elif len(i) == 7:
        hometown = i[3]
        boarded = i[4]
        position = i[5]
        gender = i[6]
        lifeboat = ''

    else:
        hometown = i[2]
        position = i[3]
        lifeboat = ''
        boarded = 'Southampton'
        gender = i[5]
    
    name = i[0]
    age = i[1]
    country = fc.country_city(hometown)

    if lifeboat == '':
        lifeboat = 'dead'

    writer.writerow((name,age,hometown,boarded,position,lifeboat,gender,country))