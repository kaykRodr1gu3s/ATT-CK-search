import requests
import bs4

class Techniques_tracker:
    def __init__(self):
        self.link_base = "https://attack.mitre.org/techniques/"

    def collecting(self, links: list):
        all_infos = []
        for link in links:
            print(link)
            test = {}
            technique_description = {}
            technique_information = {}

            req = requests.get(f"{self.link_base}{link}")
            bs4_obj = bs4.BeautifulSoup(req.content, "html.parser")


            name = bs4_obj.find("h1").text
            name = name.replace("\n", "").strip()
            

    
            informations_content =  bs4_obj.find_all("div", class_="col-md-11 pl-0")

            for info in informations_content:
            
                infos = info.find("span", class_="h5 card-title").text.replace(u"\xa0", u"")
            
                if infos == "Sub-techniques:":
                    sub_technique = info.find_all("a")
                    sub_technique_list = [] 
                    for sub_tech in sub_technique:
                        sub_technique_list.append(sub_tech.text)
                    
                    technique_information["Sub-techniques"] = sub_technique_list
                elif infos == "Tactic:" or "Tactics:":
                    tactic_name = info.find_all("a")
                    try:
                        technique_information["Tactic"] = tactic_name[0].text  
                    except:
                        pass
                else:

                    inf = info.text.replace("\n", "").replace(u"\xa0", u"").replace(" ", " ").strip().split(":")
                    technique_information[inf[0]] = inf[1]
            
            

            description = bs4_obj.find("div", class_="description-body")
            technique_description["Description"] = [description.text.replace("\\", "").replace("\n", "")]
            
          
            test["Name"] = name
            test["Tactic"] = technique_information['Tactic']
            test["Description"] = technique_description
            test["Information"] = technique_information
            
            print(test)
            all_infos.append(test)
        
        return all_infos
