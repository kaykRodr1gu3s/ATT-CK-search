import requests
import bs4
import os
import csv

def writer(option):


    os.chdir(f'{os.getcwd()}\\Enterprise')
    op = option
    
    
    if op in 'cloud':
        current = os.getcwd() + '\\Matrices\\cloud'
   
        cloud_plataform = ['office365', 'azuread', 'googleworkspace', 'saas', 'iaas']
        for plataform in cloud_plataform:
            req = requests.get(f'https://attack.mitre.org/matrices/enterprise/cloud/{plataform}/')

            print(req)


            bs = bs4.BeautifulSoup(req.content, 'html.parser')

            table = bs.find('table', {'class': 'matrix flat'})

            tactics_name = table.find_all('td', {'class': 'tactic name'})

            names = []
            count = []

            for c in tactics_name:
                names.append(c.text)


            tech_count = table.find_all('td', {'class': 'tactic count'})

            for c in tech_count:
                count.append(c.text.replace(u'\xa0', u' ').replace('\n', '').strip())

            dict_names = {} 

            for k, v in enumerate(names):
                dict_names[names[k]] = count[k]



            with open(f'{current}\\{plataform}.csv', 'w', newline='') as f:
                csv_writer = csv.writer(f)
                csv_writer.writerow(dict_names.keys())
                csv_writer.writerow(dict_names.values())



    else:
        current = os.getcwd() + '\\Matrices'

        req = requests.get(f'https://attack.mitre.org/matrices/enterprise/{option}/')

        print(req)


        bs = bs4.BeautifulSoup(req.content, 'html.parser')

        table = bs.find('table', {'class': 'matrix flat'})

        tactics_name = table.find_all('td', {'class': 'tactic name'})

        names = []
        count = []

        for c in tactics_name:
            names.append(c.text)


        tech_count = table.find_all('td', {'class': 'tactic count'})

        for c in tech_count:
            count.append(c.text.replace(u'\xa0', u' ').replace('\n', '').strip())

        dict_names = {} 

        for k, v in enumerate(names):
            dict_names[names[k]] = count[k]


        with open(f'{current}\\{option}.csv', 'w', newline='') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(dict_names.keys())
            csv_writer.writerow(dict_names.values())


name = ['pre', 'windows', 'macos', 'cloud', 'network', 'containers']
options = [0, 1, 2, 3, 4, 5]

zipped = zip(options, name)


for zipp in zipped:
    print(zipp)

print('-=' * 20)
option = int(input('Which do you wanna see ? '))
print('-=' * 20)

writer(name[option])