"""
GeoDataFrame is a Data Structure of the Geopandas library.
More information can be found from their website over at
`LINKS.txt > [001]`.

These experiments were written for a hands on experience with working
on this type of data structure, and also learn a few of its methods and
attribtues.
"""


from shapely import Polygon, MultiPolygon

import geopandas as gp


GDF_DIR = '.\\assets\\ne_10m_land.shp' 


def main():
    gdf = gp.read_file(GDF_DIR)
    gs = gdf['geometry']  # GeoSeries

    print(gs)


if __name__ == '__main__':
    main()
