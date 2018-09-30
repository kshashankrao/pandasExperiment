import pandas as pd
import os
# Creating Data using Dictionary
data = {"Name":["A","B","C","D","E","F","G","H","I","J"],"Age":['1','2','3','4','5','6','7','8','9','10']}
df = pd.DataFrame(data,columns = ['Name','Age'])
# Display the 1st five row of data
print(df.head())
#Display the last 5 row of data
print(df.tail())
#Displaying full data
print(df)
# Describe the data
print(df.describe())
# Saving Data
df.to_csv('nameAge.csv')

#Opening the csv file
df = pd.read_csv("nameAge.csv")
#Adding new column
df["Country of origin"] = ["ABC","BCD","CDE","DEF","EFG","FGH","GHI","HIJ","IJK","JKL"]
# Display the 1st five row of data
print(df.head())

#Removing column
df.drop("Country of origin" , axis = 1, inplace = True)
# Display the 1st five row of data
print(df.head())

# Removing column by its number
df.drop(df.columns[[0,1]], axis=1, inplace=True)
# Display the 1st five row of data
print(df.head())
