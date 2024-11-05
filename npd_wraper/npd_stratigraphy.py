from .npd_wraper import npd

class stratigraphy(npd):
    def get_cores(self):
        '''
        get core data
        '''
        url_dataset = self._get_total_path(tag_name="strat_litho_wellbore_core")
        return self._get_dataframe_data(url_dataset)

    def get_wellbores(self):
        '''
        get wellbores
        '''
        url_dataset = self._get_total_path(tag_name="strat_litho_wellbore")
        return self._get_dataframe_data(url_dataset)

    def get_overview(self):
        '''
        get overview
        '''
        url_dataset = self._get_total_path(tag_name="strat_litho_overview")
        return self._get_dataframe_data(url_dataset)