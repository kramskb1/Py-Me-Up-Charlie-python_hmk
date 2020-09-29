import os
import csv
import sys
import pandas as pd
import numpy as np
sys.stdout = open ("test.txt", "w")
df = pd.read_csv(r"C:\Users\benkr\OneDrive\Desktop\Resources\election_data.csv")
index=df.index
dfc=df.groupby('Candidate').count()
dfc.sort_values ('Voter ID', axis=0, ascending=False,inplace=True)
winner=dfc.index[0]
total=df.count()
dfp=dfc['Voter ID'].apply(lambda x: 100*x/total)
dfp['Percent']=pd.Series([round(val, 3) for val in dfp['Voter ID']], index = dfp.index)
dfp['Count']=dfc['Voter ID']
print ("Election Results")
print ("-------------------------")
print ("Total Votes= "+ str(total[1]))
print ("-------------------------")
for index,row in  dfp.iterrows() : print(index+": " + str(row['Percent']) + "% ("+str(row['Count'].astype(np.int64)) + ")")
print ("-------------------------")
print("Winner= "+winner)
sys.stdout.close()


