import requests
import re
import bs4

def getting_tactics() ->list:
    tactics_link = []

    req = requests.get('https://attack.mitre.org/tactics/enterprise/')
    bs = bs4.BeautifulSoup(req.content, 'html.parser')
    bs = bs.find('table', class_='table table-bordered table-alternate mt-2')
    bs4_tactics = bs.find_all('a', href=re.compile(r'/tactics/TA[\d]+'))

    for link in bs4_tactics:
        
        if link['href'] not in tactics_link:

            tactics_link.append(link['href'])
        else:
            continue

    return tactics_link

def options():
    number = ['0', '1', '2', '3', '4', '5', '6', '7', '8','9', '10', '11', '12', '13']
    name = ['Reconnaissance', 'Resource Development', 'Initial Access', 'Execution', 'Persistence', 'Privilege Escalation', 'Defense Evasion',
            'Credential Access', 'Discovery', 'Lateral Movement', 'Collection', 'Command and Control', 'Exfiltration', 'Impact']  


    conc = zip(number, name)

    print('Choice one option')
    print('=' * 30)
    for c in conc:
        print(c)

    print('=' * 30)

    choice = int(input('which of the choices: '))
    print()
    print(f'You choice the {name[choice].upper()} option')
    print()

    return choice


req = requests.get(f'https://attack.mitre.org{getting_tactics()[options()]}')


beuaty_soup = bs4.BeautifulSoup(req.content, 'html.parser')
Table = beuaty_soup.find('table', {'class': 'table-techniques'})

headers = []
bs = Table.find_all('td', colspan='2')
headers.append(bs[0])
del bs[0]


name_id = []
options_id = []
for c in bs:
    name_id.append(c.text.replace('\n', ''))
    
print(f'The tactics are -> {name_id}')


for num in enumerate(name_id):
    options_id.append(num)




print('For see the tactics information paste the ID bellow')
for option in options_id:
    print(option)

tactic_option = int(input('Which of the options you want? '))

req_sub_technique = requests.get(f'https://attack.mitre.org/techniques/{name_id[tactic_option].strip()}')
print(req_sub_technique)