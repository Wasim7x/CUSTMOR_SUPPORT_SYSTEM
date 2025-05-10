import os
import yaml
from pathlib import Path 
class ConfigClass:
    def __init__(self):
        pass
    def read_yaml(self,config_file_path):
        with open(config_file_path, "r") as file:
            config_data = yaml.safe_load(file)
        return config_data
        
def main():
    file_path = "config/config.yml"
    config_obj = ConfigClass()
    data=config_obj.read_yaml(file_path)
    # print("this is data",data)

if __name__=="__main__":
    main()
