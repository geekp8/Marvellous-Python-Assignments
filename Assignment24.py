import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.preprocessing import MinMaxScaler
data={
    'Name':['Amit','Sagar','Pooja'],
    'Math':[85,90,78],
    'Science':[92,88,80],
    'English':[75,85,82]
}
df=pd.DataFrame(data)
print(data)
print(df.shape)
print(df.columns)
print(df.dtypes)#prints datatypes

print(df.describe())


Line="*"*20
print("Assignemnt 24 Solutions")
print(Line)

print("Math Normalised:")
scaler=MinMaxScaler()
scalerfit=df['Math_norm']=scaler.fit_transform(df[['Math']])
print(scalerfit)

#create a gender column 
data={
    'Name':['Amit','Sagar','Pooja'],
    'Math':[85,90,78],
    'Science':[92,88,80],
    'English':[75,85,82]
}
print("One hot encoding")
df['Gender']=['Male','Male','Female']
print("Grouping student by gender with average marks")
groupavg=df.groupby('Gender')[['Math','Science','English']].mean()
print(groupavg)
df=pd.get_dummies(df,columns=['Gender'])
print(df)


print("Pie chart for Marks of Sagar")
marks1=df[df['Name']=='Sagar'].drop(columns='Name').iloc[0]
marks2=marks1[['Math','Science','English']]

plt.pie(marks2,labels=marks2.index,autopct='%1.1f%%')
plt.title("Marks of Sagar for all subjects")
plt.show()

#add a status column

print("added Status column")
df['Total'] = df[['Math', 'Science', 'English']].sum(axis=1)
df['Status'] = df['Total'].apply(lambda x: 'Pass' if x >= 250 else 'Fail')
print(df)

#count how many students passed
print("The no of students passed:")
count=df[df['Status']=='Pass'].shape[0]
print(count)

#export to csv
print("Final dataframe to csv")
df.to_csv('final_df.csv',index=False)

#create histogram of Maths
plt.hist(df['Math'],bins=5 ,color='blue',edgecolor='black')
plt.title("Distribution of Maths ")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()

#rename maths to mathematics

df=df.rename(columns={'Math':'Mathematics'})
print(df)

#boxplot of english marks
plt.boxplot(df['English'])
plt.title("Boxplot of English marks")
plt.ylabel("Marks")
plt.show()