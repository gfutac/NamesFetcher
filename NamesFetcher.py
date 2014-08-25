
from bs4 import BeautifulSoup
import urllib.request

genders = ['muska', 'zenska']
letters = "ABCDEFGHIJKLMNOPRSTUVZ"
basepage = "http://www.knjigaimena.com/?" + genders[0] + "&imena-koja-pocinju-sa-"

html = ""
counter = 1

def getNames(url):
    response = urllib.request.urlopen(url)
    html = response.read()   
    soup = BeautifulSoup(html)
    names = [n.text for n in soup.findAll("a", { "class" : "name"})]

    nextpage = True

    try:
        indexofnext = names.index("~ Sledeća ~")
        names = names[0:indexofnext]
    except:
        nextpage = False

    return nextpage, names

def prettyprint(list):
    global counter
    for element in list:
        print(str(counter) + ';' + element + ';' + element)
        counter = counter + 1

for l in letters:
    url = basepage + l
    next = 1
    while True:
        next = next + 1
        nextpage, names = getNames(url)
        if '~ Prethodna ~' in names:
            names.remove('~ Prethodna ~')

        if nextpage == False:
            break

        try:
            i = names.index('A')
            names = names[0:i]
            break
        except:
            pass

        prettyprint(names)
        url = url + "&stranica=" + str(next)



