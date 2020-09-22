from .npd_wraper import npd

class stratigraphy(npd):
    def get_cores(self):
        '''
        get core data
        '''
        url_dataset=self.npd_path+"stratigraphy/cores"
        return self._get_dataframe_data(url_dataset)

    def get_wellbores(self):
        '''
        get wellbores
        '''
        url_dataset=self.npd_path+"stratigraphy/wellbores"
        return self._get_dataframe_data(url_dataset)