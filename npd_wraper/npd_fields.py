from .npd_wraper import npd
from datetime import datetime
import pandas as pd


class field(npd):

    def get_field_production_monthly(self, field_name='all'):
        '''
        Get production per field on monthly basis
        example:
        field().get_field_production_monthly()
        return a dataframe
        optional argument are field name currently defaulted to all fields
        could select one field
        '''
        url_dataset=self.npd_path+"field/production-monthly-by-field"
        df = self._get_dataframe_data(url_dataset)
        df["Date"] = df.apply(lambda row: datetime(int(row['prfYear']),int(row['prfMonth']), 1),axis=1)
        df["Date"]=pd.to_datetime(df.Date)
        df.set_index("Date", inplace=True)
        cols = ["prfInformationCarrier", "prfPrdOilNetMillSm3", "prfPrdGasNetBillSm3",
                "prfPrdNGLNetMillSm3", "prfPrdCondensateNetMillSm3", "prfPrdOeNetMillSm3",
                "prfPrdProducedWaterInFieldMillSm3"]
        # make columns as numeric
        for col in df.drop(["prfInformationCarrier"], axis=1).columns:
            df[col]=df[col].astype("float")
        if field_name == "all":
            return  df[cols]
        else:
            if field_name.upper() not in df["prfInformationCarrier"].unique():
                raise ValueError("field name needs to be one of this name:", df["prfInformationCarrier"].unique())
            return df[df["prfInformationCarrier"]==field_name.upper()][cols]

    def get_field_production_yearly(self, field_name="all"):
        '''
        Get production per field on yearly basis
        example:
        field().get_field_production_yearly()
        return a dataframe
        optional argument are field name currently defaulted to all fields
        could select one field
        '''
        url_dataset = self.npd_path+"field/production-yearly-by-field"
        df= self._get_dataframe_data(url_dataset).set_index('prfYear')

        if field_name == "all":
            return  df
        else:
            if field_name.upper() not in df["prfInformationCarrier"].unique():
                raise ValueError("field name needs to be one of this name:", df["prfInformationCarrier"].unique())
            return df[df["prfInformationCarrier"]==field_name.upper()]

    def get_all_fields_cumulative_production(self):
        '''
        return: cumulative production for all fields

        '''
        url_dataset=self.npd_path+"field/production-yearly-total"
        df= self._get_dataframe_data(url_dataset).set_index('prfYear')
        return df



    def get_field_description(self, field_name="all"):
        '''
        return: field description
        field_name : optional argument to filter the dataframe for each field
        '''

        url_dataset=self.npd_path+"field/description"
        df= self._get_dataframe_data(url_dataset)
        if field_name == "all":
            return  df
        else:
            if field_name.upper() not in df['fldName'].unique():
                raise ValueError("field name needs to be one of this name:", df['fldName'].unique())
            return df[df['fldName']==field_name.upper()]

    def get_field_inplace_volume(self, field_name="all"):
        '''
        return: get field in place volume
        field_name: return field inplace for a specific
        '''
        url_dataset= self.npd_path+"field/in-place-volumes"
        df= self._get_dataframe_data(url_dataset)

        for col in df.drop(['fldName','fldDateOffResEstDisplay','fldNpdidField','DatesyncNPD'],axis=1).columns:
            df[col] = df[col].astype("float")
        if field_name == "all":
            return df
        else:
            if field_name.upper() not in df['fldName'].unique():
                raise ValueError("field name needs to be one of this name:", df['fldName'].unique())
            return df[df['fldName'] == field_name.upper()]

    def get_field_licenses(self, field_name="all"):
        '''
        return field licensees
        field_name: filter the dataframe for each specific field
        '''
        url_dataset= self.npd_path+"field/licensees"
        df= self._get_dataframe_data(url_dataset)
        if field_name == "all":
            return df
        else:
            if field_name.upper() not in df['fldName'].unique():
                raise ValueError("field name needs to be one of this name:", df['fldName'].unique())
            return df[df['fldName'] == field_name.upper()]

    def get_field_operators(self, field_name="all"):
        '''
        return field operators
        field_name: filter the dataframe for specific field
        '''
        url_dataset= self.npd_path+"field/operators"
        df= self._get_dataframe_data(url_dataset)
        if field_name == "all":
            return df
        else:
            if field_name.upper() not in df['fldName'].unique():
                raise ValueError("field name needs to be one of this name:", df['fldName'].unique())
            return df[df['fldName'] == field_name.upper()]


    def get_field_overview(self, field_name="all"):
        '''
        return: field overview
        field_name: filiter field overview for a specific field
        '''
        url_dataset = self.npd_path+"field/overview"
        df= self._get_dataframe_data(url_dataset)
        if field_name == "all":
            return df
        else:
            if field_name.upper() not in df['fldName'].unique():
                raise ValueError("field name needs to be one of this name:", df['fldName'].unique())
            return df[df['fldName'] == field_name.upper()]

    def get_field_owners(self, field_name="all"):
        '''
        return field owners
        '''
        url_dataset=self.npd_path+"field/owners"
        df= self._get_dataframe_data(url_dataset)
        if field_name == "all":
            return df
        else:
            if field_name.upper() not in df['fldName'].unique():
                raise ValueError("field name needs to be one of this name:", df['fldName'].unique())
            return df[df['fldName'] == field_name.upper()]

    def get_field_reserves(self, field_name="all"):
        '''
        return field reserves
        '''
        url_dataset=self.npd_path+"field/reserves"
        df= self._get_dataframe_data(url_dataset)
        if field_name == "all":
            return df
        else:
            if field_name.upper() not in df['fldName'].unique():
                raise ValueError("field name needs to be one of this name:", df['fldName'].unique())
            return df[df['fldName'] == field_name.upper()]


    def get_field_status(self, field_name="all"):
        '''
        return field status
        '''
        url_dataset=self.npd_path+"field/status"
        df= self._get_dataframe_data(url_dataset)
        if field_name == "all":
            return df
        else:
            if field_name.upper() not in df['fldName'].unique():
                raise ValueError("field name needs to be one of this name:", df['fldName'].unique())
            return df[df['fldName'] == field_name.upper()]

    def get_field_investments(self, field_name="all"):
        '''
        get field investment yearly
        return dataframe
        field_name: optional arguments to filter based on field_name
        '''
        url_dataset=self.npd_path+"investments/yearly-by-field"
        df= self._get_dataframe_data(url_dataset)
        df['prfInvestmentsMillNOK']=df['prfInvestmentsMillNOK'].astype("float")
        if field_name == "all":
            return df
        else:
            if field_name.upper() not in df['prfInformationCarrier'].unique():
                raise ValueError("field name needs to be one of this name:", df['prfInformationCarrier'].unique())
            return df[df['prfInformationCarrier'] == field_name.upper()]



