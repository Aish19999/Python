#Read the CSV file and put the data in the list
# with open('weather_data.csv') as data:
#     content = data.readlines()
#     print(content)

#
#Usung csv library
# import csv
#
# with open('weather_data.csv') as data:
#     content = csv.reader(data)
#     tenperature =[]
#     for row in content:
#         print(row)
#         if(row[1] != "temp"):
#             tenperature.append(f"temp ony int({row[1]})")
#     print(tenperature)