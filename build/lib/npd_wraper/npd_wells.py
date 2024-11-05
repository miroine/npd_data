import pandas as pd 
from .npd_wraper import npd


class well_data(npd):
    def get_exploration_wells(self, field_name="all", area="all", content="all", completion_year="all"):
        '''
        return: get all exploration wells
        field_name: optional to filter by fields
        area: optional to filter by area
        content: display which phase was encouter on the well

        '''

        url_dataset = self._get_total_path(tag_name="wellbore_exploration_all")
        df= self._get_dataframe_data(url_dataset)
        if content != "all":
            if content.upper() not in df['wlbContent'].unique():
                raise ValueError("Content needs to be one of this ", df['wlbContent'].unique())
            df = df[df['wlbContent']==content.upper()]
        if field_name != "all":
            if field_name.upper() not in df['wlbField'].unique():
                raise ValueError("field name needs to be one of this name:", df['wlbField'].unique())
            df= df[df['wlbField'] == field_name.upper()]
        if area !="all":
            if area.upper() not in df['wlbMainArea'].unique():
                raise ValueError("Area name needs to be one of those names", df['wlbMainArea'].unique())
            df = df[df['wlbMainArea'] == area.upper()]
        if completion_year !="all":
            df['wlbCompletionYear']=df['wlbCompletionYear'].astype("int")
            if completion_year not in df['wlbCompletionYear'].unique():
                raise ValueError("Content needs to be one of this ", df['wlbCompletionYear'].unique())
            df = df[df['wlbCompletionYear'] == completion_year]

        return df


    def get_development_wells(self, field_name="all", area="all", content="all", completion_year="all"):
        '''
        return get development wells
        '''

        url_dataset = self._get_total_path(tag_name="wellbore_development_all")
        df= self._get_dataframe_data(url_dataset)



        if content != "all":
            if content.upper() not in df['wlbContent'].unique():
                raise ValueError("Content needs to be one of this ", df['wlbContent'].unique())
            df = df[df['wlbContent']==content.upper()]
        if field_name != "all":
            if field_name.upper() not in df['wlbField'].unique():
                raise ValueError("field name needs to be one of this name:", df['wlbField'].unique())
            df= df[df['wlbField'] == field_name.upper()]
        if area !="all":
            if area.upper() not in df['wlbMainArea'].unique():
                raise ValueError("Area name needs to be one of those names", df['wlbMainArea'].unique())
            df = df[df['wlbMainArea'] == area.upper()]
        if completion_year !="all":
            df['wlbCompletionYear']=df['wlbCompletionYear'].astype("int")
            if completion_year not in df['wlbCompletionYear'].unique():
                raise ValueError("Content needs to be one of this ", df['wlbCompletionYear'].unique())
            df = df[df['wlbCompletionYear'] == completion_year]

        return df


    def get_all_wells(self, field_name="all", area="all", content="all", completion_year="all"):
        '''
        return get development wells
        '''

        url_dataset = self._get_total_path(tag_name="wellbore_all_long")
        df= self._get_dataframe_data(url_dataset)



        if content != "all":
            if content.upper() not in df['wlbContent'].unique():
                raise ValueError("Content needs to be one of this ", df['wlbContent'].unique())
            df = df[df['wlbContent']==content.upper()]
        if field_name != "all":
            if field_name.upper() not in df['wlbField'].unique():
                raise ValueError("field name needs to be one of this name:", df['wlbField'].unique())
            df= df[df['wlbField'] == field_name.upper()]
        if area !="all":
            if area.upper() not in df['wlbMainArea'].unique():
                raise ValueError("Area name needs to be one of those names", df['wlbMainArea'].unique())
            df = df[df['wlbMainArea'] == area.upper()]
        if completion_year !="all":
            df['wlbCompletionYear']=df['wlbCompletionYear'].astype("int")
            if completion_year not in df['wlbCompletionYear'].unique():
                raise ValueError("Content needs to be one of this ", df['wlbCompletionYear'].unique())
            df = df[df['wlbCompletionYear'] == completion_year]

        return df

    def get_shallow_wells(self):
        '''
        return get shallow wells
        '''

        url_dataset = self._get_total_path(tag_name="wellbore_other_all")
        return self._get_dataframe_data(url_dataset)

    def get_wells_with_casing_and_leak_off(self):
        '''
        return get wells with casing and leak off
        '''

        url_dataset = self._get_total_path(tag_name="wellbore_casing_and_lot")
        return self._get_dataframe_data(url_dataset)

    def get_wells_with_coordinates(self):
        '''
        return get wells with coordinates
        '''

        url_dataset = self._get_total_path(tag_name="wellbore_coordinates")
        return self._get_dataframe_data(url_dataset)

    def get_wells_with_core_photos(self):
        '''
        return get wells with core photos
        '''

        url_dataset = self._get_total_path(tag_name="wellbore_core_photo")
        return self._get_dataframe_data(url_dataset)

    def get_wells_with_cores(self):
        '''
        return get wells with cores
        '''

        url_dataset = self._get_total_path(tag_name="wellbore_core")
        return self._get_dataframe_data(url_dataset)

    def get_wells_with_documents(self):
        '''
        return: get wells containing documentation
        '''

        url_dataset = self._get_total_path(tag_name="wellbore_document")
        return self._get_dataframe_data(url_dataset)

    def get_wells_with_dst(self):
        '''
        return: get wells with dst
        '''

        url_dataset = self._get_total_path(tag_name="wellbore_dst")
        return self._get_dataframe_data(url_dataset)

    def get_wells_with_drilling_mud(self):
        '''
        return: get wells with drilling mud
        '''

        url_dataset = self._get_total_path(tag_name="wellbore_mud")
        return self._get_dataframe_data(url_dataset)


    def get_wells_with_history(self):
        '''
        return: get wells with hisotry
        '''

        url_dataset = self._get_total_path(tag_name="wellbore_history")
        return self._get_dataframe_data(url_dataset)

    def get_wells_with_lithostratigraphy(self):
        '''
        return: get wells with lithostratigraphy
        '''

        url_dataset = self._get_total_path(tag_name="wellbore_formation_top")
        return self._get_dataframe_data(url_dataset)

    def get_wells_with_npdid(self):

        '''
        return wells with npdid
        '''
        url_dataset = self._get_total_path(tag_name="wellbore_npdid_overview")
        return self._get_dataframe_data(url_dataset)

    def get_wells_with_oilsamples(self):

        '''
        return wells with npdid
        '''
        url_dataset = self._get_total_path(tag_name="wellbore_oil_sample")
        return self._get_dataframe_data(url_dataset)

    def get_wells_with_co2(self):

        '''
        return wells with co2
        '''
        url_dataset = self._get_total_path(tag_name="wellbore_co2")
        return self._get_dataframe_data(url_dataset)

    def get_wells_with_thin_section(self):

        '''
        return wells with thin section
        '''
        url_dataset = self._get_total_path(tag_name="wellbore_thin_section")
        return self._get_dataframe_data(url_dataset)

    def get_wells_prognosis(self):

        '''
        get well prognosis
        '''
        url_dataset = "https://factpages.sodir.no/pbl/wellbore_general/PrognosisResultData_Released.csv"
        return pd.read_csv(url_dataset)