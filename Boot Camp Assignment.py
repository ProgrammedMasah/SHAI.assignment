import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

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
#The 'Notes' &'Status' columns will be deleted because they do not contain any data
df.drop(['Notes', 'Status'], axis=1, inplace=True)

#If it is not stated whether the employee has Benefits, Overtime Pay, or Other Pay, then these values should be set to zero
df['OvertimePay'].fillna(0, inplace=True)
df['OtherPay'].fillna(0, inplace=True)
df['Benefits'].fillna(0, inplace=True)

#The values in this column are calculated based on other values within the same row: BasePay = TotalPay - (OvertimePay + OtherPay)
#Handling the First Case
df['BasePay'].fillna(df['TotalPay'] - (df['OvertimePay'] + df['OtherPay']), inplace=True)
#Handling the Second Case
#df = df[['Id', 'EmployeeName', 'JobTitle', 'TotalPay', 'BasePay', 'OvertimePay', 'OtherPay', 'Benefits', 'TotalPayBenefits', 'Year', 'Agency']]
#df['BasePay'].fillna(method = 'pad', inplace=True)


#==========================================================

#Basic Data Visualization: 
#==========================
#The Distribution of Salaries
plt.plot(df['Year'],df['TotalPay'], color = 'r')
plt.title('The Distribution of Salaries', fontdict = {'fontname' : 'Constantia', 'fontsize' : 20})
plt.xticks([2011,2012,2013,2014])
plt.xlabel('Year', fontdict = {'fontname' : 'Constantia', 'fontsize' : 15}, color = 'r')
plt.ylabel('Salaries', fontdict = {'fontname' : 'Constantia', 'fontsize' : 15}, color = 'r')
plt.show()

#pie chart to represent the proportion of employees in different departments                
department_counts = (df['JobTitle'].value_counts()* 100 ) / 148654
p = {}
other = 0
for x, y in department_counts.items():
    if y < 1:
        other+= y
    else:
        p[x] = np.floor(y)

p['Other'] = np.floor(other)
explode = (2,2,2,2,2,2,2,2,2,2,2,2)
plt.pie(p.values() , labels=p.keys(), autopct='%1.2f%%', startangle=90, shadow = True, explode = explode)
plt.legend(loc='lower left')
plt.show()

#==========================================================

#Grouped Analysis: 
#==================
#Group the data by one columns and calculate summary statistics for each group
print(df.groupby(['JobTitle']).mean())
print(df.groupby(['JobTitle']).median())
print(df.groupby(['JobTitle']).mean())
print(df.groupby(['JobTitle']).std())

#Group the data by more columns and calculate summary statistics for each group
print(df.groupby(['JobTitle', 'TotalPay']).mean())
print(df.groupby(['JobTitle', 'TotalPay']).median())
print(df.groupby(['JobTitle', 'TotalPay']).mean())
print(df.groupby(['JobTitle', 'TotalPay']).std())

#compare the average salaries across different groups.
print(df.groupby(['JobTitle']).mean()['TotalPay'])


#==========================================================

#Simple Correlation Analysis:
#=============================
#Identify any correlation between salary and another numerical column
print('Correlation Between Salary & Total Pay Benefits  %6.5f'%(df['TotalPay'].corr(df['TotalPayBenefits'])))
print('---------------------------------------------------------------')
print('Correlation Between Salary & Benefits            %6.5f'%(df['TotalPay'].corr(df['Benefits'])))
print('---------------------------------------------------------------')
print('Correlation Between Salary & OtherPay            %6.5f'%(df['TotalPay'].corr(df['OtherPay'])))
print('---------------------------------------------------------------')
print('Correlation Between Salary & Overtime Pay        %6.5f'%(df['TotalPay'].corr(df['OvertimePay'])))
print('---------------------------------------------------------------')
print('Correlation Between Salary & Base Pay            %6.5f'%(df['TotalPay'].corr(df['BasePay'])))
print('---------------------------------------------------------------')
print('Correlation Between Salary & Year                %6.5f'%(df['TotalPay'].corr(df['Year'])))
# => Correlation Between Salary & Total Pay Benefits is the largest

#plot a scatter plot to visualize the relationship.
plt.scatter(df['TotalPay'], df['TotalPayBenefits'], color = 'purple')
plt.title('The Distribution of Salaries', fontdict = {'fontname' : 'Constantia', 'fontsize' : 23})
plt.xlabel('Total Pay', fontdict = {'fontname' : 'Constantia', 'fontsize' : 15}, color = 'purple')
plt.ylabel('Total Pay Benefits', fontdict = {'fontname' : 'Constantia', 'fontsize' : 15}, color = 'purple')
plt.show()
