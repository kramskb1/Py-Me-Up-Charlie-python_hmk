  When I started the assignment, I created a Python script for the PyBank part of the assignment. I initially used the CSV file from my own desktop, then tried to create relative path which I had trouble creating earlier. I first looked at the count. Then, I used the count function in Python to calculate the number of rows which is how I answered the first part of the assignment. To find the net/total amount of profit/losses over the entire period, I used the code total=df['Profit/Losses'].sum(axis=0).  To analyze the difference, I used the code df['Dif']=df['Profit/Losses'].diff(). I used a similar kind of code to analyze the maximum difference and the minimum difference. I attempted to print my analysis to a text file, but when I put the command that I did in there nothing ran, so I had to take that command out. I played around with the command and am hoping that now a new sheet would open with output on that command.
	Next, I created a Python script for the Pypoll part of the assignment. I imported the CSV into my Python script without opening the Excel file, as Excel could not handle as much data as this data set had. I found the total number of votes cast by using the print command in Python and printing the count of my df variable. Next, I did a groupby count of each candidate. Next, I created a code to sort the values so that the winner would be on top of the chart which I outputted. Next. I took the total. After that, I used the lambda function in Python to figure out all of the percentages that I needed to figure out. Next, I used a series in Python to calculate the percentage that each candidate received. I then attempted to drop the voter ID column. I then outputted my results to a text file.
	My output reveals a lot of interesting things. For the first part, it reveals a lot of interesting information in regards to the profit and losses over time of the company. It is also very useful to know the greatest increase in profits and the greatest decrease in losses. For the second part, it shows a lot of interesting analysis on votes and how they were cast during that given election. In my code I wrote the command for index,row in  dfp.iterrows() : print(index+": " + str(row['Percent']) + "% ("+str(row['Count']) + ")") which outputted a spreadsheet with all of the information requested. 
	In order to open my output as an excel file, I used Python code sys.stdout = open ("test.txt", "w") at the beginning of my document and Python code sys.stdout.close() at the end of my document, which I deleted after obtaining the text file. I found this assignment very interesting as I had to analyze data about topics that I am very passionate about. 