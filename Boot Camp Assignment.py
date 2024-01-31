import pandas as pd
import numpy as np
import matplotlib as mpl 

#read file 
df = pd.read_csv('Salaries.csv')

#==========================================================

#Basic Data Exploration:
#=======================
#the number of rows and columns
print("the number of rows is:", len(df['Id']))
print("the number of columns is:", len(df.columns))
print("\n"*2)


#determine the data types of each column
print("%5s \t\t  %14s" %("Column","data Type"))
print("="*30)
print(df.dtypes)
print("\n"*2)

#check for missing values in each column.
print("%5s \t\t  %18s" %("Column","Missing Values"))
print("="*35)
print(df.isnull().sum())


#==========================================================

#Descriptive Statistics:
#=======================
#Calculate basic statistics mean, median, mode, minimum, and maximum value to the columns, determine the range of salaries, and find the standard deviation.
print("Descriptive Statistics of Salary:")
print("="*35)
print("Mean                 %9.4f" %(df['TotalPay'].mean()))
print("Median               %9.4f" %(df['TotalPay'].median()))
print("Mode                 %9.4f" %(df['TotalPay'].mode()[0]))
print("Minimum              %9.4f" %(df['TotalPay'].min()))
print("Maximum              %9.4f" %(df['TotalPay'].max()))
print("Standard Deviation   %9.4f" %(df['TotalPay'].std()))
print('The Salary Range =  [', df['TotalPay'].min() , ',' , df['TotalPay'].max(), ']')


#==========================================================

#Data Cleaning:
#=============== 
#Handle missing data by suitable method
df.drop(['Notes', 'Status'], axis=1, inplace=True)

df['OvertimePay'].fillna(0, inplace=True)
df['OtherPay'].fillna(0, inplace=True)
df['Benefits'].fillna(0, inplace=True)
  
#First case
df['BasePay'].fillna(df['TotalPay'] - (df['OvertimePay'] + df['OtherPay']), inplace=True)
#Second case
#df = df[['Id', 'EmployeeName', 'JobTitle', 'TotalPay', 'BasePay', 'OvertimePay', 'OtherPay', 'Benefits', 'TotalPayBenefits', 'Year', 'Agency']]
#df['BasePay'].fillna(method = 'pad', inplace=True)
#==========================================================

#Basic Data Visualization: 
#==========================
#The Distribution of Salaries
plt.plot(df['Year'],df['TotalPay'])
plt.title('The Distribution of Salaries', fontdict = {'fontname' : 'Constantia', 'fontsize' : 20})
plt.xticks([2011,2012,2013,2014])
plt.xlabel('Year', fontdict = {'fontname' : 'Constantia', 'fontsize' : 15})
plt.ylabel('Salaries', fontdict = {'fontname' : 'Constantia', 'fontsize' : 15})




#==========================================================

#Grouped Analysis: 
#==================
#Group the data by one columns and calculate summary statistics for each group
df.groupby(['JobTitle']).mean()
df.groupby(['JobTitle']).median()
df.groupby(['JobTitle']).mean()
df.groupby(['JobTitle']).std()

#Group the data by more columns and calculate summary statistics for each group
df.groupby(['JobTitle', 'TotalPay']).mean()
df.groupby(['JobTitle', 'TotalPay']).median()
df.groupby(['JobTitle', 'TotalPay']).mean()
df.groupby(['JobTitle', 'TotalPay']).std()

#compare the average salaries across different groups.
df.groupby(['JobTitle']).mean()['TotalPay']


#==========================================================

#Simple Correlation Analysis:
#=============================
#Identify any correlation between salary and another numerical column


#plot a scatter plot to visualize the relationship.
