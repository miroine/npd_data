from .npd_wraper import npd

class facility(npd):

    def get_fixed_facilities(self):
        '''
        get the fixed facilities
        '''
        url_dataset = self._get_total_path(tag_name="facility_fixed")
        return self._get_dataframe_data(url_dataset)

    def get_movable_facilities(self):
        '''
        get movable facilities
        '''
        url_dataset = self._get_total_path(tag_name="facility_moveable")
        return self._get_dataframe_data(url_dataset)