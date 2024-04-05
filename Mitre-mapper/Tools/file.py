import pandas as pd
import os
import yaml

print(os.getcwd())
os.chdir("Mitre-mapper\\Tactics")
class file_writer:
    def file_creator(self, datas):
        folders = os.listdir()
        df = pd.DataFrame(datas)
        for folder in folders:
            os.chdir(folder)
            try:
                df_filt = (df["Tactic"] == folder)
                a = df.loc[df_filt].to_dict(orient="records")
                for c in a:
                    with open(f"{c['Name']}.yaml", "w") as f:
                        yaml.dump(c, f, sort_keys=False)
            except:
                pass
            os.chdir("../")
        
