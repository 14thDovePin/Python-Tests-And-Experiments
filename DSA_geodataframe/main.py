"""
GeoDataFrame is a Data Structure of the Geopandas library.
More information can be found from their website here:
    https://geopandas.org/

These experiments were written for a hands on experience with working
on this type of data structure, and also learn a few of its methods and
attribtues.
"""


import geopandas as gp


# Parent Directory
PD = '.\\DSA_geodataframe'
# GeoDataFrame
GDF_FILE = PD + '\\assets\\ne_10m_land.shp' 
GDF = gp.read_file(GDF_FILE)


def main():
    print(GDF)


if __name__ == '__main__':
    main()
