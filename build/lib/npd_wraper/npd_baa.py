from .npd_wraper import npd

class baa(npd):
    def get_baa_area(self):
        '''
        get block area
        '''
        url_dataset=self.npd_path+"baa/area"
        return self._get_dataframe_data(url_dataset)

    def get_baa_licensees(self):
        '''
        return: get blocks licenses
        '''
        url_dataset=self.npd_path+"baa/licensees"
        return self._get_dataframe_data(url_dataset)

    def get_baa_operators(self):
        '''
        return: get blocks licenses
        '''
        url_dataset=self.npd_path+"baa/operators"
        return self._get_dataframe_data(url_dataset)

    def get_baa_overview(self):
        '''
        return: get block overview
        '''

        url_dataset=self.npd_path+"baa/overview"
        return self._get_dataframe_data(url_dataset)

    def get_baa_transfers(self):
        '''
        get block transfers
        '''
        url_dataset=self.npd_path+"baa/transfers"
        return self._get_dataframe_data(url_dataset)

