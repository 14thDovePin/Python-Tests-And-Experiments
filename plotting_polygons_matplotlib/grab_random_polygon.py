from random import randint
from shapely import Polygon, MultiPolygon

import geopandas as gp


GDF_DIR = ".\\DSA_geodataframe\\assets\\ne_10m_land.shp"


def rr(_list):
    """Return a random element from a list."""
    return _list[randint(0, len(_list))]


def grab_polygon():
    """Return a random polygon from the project `DSA_geodataframe`."""
    gdf = gp.read_file(GDF_DIR)
    gs = gdf['geometry']  # GeoSeries / List of Multi-polygons

    # Select a random geometry.
    geometry = rr(gs)

    # Check and return a polygon.
    if type(geometry) is MultiPolygon:
        polygon = rr(geometry.geoms)
        return polygon
    elif type(geometry) is Polygon:
        return geometry
    else:
        raise Exception('Failed to find a Polygon object.')


if __name__ == "__main__":
    polygon = grab_polygon()
    # Print the object's type and the count of coordinate points.
    print(type(polygon), len(polygon.exterior.coords))
