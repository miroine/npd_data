from .npd_wraper import npd

class baa(npd):
    def get_baa_area(self):
        '''
        get block area
        '''
        url_dataset = self._get_total_path(tag_name="bsns_arr_area_area_poly_hst")
        return self._get_dataframe_data(url_dataset)

    def get_baa_licensees(self):
        '''
        return: get blocks licenses
        '''
        url_dataset = self._get_total_path(tag_name="bsns_arr_area_licensee_hst")
        return self._get_dataframe_data(url_dataset)

    def get_baa_operators(self):
        '''
        return: get blocks licenses
        '''
        url_dataset = self._get_total_path(tag_name="bsns_arr_area")
        return self._get_dataframe_data(url_dataset)

    def get_baa_overview(self):
        '''
        return: get block overview
        '''

        url_dataset = self._get_total_path(tag_name="bsns_arr_area")
        return self._get_dataframe_data(url_dataset)

    def get_baa_transfers(self):
        '''
        get block transfers
        '''
        url_dataset = self._get_total_path(tag_name="bsns_arr_area_transfer_hst")
        return self._get_dataframe_data(url_dataset)
    
    def get_baa_co2(self):
        '''
        get block transfers
        '''
        url_dataset = self._get_total_path(tag_name="bsns_arr_area_co2")
        return self._get_dataframe_data(url_dataset)

