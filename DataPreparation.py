import pandas as pad

health_data = pad.read_csv("data.csv", header=0, sep=",")
print(health_data)

# DATA CLEANING  //dropna() function is used to remove blank space and any dirty data in the csv file
health_data.dropna(axis=0, inplace=True)

print("\n",health_data)
print(health_data.info()) #info() to check datatype of data

health_data["Average_Pulse"] = health_data['Average_Pulse'].astype(float)
health_data["Max_Pulse"] = health_data["Max_Pulse"].astype(float)

print (health_data.info())
#Data Analysising    describe() fn is used to analysis the data
print(health_data.describe())