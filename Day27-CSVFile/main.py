import pandas

data = pandas.read_csv('weather_data.csv')
# print(data)
# col = data["temp"].tolist()
# print(col)

#Get the avg temp
#avg = sum(col) / len(col)
#print(avg)

#Get the data  colum
#data["temp"] or data.temp

#Get the data row
#print(data[data.day == "Monday"])
#print(data.day == "Monday")


#Avg using pandas
# print(data["temp"].mean())
# #Get the max value
# print(max(data["temp"]))
# print(data["temp"].max())

#Get the data in column
#print(data["condition"])
#print(data.condition)


#Get the single Row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

#Create a Datafarme from scratch
data_dic = {
    "student": ["Any", "James", "Angela"],
    "score": [76,56, 65]
}
#Create a new CSV file
data = pandas.DataFrame(data_dic)
print(data)
data.to_csv("new_data.csv")