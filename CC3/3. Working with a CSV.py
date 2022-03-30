import csv

year_list, month_list, value_list = [],[],[]
with open ("co2_ppm_daily.csv") as co2:
    csv_reader =csv.reader(co2, delimiter=',')
    linecount = 0
    #headerline = co2.next() # AD - Check your version of python, you should be using 3.7 or similar. This fails on my machine
    headerline = next(co2)  # AD - Fixed
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
#overall_mean = str(sum(value_list/len(value_list))) # AD - ERROR HERE
overall_mean = str(sum(value_list)/len(value_list)) # AD - Needed to add )
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
                #ppm_by_year.append(row[1]) # AD -This is the problem
                ppm_by_year.append(float(str(row[1])))
    #print("Year is: " + str(int(year_select)) + " ppm is: " + str(float(sum(ppm_by_year) / len(ppm_by_year)))) # AD - Now error here
    # print(type(year_select)) # AD tyring to figure out error - This is fine
    # print("Year is: " + str(year_select)) # AD tyring to figure out error - This is fine
    #print(float(sum(ppm_by_year) / len(ppm_by_year))) # AD - Failure is here
    #print(sum(ppm_by_year)) # AD - This must be a list of strings which is why the math fails.
    #print(ppm_by_year) # AD - Yes, these are strings, so we need to type convert on line 39.
    print("Year is: " + str(year_select) + " ppm is: " + str(float(sum(ppm_by_year) / len(ppm_by_year)))) # AD - Now error here


#seasonal average
seasons_winter = ['12', '01', '02']
seasons_spring = ['03', '04', '05']
seasons_summer = ['06', '07', '08']
seasons_fall = ['09', '10', '11']
seasons_winter_ppm = []
seasons_spring_ppm = []
seasons_summer_ppm = []
seasons_fall_ppm = []
for year_select in year_list:
    ppm_by_year = []
    with open("co2_ppm_daily.csv") as co2:
        csv_reader = csv.reader(co2, delimiter=',')
        linecount = 0
        header = next(csv_reader)
        print(header)
        for row in csv_reader:
            year, month, day = row[0].split("-")
            if month in seasons_winter:
                seasons_winter_ppm.append(float(row[1]))
            if month in seasons_spring:
                seasons_spring_ppm.append(float(row[1]))
            if month in seasons_summer:
                seasons_summer_ppm.append(float(row[1]))
            if month in seasons_fall:
                seasons_fall_ppm.append(float(row[1]))
            if year == year_select:
                ppm_by_year.append(float(row[1])) # AD - also needed to be fixed
    print("Year is: " + str(int(year_select)) + " ppm is: " + str(float(sum(ppm_by_year) / len(ppm_by_year))))
print("Winter average is: " + str(float(sum(seasons_winter_ppm) / len(seasons_winter_ppm))))
print("Spring average is: " + str(float(sum(seasons_spring_ppm) / len(seasons_spring_ppm))))
print("Summer average is: " + str(float(sum(seasons_summer_ppm) / len(seasons_summer_ppm))))
print("Fall average is: " + str(float(sum(seasons_fall_ppm) / len(seasons_fall_ppm))))

#calculating anomaly
print(overall_mean)
with open("co2_ppm_daily.csv") as co2:
    csv_reader = csv.reader(co2, delimiter=',')
    linecount = 0
    header = next(csv_reader)
    for row in csv_reader:
        print(float(str(row[1])) - float(overall_mean))