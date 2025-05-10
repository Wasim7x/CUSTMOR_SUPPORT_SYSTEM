import pandas as pd
from langchain_core.documents import Document
import sys
from pathlib import Path
sys.path[0]=str(Path(__file__).parent.parent)
from config.config import ConfigClass

class data_conveter:
    def __init__(self, data_path:str):
        print("Reading data from:", data_path)
        self.product_data = pd.read_csv(data_path)
        # print(self.product_data.head())

    def data_transformation(self):
        required_columns = self.product_data.columns
        required_columns = list(required_columns[1:])
        # print(required_columns)
        product_list = []
        for index, row in self.product_data.iterrows():

            object = {
                "product_name": row['product_title'],
                "product_rating": row['rating'],
                "product_summary": row['summary'],
                "product_review": row['review']
            }
            product_list.append(object)
        # print("_----------this is product_list-----------")
        # print(product_list[0])

        docs = []
        for entry in product_list:
            metadata = {"product_name":entry["product_name"],
                        "product_rating":entry["product_rating"],
                        "product_summary":entry["product_summary"],
                        "product_review":entry["product_review"]
                        }
            doc = Document(page_content=entry['product_review'], metadata= metadata)
            docs.append(doc)
        print(docs[0])
def main():
    try:
        config_data = ConfigClass().read_yaml("config/config.yml")
        data_path = config_data["data_path"]
        data_con= data_conveter(data_path)
        data_con.data_transformation()
    except Exception as e:
        print("Exception",e)      

if __name__ == '__main__':
    main()