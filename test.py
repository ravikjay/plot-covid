# first attempt 
import csv
import sys

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


file_confirmed = 'time_series_covid19_confirmed_global.csv'
file_deaths = 'time_series_covid19_deaths_global.csv'
file_recovered = 'time_series_covid19_recovered_global.csv'

state_idx = 0
country_idx = 1
lat_idx = 2
lon_idx = 3
first_date_idx = 4

with open(file_confirmed) as csv_file:
    r = list(csv.reader(csv_file))

    # Set up dates index
    dates = [''] * (len(r[0]) - first_date_idx)
    print()
    for i in range(first_date_idx, len(r[0])):
        date = r[0][i]
        print(date)
        dates[i-first_date_idx] = date

with open(file_confirmed) as csv_file:
    r = list(csv.reader(csv_file))

    confirmed = [0] * len(dates)

    for row in r[1:]:
        state = row[state_idx]
        country = row[country_idx]

        for i in range(first_date_idx, len(r[0])):
            val = int(row[i])
            confirmed[i-first_date_idx] = confirmed[i-first_date_idx] + val

with open(file_deaths) as csv_file:
    r = list(csv.reader(csv_file))

    deaths = [0] * len(dates)

    for row in r[1:]:
        state = row[state_idx]
        country = row[country_idx]

        for i in range(first_date_idx, len(r[0])):
            val = int(row[i])
            deaths[i-first_date_idx] = deaths[i-first_date_idx] + val

with open(file_recovered) as csv_file:
    r = list(csv.reader(csv_file))

    recovered = [0] * len(dates)

    for row in r[1:]:
        state = row[state_idx]
        country = row[country_idx]

        for i in range(first_date_idx, len(r[0])):
            val = int(row[i])
            recovered[i-first_date_idx] = recovered[i-first_date_idx] + val
