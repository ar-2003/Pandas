import numpy as np
import pandas as pd

'''dict1 = {
    "name":['harry','rohan','ar','sg'],
    "marks": [92, 34, 24, 17],
    "city": ['Mum', 'Delhi', 'Blr', 'Hyd']
}
'''
#df = pd.DataFrame(dict1)


#df.to_csv('friends.csv') #Exporting values to csv with filename with index
#df.to_csv('friends_if.csv', index = False) #Exporting values to csv with filename without index

#print(df) # print whole dataset
#print(df.head(2)) # print only top 2 rows in dataset
#print(df.tail(2)) # print only bottom 2 rows in dataset
#print(df.describe())  # calculates 1)count 2)mean 3)std 4min 5)25% 6)50% 7)75% 8)max   

temp = pd.read_csv('Temp.csv')
#print(temp)
#temp['Speed'][0] = 50
print(temp['Speed'])