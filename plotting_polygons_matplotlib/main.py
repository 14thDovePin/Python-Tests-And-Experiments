"""
In this test, I'll be using the `matplotlib` library to plot a polygon
object from the `shapely` library and other related test you'll see.
"""


import matplotlib.pyplot as plt

from grab_random_polygon import grab_polygon


def main():
    # Polygon coordinates
    x, y = [], []
    polygon = grab_polygon()

    # Sequence all x and y coordinates respectively.
    coordinates = polygon.exterior.coords
    for cord in coordinates:
        x.append(cord[0])
        y.append(cord[1])

    # Plot polygon in matplotlib.
    plt.fill(x, y)
    plt.show()


if __name__ == '__main__':
    main()
