import requests
import json
import pandas as pd
import numpy as np
from datetime import datetime
from io import StringIO



class npd():
    '''
    class to get data from npd_data based on API requests
    extracting from http://hotell.difi.no/api/json/sodir/
    '''
    
    def __init__(self):
        '''
        Initialize npd_data class with path to npd_data API.
        '''


    def _get_total_path(self, tag_name):
        '''
        Construct the total path for a given tag.
        '''
        SODIR_PATH= f"https://factpages.sodir.no/public?/Factpages/external/tableview/{tag_name}&rs:Command=Render&rc:Toolbar=false&rc:Parameters=f&IpAddress=not_used&CultureCode=en&rs:Format=CSV&Top100=false"
        return SODIR_PATH
    def _get_dataframe_data(self, url_dataset):
        response = requests.get(
            url_dataset)
        df = pd.DataFrame()
        # Check if the request was successful
        if response.status_code == 200:
            # Load CSV data into a DataFrame
            df = pd.read_csv(StringIO(response.text))
        else:
            print(f"Something wrong with the API: {response.status_code}")
        return df
