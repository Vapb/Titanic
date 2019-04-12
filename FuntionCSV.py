# Serie of Functions to help Webscrapping

# ============================================================================================================================================

# Function that return gender of the pronoun 
def pronoun_sex (nome):
    pronouns_female = ["Mrs.","Miss ","Lucy ","Doña ","Mrs,","Mrs ","Miss."]
    pronouns_male = ["Colonel ","Mr.","Master ","Father ","Dr.","Reverend ","Don ","Sir ","Major ","Captain ","Mr,","Mr ","Lieutenant","Commander"]
    sex = "None"
    for i in pronouns_male:
        if i in nome:
            sex = "Male"
    for i in pronouns_female:
        if i in nome:
            sex = "Female"
    if sex == "None": # The excessions are male
        sex = "Male"
    return sex

#=============================================================================================================================================

# Function recive a Table and make a list out of the contents
def make_list (tab,classy = ""):
    rows = tab.find_all('tr')
    lista = []
    for tr in rows:
        elements = tr.find_all('td')
        # (strip = true) gets /n off the mix
        row = [i.get_text(strip=True)  for i in elements]
        if len(row) != 0:
            if classy != "":
                row.append(classy + 1)
            row.append(pronoun_sex(row[0]))
            lista.append(row)
    return(lista)

#===============================================================================================================================================

# GEt country from the hometown
def country_city (hometown):
    country = ''
    coma = False
    for i in hometown:
        if i == '[':
            break
        if coma:
            country = country + i
        if i == ',' and coma and i != hometown[-1:]:
            country = ''
        elif i == ',':
            coma = True

    if coma == False: # no comma
        country = hometown
    return country 

# ==========================================================================================================================================