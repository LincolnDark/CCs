import pandas as pd

df = pd.read_csv('co2_ppm_daily.csv')

# 1 Annual Average

# co2_data = co2.frame
co2_data["date"] = pd.to_datetime(co2_data[["year", "month", "day"]])

# code appropriated from: https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpr_co2.html

for year in date:
    print(year)
    total = 0
    with open("co2_ppm_daily.csv") as co2.csv:
        for row in csv.reader(co2.csv):
            if year == row[0]
                total += float(row[1])
                print(total / 12)

# 2 Min, Max, and Average

max1 = df['value'].max()
min1 = df['value'].min()
mean1 = df['value'].mean()

# code from https://datatofish.com/use-pandas-to-calculate-stats-from-an-imported-csv-file/

# 3 Seasonal averages

import csv
from datetime import datetime
from itertools import groupby

LOOKUP_SEASON = {
    11: 'Autumn',
    12: 'Winter',
    1: 'Winter',
    2: 'Winter',
    3: 'Spring',
    4: 'Spring',
    5: 'Spring',
    6: 'Summer',
    7: 'Summer',
    8: 'Summer',
    9: 'Autumn',
    10: 'Autumn'
}


def get_season(row):
    date = datetime.strptime(row[0], '%d/%m/%Y')
    season = LOOKUP_SEASON[date.month]
    if season == 'Winter':
        if date.month == 1:
            last_year, next_year = date.year - 1, date.year
        else:
            last_year, next_year = date.year, date.year + 1
        return '{} {}/{}'.format(season, last_year, next_year)
    else:
        return '{} {}'.format(season, date.year)


def get_year(row):
    date = datetime.strptime(row[0], '%d/%m/%Y')
    if date.month < 8:
        return date.year - 1
    else:
        return date.year


season.mean("Winter")
season.mean("Spring")
season.mean("Summer")
season.mean("Fall"

# code appropriated from https://stackoverflow.com/questions/22693024/group-data-in-csv-by-season-and-year-using-python-and-pandas

# 4 Calculating anomaly

import numpy as np
import pandas as pd

df['month'] = df['Dates'].dt.strftime("%m").astype(int)
df = df.merge(monthly_means.rename(columns={'Dates': 'month', 'Values': 'Mean'}), on='month', how='left')
df['Diff'] = df['Mean'] - df['Values']

# code appropriated from https://stackoverflow.com/questions/65839307/calculating-monthly-anomalies-in-pandas
