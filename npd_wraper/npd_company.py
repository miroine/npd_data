from .npd_wraper import npd

class company(npd):
    def get_all_companies(self):
        '''
        get all companies
        '''
        url_dataset=self.npd_path+"company/all"
        return self._get_dataframe_data(url_dataset)

    def get_company_reserves(self):
        '''
        get reserves for each company
        '''
        url_dataset=self.npd_path+"company/reserves"
        return self._get_dataframe_data(url_dataset)