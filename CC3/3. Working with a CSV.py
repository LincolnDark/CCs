import csv

year_list, month_list, value_list = [],[],[]
with open ("co2_ppm_daily.csv") as co2:
    csv_reader =csv.reader(co2,delimiter = ',')
    linecount = 0
    headerline = co2.next()
    print(headerline)
    for row in csv_reader:
        year,month,day = row[0].split("-")
        if year not in year_list:
            year_list.append(year)
        if month not in month_list:
            month_list.append(month)
        value_list.append(float(row[1]))
        line_count = len(value_list)


# min, max, average
print("Minimum = " + str(min(value_list)))
print("Maximum = " + str(max(value_list)))
print("Average = " + str(float(sum(value_list) / int(line_count))))
print("Average 2 = " + str(sum(value_list) / len(value_list)))



# code from https://datatofish.com/use-pandas-to-calculate-stats-from-an-imported-csv-file/

# 3 Seasonal averages

import csv
# from datetime import datetime
# from itertools import groupby
#
# LOOKUP_SEASON = {
#     11: 'Autumn',
#     12: 'Winter',
#     1: 'Winter',
#     2: 'Winter',
#     3: 'Spring',
#     4: 'Spring',
#     5: 'Spring',
#     6: 'Summer',
#     7: 'Summer',
#     8: 'Summer',
#     9: 'Autumn',
#     10: 'Autumn'
# }
#
#
# def get_season(row):
#     date = datetime.strptime(row[0], '%d/%m/%Y')
#     season = LOOKUP_SEASON[date.month]
#     if season == 'Winter':
#         if date.month == 1:
#             last_year, next_year = date.year - 1, date.year
#         else:
#             last_year, next_year = date.year, date.year + 1
#         return '{} {}/{}'.format(season, last_year, next_year)
#     else:
#         return '{} {}'.format(season, date.year)
#
#
# def get_year(row):
#     date = datetime.strptime(row[0], '%d/%m/%Y')
#     if date.month < 8:
#         return date.year - 1
#     else:
#         return date.year
#
#
# season.mean("Winter")
# season.mean("Spring")
# season.mean("Summer")
# season.mean("Fall"
#
# # code appropriated from https://stackoverflow.com/questions/22693024/group-data-in-csv-by-season-and-year-using-python-and-pandas
#
# # 4 Calculating anomaly
#
# import numpy as np
# import pandas as pd
#
# df['month'] = df['Dates'].dt.strftime("%m").astype(int)
# df = df.merge(monthly_means.rename(columns={'Dates': 'month', 'Values': 'Mean'}), on='month', how='left')
# df['Diff'] = df['Mean'] - df['Values']
#
# # code appropriated from https://stackoverflow.com/questions/65839307/calculating-monthly-anomalies-in-pandas
