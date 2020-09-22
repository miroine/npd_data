from .npd_wraper import npd


class well_data(npd):
    def get_exploration_wells(self):
        '''
        return: get all exploration wells
        '''

        url_dataset = self.npd_path + "wellbore/exploration"
        return self._get_dataframe_data(url_dataset)

    def get_development_wells(self):
        '''
        return get development wells
        '''

        url_dataset = self.npd_path + "wellbore/development"
        return self._get_dataframe_data(url_dataset)

    def get_shallow_wells(self):
        '''
        return get shallow wells
        '''

        url_dataset = self.npd_path + "wellbore/shallow"
        return self._get_dataframe_data(url_dataset)

    def get_wells_with_casing_and_leak_off(self):
        '''
        return get wells with casing and leak off
        '''

        url_dataset = self.npd_path + "wellbore/with-casing-and-leak-off"
        return self._get_dataframe_data(url_dataset)

    def get_wells_with_coordinates(self):
        '''
        return get wells with coordinates
        '''

        url_dataset = self.npd_path + "wellbore/with-coordinates"
        return self._get_dataframe_data(url_dataset)

    def get_wells_with_core_photos(self):
        '''
        return get wells with core photos
        '''

        url_dataset = self.npd_path + "wellbore/with-core-photos"
        return self._get_dataframe_data(url_dataset)

    def get_wells_with_cores(self):
        '''
        return get wells with cores
        '''

        url_dataset = self.npd_path + "wellbore/with-cores"
        return self._get_dataframe_data(url_dataset)

    def get_wells_with_documents(self):
        '''
        return: get wells containing documentation
        '''

        url_dataset = self.npd_path + "wellbore/with-documents"
        return self._get_dataframe_data(url_dataset)

    def get_wells_with_dst(self):
        '''
        return: get wells with dst
        '''

        url_dataset = self.npd_path + "wellbore/with-drill-stem-tests"
        return self._get_dataframe_data(url_dataset)

    def get_wells_with_drilling_mud(self):
        '''
        return: get wells with drilling mud
        '''

        url_dataset = self.npd_path + "wellbore/with-drilling-mud"
        return self._get_dataframe_data(url_dataset)


    def get_wells_with_history(self):
        '''
        return: get wells with hisotry
        '''

        url_dataset = self.npd_path + "wellbore/with-history"
        return self._get_dataframe_data(url_dataset)

    def get_wells_with_lithostratigraphy(self):
        '''
        return: get wells with lithostratigraphy
        '''

        url_dataset = self.npd_path + "wellbore/with-lithostratigraphy"
        return self._get_dataframe_data(url_dataset)

    def get_wells_with_npdid(self):

        '''
        return wells with npdid
        '''
        url_dataset = self.npd_path + "wellbore/with-npdid"
        return self._get_dataframe_data(url_dataset)

    def get_wells_with_oilsamples(self):

        '''
        return wells with npdid
        '''
        url_dataset = self.npd_path + "wellbore/with-oil-samples"
        return self._get_dataframe_data(url_dataset)