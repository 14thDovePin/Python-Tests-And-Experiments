"""
The purpose of this test is to plot the data from a mockup csv file
named `DATA_0.TXT` for 14DovePin's group research purposes.
"""


import csv

from datetime import datetime, timedelta

import matplotlib.pyplot as plt
import pandas as pd

from matplotlib.dates import DateFormatter


CSV_FILE = '.\\plotting_research_data\\DATA_0.csv'
# Use `Hour:Minute` Millitary Time Format
EST_TS = '12:18'  # Estimated Time Start
# Date: 11/29/23


def main():
    # Open the CSV file using `csv` from the standard library.
    with open(CSV_FILE, 'r') as file:
        # Create a CSV reader object
        csv_data = csv.reader(file)

        # for row in list(csv_data)[1:]:
        #     print(row, end='\r')
        # print()

    # Open the CSV file using the `Pandas` library.
    pd_data = pd.read_csv(CSV_FILE)

    # print(pd_data)

    # Grab data.
    temperature_data = list(pd_data['Temperature'])
    humidity_data = list(pd_data['Humidity'])

    # Construct data.
    th_timestamp = []
    for i in range(0, len(temperature_data)*2, 2):
        time_stamp = parse_time(EST_TS, i)
        th_timestamp.append(time_stamp)

    # Plot using `matplotlib.pyplot.plot()`
    plt.plot(
        th_timestamp,
        temperature_data,
        label='Temperature',
        marker=''
        )
    plt.plot(
        th_timestamp,
        humidity_data,
        label='Humidity',
        marker=''
        )

    # Format plot.
    plt.legend()
    date_formatter = DateFormatter('%H:%M')
    plt.gca().xaxis.set_major_formatter(date_formatter)

    # Show plot.
    plt.show()


def parse_time(time_start, time_elapsed):
    """Return time calculated."""
    # Convert `%H:%M` time string into a datetime object.
    start_time = datetime.strptime(time_start, "%H:%M")

    # Add the `time_elapsed` as timedelta.
    end_time = start_time + timedelta(seconds=time_elapsed)

    # Return datetime object
    return end_time


if __name__ == "__main__":
    main()
