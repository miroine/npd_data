from .npd_wraper import npd

class discovery(npd):
    def get_discovery_overview(self):
        '''
        overview of all the discoveries
        '''
        url_dataset=self.npd_path+"discovery/overview"
        return self._get_dataframe_data(url_dataset)

