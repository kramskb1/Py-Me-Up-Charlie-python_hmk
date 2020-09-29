import os
import csv
import sys
import pandas as pd
import numpy as np
sys.stdout = open ("test.txt", "w")
df = pd.read_csv(r"C:\Users\benkr\OneDrive\Desktop\Resources\election_data.csv")
index=df.index
#print(df.count())
#number_of_rows = len(index)
#print((number_of_rows))
#def(Voter_ID)
#candidate = list(set(Voter_ID))
#candidate.sort()
#listColumns = list(df.columns)
#df.groupby(['Candidate'])

#s=df.Candidate

#counts=s.value_counts()
#per100= s.value_counts().mul(100).div(df.count()).round(2).astype(str)+'%'
#.div(df.count())

#newdf= pd.DataFrame({'counts': counts,'percent': per100})

#print (newdf)

dfc=df.groupby('Candidate').count()
dfc.sort_values ('Voter ID', axis=0, ascending=False,inplace=True)
#dfc['Candidate',0]
winner=dfc.index[0]



#vc=df['Candidate'].value_counts(Normalize=True)
#print(vc)
total=df.count()

#dfc['Percentage']=(dfc['Voter ID'] * 100) / total

dfp=dfc['Voter ID'].apply(lambda x: 100*x/total)

#{:,.2f}'.format
#dfc['Percentage1'] = pd.Series([round(val, 2) for val in df['Percentage']], index = dfc.index)

dfp['Percent']=pd.Series([round(val, 3) for val in dfp['Voter ID']], index = dfp.index)
dfp['Count']=dfc['Voter ID']
#dfp['Name']=dfc['Candidate']
#print(dfc)


#print(dfp)

#dfp.drop(index=['Voter Id'], )



#for index,  in dfp.Index:
print ("Election Results")
print ("-------------------------")
print ("Total Votes= "+ str(total[1]))
print ("-------------------------")

for index,row in  dfp.iterrows() : print(index+": " + str(row['Percent']) + "% ("+str(row['Count'].astype(np.int64)) + ")")

print ("-------------------------")
print("Winner= "+winner)
sys.stdout.close()
#for items in dfp.iteritems():
#   print ( items)

#$ python BenjaminKramskoiPythonHW2.py > output.txt
 # print ( str(items[0])+':'+ str(items[2])+'% ('+str(items[3])+')')

#for rownum,(indx,val) in enumerate(dfp.iteritems()):
#    print('VAL1: ', val[0], 'VAL2: ', val[1], 'VAL3: ', val[2], 'VAL4: ', val[3])

#print(dfp)
#[listColumns].sum ()
#Winner = max(dfp)
#print("Winner:(Winner)")
#print(df.groupby('Voter ID').count())
#my_list = [Khan, Correy, Li, O'Tooley]
#print(df.groupby('Candidate').value_counts())
#df
#a="Khan"
#b="Correy"
#c="Li"
#d="OTooley"
#List = [a, b, c, d]
#print (List)
#Total_votes = List
#print (len(Total_votes))
#List2 = [a+b+c+d]
#print (len(List2))
#print(sum(a+b+c+d)
#print(dtotal_count)
