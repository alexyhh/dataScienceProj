# installing packages use pip install
#pip install <package name>

# importing libraries
import pandas as pd    #pandas is for dataframes
import matplotlib.pyplot as plt    #matplotlib is for charts
import seaborn as sns    #seaborn is for charts and visualisations

# loading a csv file to a dataframe (df)
df = pd.read_csv('/content/sample_data/california_housing_train.csv')

# to load excel to df
#df = pd.read_excel('/path to excel file')

# show 5 rows of the df
df.head(5)

# show the shape of the table
df.shape

# check for the sum of Null values in each of the column
df.isnull().sum()

# remove a column (eg. remove column "total_rooms") assign to new df (df2)
df2 = df.drop(['total_rooms'], axis = 1)

# saving the dataframe df into a csv file (DON'T RUN)
#df.to_csv('df.csv')

#test