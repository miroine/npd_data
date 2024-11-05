from .npd_wraper import npd
import geopandas as gpd


class npd_shape(npd):
    '''
    class to load the shape files as a geopandas instance

    '''
    def __init__(self):
        super(npd, self).__init__()
        self.shape_dict={
            "afex": "https://factpages.npd.no/downloads/shape/afxAreaCurrent.zip",
            "afex_block": "https://factpages.npd.no/downloads/shape/afxAreaSplitByBlock.zip",
            "license": "https://factpages.npd.no/downloads/shape/prlAreaCurrent.zip",
            "license_block": "https://factpages.npd.no/downloads/shape/prlAreaSplitByBlock.zip",
            "license_apa_gross": "https://factpages.npd.no/downloads/shape/apaAreaGross.zip",
            "license_apa_net": "https://factpages.npd.no/downloads/shape/apaAreaNet.zip",
            "wellbore": "https://factpages.npd.no/downloads/shape/wlbPoint.zip",
            "baa_blocks": "https://factpages.npd.no/downloads/shape/baaAreaSplitByBlock.zip",
            "field": "https://factpages.npd.no/downloads/shape/fldArea.zip",
            "discovery": "https://factpages.npd.no/downloads/shape/dscArea.zip",
            "facility": "https://factpages.npd.no/downloads/shape/fclPoint.zip",
            "tuf": "https://factpages.npd.no/downloads/shape/pipLine.zip",
            "block": "https://factpages.npd.no/downloads/shape/blkArea.zip",
            "quadrant": "https://factpages.npd.no/downloads/shape/qadArea.zip",
            "subarea": "https://factpages.npd.no/downloads/shape/subArea.zip"
        }
    def get_afex(self):
        return gpd.read_file(self.shape_dict["afex"])

    def get_license(self):
        return gpd.read_file(self.shape_dict["license"])

    def get_afex_block(self):
        return gpd.read_file(self.shape_dict["afex_block"])

    def get_license_block(self):
        return gpd.read_file(self.shape_dict["license_block"])

    def get_license_apa_gross(self):
        return gpd.read_file(self.shape_dict["license_apa_gross"])

    def get_license_apa_net(self):
        return gpd.read_file(self.shape_dict["license_apa_net"])

    def get_wellbore(self):
        return gpd.read_file(self.shape_dict["wellbore"])

    def get_baa_blocks(self):
        return gpd.read_file(self.shape_dict["baa_blocks"])

    def get_field(self):
        return gpd.read_file(self.shape_dict["field"])

    def get_discovery(self):
        return gpd.read_file(self.shape_dict["discovery"])

    def get_facility(self):
        return gpd.read_file(self.shape_dict["facility"])

    def get_tuf(self):
        return gpd.read_file(self.shape_dict["tuf"])

    def get_block(self):
        return gpd.read_file(self.shape_dict["block"])

    def get_quadrant(self):
        return gpd.read_file(self.shape_dict["quadrant"])

    def get_subarea(self):
        return gpd.read_file(self.shape_dict["subarea"])