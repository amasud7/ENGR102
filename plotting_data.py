# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Ayad Masud
# Section: 511
# Assignment: 4.17 Lab
# Date: 11/11/23
# comment
import numpy as np
import matplotlib.pyplot as plt


with open('WeatherDataCLL.csv', 'r') as file:
    next(file)
    max_temp = [] # holds list of max temps (y-values)
    wind = []
    rain = []
    humid = []
    data = {}
    for line in file:
        r = line.strip()
        s = line.split(',') # list of elements in each line
        data[s[0]] = s
        if s[-2] == '':
            continue
        max_temp.append(s[-2])
        if s[1] == '':
            continue
        wind.append(s[1])  
        if s[2] == '0':
            continue
        rain.append(s[2])
        if s[3] == '':
            continue
        humid.append(s[3])
rain1 = [float(i) for i in rain]
humid1 = [eval(i) for i in humid]

# plot 1
max_temp1 = [float(i) for i in max_temp]
fig, ax = plt.subplots()
x = np.arange(3649)
ax.set_title('Maximum Temparature and Average Wind Speed')
ax.set_xlabel('Data')
ax.set_ylabel('Max Temperature')
ax.plot(x, max_temp1, 'r', linewidth=1.0, label='Max Temp')
ax.legend()

wind1= [float(i) for i  in wind]
ax2 = ax.twinx()
ax2.set_ylabel('Average Wind Speed MPH')
ax2.plot(x, wind1, 'b', linewidth=1.0, label='Wind Speed')
ax2.legend(loc='upper right')
plt.show()

# plot 2
plt.hist(wind1)
plt.title('Histogram of Average Wind Speed')
plt.xlabel('Average Wind Speed MPH')
plt.ylabel('Number of Days')
plt.tick_params
plt.show()

# plot 3
h = np.array(humid1)
r = np.array(rain1)
h1 = np.resize(h, 945)

plt.scatter(h1, r, color='black', marker='o')
plt.xlabel('Average Relative Humidty (%)')
plt.ylabel('Precipitation (in)')
plt.title('Precipitation vs Average Relative Humidity')
plt.show()

# plot 4
# getting average temp of each month

# january 
jan_temp = []
for i in data:
    if '1' == i[0] and i[1] == '/':
        if data[i][-3] == '':
            continue
        jan_temp.append(data[i][-3])
jan_int = [eval(i) for i in jan_temp]
jan_avg = sum(jan_int) / len(jan_temp)
jan_max = max(jan_int)
jan_min = min(jan_int)

# february
feb_temp = []
for i in data:
    if '2' == i[0] and i[1] == '/':
        if data[i][-3] == '':
            continue
        feb_temp.append(data[i][-3])
feb_int = [eval(i) for i in feb_temp]
feb_avg = sum(feb_int) / len(feb_temp)
feb_max = max(feb_int)
feb_min = min(feb_int)

# march
mar_temp = []
for i in data:
    if '3' == i[0] and i[1] == '/':
        if data[i][-3] == '':
            continue
        mar_temp.append(data[i][-3])
mar_int = [eval(i) for i in mar_temp]
mar_avg = sum(mar_int) / len(mar_temp)
mar_max = max(mar_int)
mar_min = min(mar_int)

# april
apr_temp = []
for i in data:
    if '4' == i[0] and i[1] == '/':
        if data[i][-3] == '':
            continue
        apr_temp.append(data[i][-3])
apr_int = [eval(i) for i in apr_temp]
apr_avg = sum(apr_int) / len(apr_temp)
apr_max = max(apr_int)
apr_min = min(apr_int)

# May
may_temp = []
for i in data:
    if '5' == i[0] and i[1] == '/':
        if data[i][-3] == '':
            continue
        may_temp.append(data[i][-3])
may_int = [eval(i) for i in may_temp]
may_avg = sum(may_int) / len(may_temp)
may_max = max(may_int)
may_min = min(may_int)

# June
jun_temp = []
for i in data:
    if '6' == i[0] and i[1] == '/':
        if data[i][-3] == '':
            continue
        jun_temp.append(data[i][-3])
jun_int = [eval(i) for i in jun_temp]
jun_avg = sum(jun_int) / len(jun_temp)
jun_max = max(jun_int)
jun_min = min(jun_int)

# July
jul_temp = []
for i in data:
    if '7' == i[0] and i[1] == '/':
        if data[i][-3] == '':
            continue
        jul_temp.append(data[i][-3])
jul_int = [eval(i) for i in jul_temp]
jul_avg = sum(jun_int) / len(jul_temp)
jul_max = max(jul_int)
jul_min = min(jul_int)

# august
aug_temp = []
for i in data:
    if '8' == i[0] and i[1] == '/':
        if data[i][-3] == '':
            continue
        aug_temp.append(data[i][-3])
aug_int = [eval(i) for i in aug_temp]
aug_avg = sum(aug_int) / len(aug_temp)
aug_max = max(aug_int)
aug_min = min(aug_int)

# September
sep_temp = []
for i in data:
    if '9' == i[0] and i[1] == '/':
        if data[i][-3] == '':
            continue
        sep_temp.append(data[i][-3])
sep_int = [eval(i) for i in sep_temp]
sep_avg = sum(sep_int) / len(sep_temp)
sep_max = max(sep_int)
sep_min = min(sep_int)

# October
oct_temp = []
for i in data:
    if '1' == i[0] and i[1] == '0' and  i[2] == '/':
        if data[i][-3] == '':
            continue
        oct_temp.append(data[i][-3])
oct_int = [eval(i) for i in oct_temp]
oct_avg = sum(oct_int) / len(oct_temp)
oct_max = max(oct_int)
oct_min = min(oct_int)

# November
nov_temp = []
for i in data:
    if '1' == i[0] and i[1] == '1' and  i[2] == '/':
        if data[i][-3] == '':
            continue
        nov_temp.append(data[i][-3])
nov_int = [eval(i) for i in nov_temp]
nov_avg = sum(nov_int) / len(nov_temp)
nov_max = max(nov_int)
nov_min = min(nov_int)

# December
dec_temp = []
for i in data:
    if '1' == i[0] and i[1] == '2' and  i[2] == '/':
        if data[i][-3] == '':
            continue
        dec_temp.append(data[i][-3])
dec_int = [eval(i) for i in dec_temp]
dec_avg = sum(dec_int) / len(dec_temp)
dec_max = max(dec_int)
dec_min = min(dec_int)



# now making the bar graph
x = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
y = np.array([jan_avg, feb_avg, mar_avg, apr_avg, may_avg, jun_avg, jul_avg, aug_avg, sep_avg, oct_avg, nov_avg, dec_avg])
plt.title('Temperature by Month')
plt.xlabel('Months')
plt.ylabel('Average Temperature F')
plt.bar(x, y)
plt.plot([jan_max, feb_max, mar_max, apr_max, may_max, jun_max, jul_max, aug_max, sep_max, oct_max, nov_max, dec_max], 'r', linewidth = 2.0)
plt.plot([jan_min, feb_min, mar_min, apr_min, may_min, jun_min, jul_min, aug_min, sep_min, oct_min, nov_min, dec_min], 'black', linewidth = 2.0)
plt.legend(['High temp', 'Low temp'])
plt.show()
