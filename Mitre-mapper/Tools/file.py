import pandas as pd
import os
import yaml

class file_writer:
    """
    This class will create the yaml files, the yaml files will be pass as argument on file_creator function.
   
    """

    def file_creator(self,tactic_datas: list, technique_datas: list):
        """
        This function will create the yaml files, the argumens must be lists 
        """

        os.chdir("Mitre-mapper\\Tactics")
        folders = os.listdir()

        df = pd.DataFrame(technique_datas)
        
        for folder in folders:

            os.chdir(folder)
            os.mkdir("Technique")

            with open(f"{folder}.yaml", 'w') as file:
                yaml.dump(tactic_datas[folder], file, sort_keys=False)

            try:
                os.chdir("technique")
                df_filt = (df["Tactic"] == folder)
                a = df.loc[df_filt].to_dict(orient="records")
                for c in a:
                    with open(f"{c['Name']}.yaml", "w") as f:
                        yaml.dump(c, f, sort_keys=False)
            except:
                pass
            os.chdir("../../")
        
