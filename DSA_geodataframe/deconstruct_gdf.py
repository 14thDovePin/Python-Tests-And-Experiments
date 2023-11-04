import geopandas as gp


GDF_DIR = '.\\DSA_geodataframe\\assets\\ne_10m_land.shp' 

def deconstruct(dir):
    # Readfile & deconstruct datastructure step by step.
    gdf = gp.read_file(dir)  # GeoDataFrame / Pandas DataFrame
    gs = gdf['geometry']  # GeoSeries / List of Multi-polygons
    mp0 = gs[0]  # Multi-polygon
    polygons = mp0.geoms  # Geometry Collection / List of Polygons
    polygon = polygons[0]  # Polygon
    lr = polygon.exterior  # Linear Ring
    cords = lr.coords  # Coordinates

    print(f'Total Coordinatres of Polygon_0: {len(cords)}')


if __name__ == '__main__':
    deconstruct(GDF_DIR)
