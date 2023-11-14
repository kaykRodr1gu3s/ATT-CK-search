import requests
import bs4
import os
import csv


class Writer:
    def __init__(self) -> None:
        self.cloud = ['office365', 'azuread', 'googleworkspace', 'saas', 'iaas']
        self.link_base = 'https://attack.mitre.org/matrices/enterprise/'

    def formating_requests(self, option):
    
        if option in 'cloud_plataforms':
            cloud = []
            for c in self.cloud:
                
                cloud.append(f'{self.link_base}cloud/{c}/')

            return cloud
        else:
            return [f'{self.link_base}{option}/']

    def code(self):
        name = ['pre', 'windows', 'macos','cloud','cloud_plataforms', 'network', 'containers']
        options = [0, 1, 2, 3, 4, 5, 6]

        zipped = zip(options, name)

        for zipp in zipped:
            print(zipp)

        print('-=' * 20)
        option = int(input('Which option do you wanna see: '))
        main = Writer()
        a = main.formating_requests(name[option])

        current = os.getcwd() + '\\Enterprise\\Matrices'
        
        for key,v in enumerate(a):

            req = requests.get(v)
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

            if len(a) > 1:
                current = os.getcwd() + '\\Enterprise\\Matrices\\Cloud_plataforms'
                with open(f'{current}\\{self.cloud[key]}.csv', 'w', newline='') as f:
                    csv_writer = csv.writer(f)
                    csv_writer.writerow(dict_names.keys())
                    csv_writer.writerow(dict_names.values())

            with open(f'{current}\\{name[option]}.csv', 'w', newline='') as f:
                csv_writer = csv.writer(f)
                csv_writer.writerow(dict_names.keys())
                csv_writer.writerow(dict_names.values())
    
instance = Writer()
instance.code()