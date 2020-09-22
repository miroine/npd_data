import requests
import json
import pandas as pd
import numpy as np
from datetime import datetime



class npd():
    '''
    class to get data from npd_data based on API requests
    extracting from http://hotell.difi.no/api/json/npd/
    '''
    def __init__(self):
        self.npd_path= "http://hotell.difi.no/api/json/npd/"

    def _get_dataframe_data(self, url_dataset):
        data = requests.get(
            url_dataset + '?page=1').json()

        page = data['pages']

        all_data_list =[]
        for i in range(0,page):
            url= url_dataset+f'?page={i+1}'
            dataset_all_json =requests.get(url).json()
            number_of_entries=len(dataset_all_json['entries'])

            for entry in range(0,number_of_entries):
                all_data_list.append(dataset_all_json['entries'][entry])

        return pd.DataFrame(all_data_list)


