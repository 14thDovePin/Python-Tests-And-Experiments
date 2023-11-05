"""
GeoDataFrame is a Data Structure of the Geopandas library.
More information can be found from their website here:
    https://geopandas.org/

These experiments were written for a hands on experience with working
on this type of data structure, and also learn a few of its methods and
attribtues.
"""


from shapely import Polygon, MultiPolygon

import geopandas as gp


GDF_DIR = '.\\DSA_geodataframe\\assets\\ne_10m_land.shp' 


def main():
    gdf = gp.read_file(GDF_DIR)
    gs = gdf['geometry']  # GeoSeries

    polygons = []

    # Extract all polygon from dataset.
    for polygon in gs:
        if type(polygon) is Polygon:
            polygons.append(polygon)
        elif type(polygon) is MultiPolygon:
            for i in polygon.geoms:
                polygons.append(i)

    print(len(polygons))


if __name__ == '__main__':
    main()
