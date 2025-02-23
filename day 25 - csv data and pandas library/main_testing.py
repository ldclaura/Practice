#CSV data
#CSV is common for tabular data (spreadsheet)
import csv
import pandas


# with open("weather_data.csv") as data_file:
#         data = data_file.readlines()
#         print(data)
    #readlines() puts each line as strings in a list
    #looks like ass tho so use csv
    #output: ['day,temp,condition\n', 'Monday,12,Sunny\n', 'Tuesday,14,Rain\n', 'Wednesday,15,Rain\n', 'Thursday,14,Cloudy\n', 'Friday,21,Sunny\n', 'Saturday,22,Sunny\n', 'Sunday,24,Sunny']

with open("weather_data.csv") as data_file:
        data = csv.reader(data_file)
        temperatures = [] #integers not string
        for row in data:
            if row[1] != 'temp': #removes temp
                temperatures.append(int(row[1])) #adds numbers temps to temperatures
                print(row)

#-------------------------------------------------------------------
#TURNS TEMPERATURES FROM STRING TO INT
        temperatures = [int(item) for item in temperatures]
        print(temperatures)

panda_data = pandas.read_csv("weather_data.csv")
print(panda_data["temp"]) #prints temp column

print(type(panda_data))
# <class 'pandas.core.frame.DataFrame'> (entire thing is dataframe)
print(type(panda_data["temp"]))
# <class 'pandas.core.series.Series'> (series=column)

panda_dictionary = panda_data.to_dict()
print(panda_dictionary)
#turns it to dictionary

temp_list = panda_data["temp"].to_list()
print(temp_list)


#AVERAGE OF TEMP_LIST
average = 0
count = 0
for _ in temp_list:
     average += _
     count += 1
average = average / count
print(average)
#or just
average = sum(temp_list) / len(temp_list)
print(average)
#or just
print(panda_data["temp"].mean())
#pandas.pydata.org
print(panda_data["temp"].nlargest(1))
print(panda_data["temp"].max())

#these do same thing, pandas behind the scene turns column headings to attributes
print(panda_data["condition"])
print(panda_data.condition)

#row of data
print("MONDAY")
print(panda_data[panda_data.day == "Monday"])
print(panda_data[panda_data["day"] == "Monday"])
#which row of data has highest temp in wk
print(panda_data[panda_data["temp"] == panda_data["temp"].max()])

monday = panda_data[panda_data.day == "Monday"]
print(monday.condition) #grab condition column from monday row

print(monday.temp)
celcius = monday.temp
fahrenheit = celcius * (9/5) + 32
print(fahrenheit)


#create csv (basically excel/spreadsheet doc) file
data_dict = {
     "students" : ["Amy", "James", "Angela"],
     "scores": [76, 56, 65]
}
students_data = pandas.DataFrame(data_dict)
print(students_data)
students_data.to_csv("new_data.csv")