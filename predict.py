import pandas as pd
from datetime import datetime
from numpy import std 
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
data=pd.read_csv('sphist.csv')
data['Date']=pd.to_datetime(data['Date'])
data=data.sort_values(by=['Date'],ascending=True)
data['day_5']=0
data['std_5']=0
data.reset_index(drop=True,inplace=True)
data['Close']=data['Close'].astype('float')
print(data.head())
for index, row in data.iterrows():
    if index<5:
        data.loc[index,'day_5']=0
    else:
        values=[]
        for i in range(index-1,index-6,-1):
            values.append(data.loc[i,'Close'])
        avg_values=sum(values)/len(values)
        std_5=std(values,ddof=0)
        data.loc[index,'day_5']=avg_values
        data.loc[index,'std_5']=std_5
data['day_365']=0
data['std_365']=0
for index, row in data.iterrows():
    if index<365:
        data.loc[index,'day_365']=0
    else:
        values=[]
        for i in range(index-1,index-366,-1):
            values.append(data.loc[i,'Close'])
        avg_value=sum(values)/len(values)
        std_365=std(values,ddof=0)
        data.loc[index,'day_365']=avg_value
        data.loc[index,'std_365']=std_365
data['day_30']=0
for index, row in data.iterrows():
    if index<30:
        data.loc[index,'day_30']=0
    else:
        values=[]
        for i in range(index-1,index-31,-1):
            values.append(data.loc[i,'Close'])
        avg_value=sum(values)/len(values)
        data.loc[index,'day_30']=avg_value
new_data=data[data['day_365'] != 0]
new_data=new_data.dropna(axis=0)
new_data['5_365_ratio']=new_data['day_5']/new_data['day_365']
new_data['std_ratio']=new_data['std_5']/new_data['std_365']
train=new_data[new_data['Date'] < datetime(year=2013,month=1,day=2)]
test=new_data[new_data['Date'] >= datetime(year=2013,month=1,day=2)]
features=['day_5','day_365','day_30','std_5','std_365','5_365_ratio','std_ratio']
lr=LinearRegression()
lr.fit(train[features],train['Close'])
predictions=lr.predict(test[features])
mse=mean_squared_error(test['Close'],predictions)
print(mse)