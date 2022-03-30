import csv

year_list, month_list, value_list = [],[],[]
with open ("co2_ppm_daily.csv") as co2:
    csv_reader =csv.reader(co2, delimiter=',')
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

# yearly average
print("there are " + str(len(year_list)) + " years.")
for year_select in year_list:
    ppm_by_year = []
    with open("co2_ppm_daily.csv") as co2:
        csv_reader = csv.reader(co2, delimiter=',')
        linecount = 0
        header = next(csv_reader)
        print(header)
        for row in csv_reader:
            year, month, day = row[0].split("-")
            if year == year_select:
                ppm_by_year.append(row[1])
    print("Year is: " + str(int(year_select)) + " ppm is: " + str(float(sum(ppm_by_year) / len(ppm_by_year))))


