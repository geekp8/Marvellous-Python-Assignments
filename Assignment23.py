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


#df['Total']=df.sum(axis=1)
#add a column
print("Newly added column displayed")
df['Total']=df[['Math','Science','English']].sum(axis=1)
print(df)

#display students who scored more than 85 in science

#printed with iteration
#print(df['Science'])
# Sci=df['Science']
# #print(Sci)
# score=df[Sci >85]
# print(score)
print("Marks in science greater than 85")
print(df['Science'][df['Science']>85])

#replace Pooja with Puja
print("Replace Pooja with Puja")
df.replace('Pooja','Puja',inplace=True)
print(df)

#sort values by descending
#descending means Highest to lowest
print("Descending values are:")
sorted=df.sort_values(by=['Total'],ascending=False)
print(sorted)

#plt.bar('Name')
studentNames=df['Name']
TotalMarks=df['Total']

plt.bar(studentNames,TotalMarks,color='blue')

plt.xlabel('Names')
plt.ylabel('Total')
plt.title('Bar plot')
plt.show()


# print(student)
# student= df[df['Name'] == 'Amit']
# print(student)

student = df[df['Name'] == 'Amit'].drop(columns=['Name']).T
student.columns = ['Marks']

plt.plot(student.index, student['Marks'], marker='o')
plt.title("Amit's Marks for all Subjects")
plt.xlabel("Subject")
plt.ylabel("Marks")
plt.grid(True)
plt.show()

#missing values with column mean
data2 = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [np.nan, 76, 88],
    'Science': [91, np.nan, 85]
}

print("Missing values with column mean are replaced:")
df1 = pd.DataFrame(data2)
df1[['Math', 'Science']] = df1[['Math', 'Science']].fillna(df1[['Math', 'Science']].mean())
print(df1)

#drop english columns
print("Dropped English column:")
df = df.drop(columns=['English'])
print(df)

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