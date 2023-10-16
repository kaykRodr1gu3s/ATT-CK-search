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

def tactics():
    req = requests.get(f'https://attack.mitre.org{getting_tactics()[options()]}')


    beuaty_soup = bs4.BeautifulSoup(req.content, 'html.parser')
    Table = beuaty_soup.find('table', {'class': 'table-techniques'})

    headers = []
    bs = Table.find_all('td', colspan='2')
    headers.append(bs[0])
    del bs[0]


    name_id = []
    for c in bs:
        name_id.append(c.text.replace('\n', ''))
    return name_id

tactics_list  = tactics()

print(f'The tactics are -> {tactics_list}')
print('=' * 30)
print()


def list_sub_techniques():
    options_id = []
    for num in enumerate(tactics_list):
        options_id.append(num)

    print('This are all the tactics available')

    for option in options_id:
        print(option)
    print()

    tactic_option = int(input('Which of the options you want to see the Sub-techniques ? '))
    
    req_sub_technique = requests.get(f'https://attack.mitre.org/techniques/{tactics_list[tactic_option].strip()}')
    bs_tecnique = bs4.BeautifulSoup(req_sub_technique.content, 'html.parser')
    table = bs_tecnique.find_all('a', class_='subtechnique-table-item')

    ids = []
    name = []

    for k,v in enumerate(table):
        if k % 2 ==0:
            ids.append(v.text.strip())
        else:
            name.append(v.text)

    sub_tecniques = zip(ids, name)

    for c in sub_tecniques:
        print(c)

    return ids


ids = list_sub_techniques()
Sub_techniques_option = int(input('which of the Sub-techniques you wanna see ? '))

sub_id = ids[Sub_techniques_option]



def sub_techniques_content():
    mitigation = {}
    Sub_techniques_page = requests.get(f'https://attack.mitre.org/techniques/{sub_id[:5]}/{sub_id[6:]}/')

    bs4_sub_techniques = bs4.BeautifulSoup(Sub_techniques_page.content, 'html.parser')


    descripition = bs4_sub_techniques.find('div', {'class': 'description-body'})
    print('=' * 30)
    print(descripition.text)

    bs = bs4_sub_techniques.find('table',{'class': 'table table-bordered table-alternate mt-2'})
    header = bs.find('tr').text
    header = header.replace('\n', ' ')
    header = header.split(' ')
    del header[0]
    del header[-1]
    
    bs_req_content = bs4_sub_techniques
    tbody = bs_req_content.find_all('tbody')
    tbody = tbody[1].text.strip()
    tbody = tbody.replace('\n\n\n', '#')
    tbody = tbody.split('#')
    for key, value in enumerate(header):
        mitigation[header[key]] = tbody[key]

    print(mitigation)


sub_techniques_content()