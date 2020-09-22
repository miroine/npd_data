from .npd_wraper import npd

class discovery(npd):
    def get_discovery_overview(self, discovery_year="all"):
        '''
        overview of all the discoveries
        '''
        url_dataset=self.npd_path+"discovery/overview"
        df= self._get_dataframe_data(url_dataset)
        if discovery_year != "all":
            df['dscDiscoveryYear']=df['dscDiscoveryYear'].astype("int")

            if discovery_year not in df.dscDiscoveryYear.unique():
                raise ValueError ("discovery year should be in this range", df.dscDiscoveryYear.unique())
            df = df[df.dscDiscoveryYear == discovery_year]

        return df

