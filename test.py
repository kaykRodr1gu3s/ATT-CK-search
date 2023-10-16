import requests
import bs4
import re

def a():
    ids = []
    name = []
    req = requests.get('https://attack.mitre.org/techniques/T1189/')

    bs = bs4.BeautifulSoup(req.content, 'html.parser')

    table = bs.find('table', class_='table table-bordered')
    try:
        hrefs = table.find_all('a',href = re.compile(r'/techniques/T1566/[\d]+/'))

        for key, value in enumerate(hrefs):
            if key % 2 ==0:
                ids.append(value.text.strip())
            else:
                name.append(value.text.strip())
        return ids
    
    except:
        print('nao tem sub-techniques')
        return None
def b():
    print('aqui foi')

test = a()
ds = b()


def main():
    if a in None:
        ds