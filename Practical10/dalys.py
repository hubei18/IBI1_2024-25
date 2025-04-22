import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# change the working directory to the position of dataset
# try the function getcwd() and listdir()
os.chdir('D:\\resource\\大一下\\IBI\\IBI_2024-25\\IBI1_2024-25')
print(os.getcwd())
print(os.listdir())

# read the .csv file
dalys_data=pd.read_csv('dalys-rate-from-all-causes.csv')

# read the first ten lines and the third column
print(dalys_data['Year'].head(10))  # the tenth yaer for Afghanistan is 1999

# traverse the year list and create the boolean list to select 1990
# create C to just print entity and year
# use iloc to get the data
truth=np.array([False]*len(dalys_data))
truth[np.where(dalys_data['Year']==1990)]=True
C=[True,False,True,True]
nine=dalys_data.iloc[truth,C]
print(nine)

# use the same method as above to get the data in United Kingdom and France
# draw plot for the two dataframe
truth=np.array([False]*len(dalys_data))
truth[np.where(dalys_data['Entity']=='United Kingdom')]=True
C=[False,False,True,True]
uk=dalys_data.iloc[truth,C]
plt.plot(uk.Year,uk.DALYs,'b+')
plt.xticks(uk.Year,rotation=-90)
plt.title('DALYs in United Kingdom')
plt.xlabel('years')
plt.ylabel('DALYs')
plt.show()
truth=np.array([False]*len(dalys_data))
truth[np.where(dalys_data['Entity']=='France')]=True
C=[False,False,True,True]
fr=dalys_data.iloc[truth,C]
plt.plot(fr.Year,fr.DALYs,'b+')
plt.xticks(fr.Year,rotation=-90)
plt.title('DALYs in France')
plt.xlabel('years')
plt.ylabel('DALYs')
plt.show()

# calculate the average UK and France DALYs and compare
ukave=np.average(uk.DALYs)
frave=np.average(fr.DALYs)
print(ukave,frave) # the DALYs of UK is larger France

# draw a boxplot to show DALYs in different countries in 1990
nine.boxplot(column='DALYs',rot=90,grid=False)
plt.title('DALYs in different countries in 1990')
plt.xlabel('countries')
plt.ylabel('DALYs')
plt.show()