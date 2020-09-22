from .npd_wraper import npd
from datetime import datetime
import pandas as pd


class field(npd):

    def get_field_production_monthly(self):
        '''
        get monthly production
        '''
        url_dataset=self.npd_path+"field/production-monthly-by-field"
        df = self._get_dataframe_data(url_dataset)
        df["Date"] = df.apply(lambda row: datetime(int(row['prfYear']),int(row['prfMonth']), 1),axis=1)
        df["Date"]=pd.to_datetime(df.Date)
        df.set_index("Date", inplace=True)
        cols = ["prfInformationCarrier", "prfPrdOilNetMillSm3", "prfPrdGasNetBillSm3",
                "prfPrdNGLNetMillSm3", "prfPrdCondensateNetMillSm3", "prfPrdOeNetMillSm3",
                "prfPrdProducedWaterInFieldMillSm3"]
        return  df[cols]

    def get_field_production_yearly(self):
        '''
        return: production yearly data
        '''
        url_dataset = self.npd_path+"field/production-yearly-by-field"
        return self._get_dataframe_data(url_dataset).set_index('prfYear')

    def get_field_cumulative_production(self):
        '''
        return: cumulative production
        '''
        url_dataset=self.npd_path+"field/production-yearly-total"

        return self._get_dataframe_data(url_dataset).set_index('prfYear')

    def get_field_description(self):
        '''
        return: field description
        '''

        url_dataset=self.npd_path+"field/description"
        return self._get_dataframe_data(url_dataset)

    def get_field_inplace_volume(self):
        '''
        return: get field in place volume
        '''
        url_dataset= self.npd_path+"field/in-place-volumes"
        return self._get_dataframe_data(url_dataset)

    def get_field_licenses(self):
        '''
        return field licensees
        '''
        url_dataset= self.npd_path+"field/licensees"
        return self._get_dataframe_data(url_dataset)

    def get_field_operators(self):
        '''
        return field operators
        '''
        url_dataset= self.npd_path+"field/operators"
        return self._get_dataframe_data(url_dataset)

    def get_field_overview(self):
        '''
        return: field overview
        '''
        url_dataset = self.npd_path+"field/overview"
        return self._get_dataframe_data(url_dataset)

    def get_field_owners(self):
        '''
        return field owners
        '''
        url_dataset=self.npd_path+"field/owners"
        return self._get_dataframe_data(url_dataset)

    def get_field_reserves(self):
        '''
        return field reserves
        '''
        url_dataset=self.npd_path+"field/reserves"
        return self._get_dataframe_data(url_dataset)

    def get_field_status(self):
        '''
        return field status
        '''
        url_dataset=self.npd_path+"field/status"
        return self._get_dataframe_data(url_dataset)

    def get_field_investments(self):
        '''
        get field investment yearly
        '''
        url_dataset=self.npd_path+"investments/yearly-by-field"
        return self._get_dataframe_data(url_dataset)



