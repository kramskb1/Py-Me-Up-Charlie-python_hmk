import os
import csv
import pandas as pd 
df = pd.read_csv(r"C:\Users\benkr\OneDrive\Desktop\Resources\budget_data.csv")
df.count()
index =df.index 
number_of_rows = len(index) 
print (number_of_rows)
total=df['Profit/Losses'].sum(axis=0)
print(total)
df['Dif']=df['Profit/Losses'].diff()
print(df['Dif'])
avg_dif=df['Dif'].mean(axis=0)
print(avg_dif)
maximumdifference=df['Dif'].max(axis=0)
print(maximumdifference)
minimumdifference=df['Dif'].min(axis=0)
print(minimumdifference)
print(df.iloc [25])
print(df.iloc [44])
#$ python BenjaminKramskoiPythonHW.py > output.txt 
