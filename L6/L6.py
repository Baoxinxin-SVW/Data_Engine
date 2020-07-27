import pandas as pd
from fbprophet import Prophet
import matplotlib.pyplot as plt

def UseProphet(data,time):
    #时间格式转换
    data.Datetime = pd.to_datetime(data.Datetime)
    data.index = data.Datetime
    data.drop(['Datetime'],axis=1,inplace=True)
    #按天累加
    df_daily = data.resample('D').sum()
    #使用fbprophet预测
    df_daily['ds'] = df_daily.index
    df_daily['y'] = df_daily.Count
    df_daily.drop(['Count'],axis=1,inplace=True)
    model = Prophet()
    model.fit(df_daily)
    future = model.make_future_dataframe(periods=time)
    forecast = model.predict(future)
    #输出
    print(forecast)
    model.plot(forecast)
    model.plot_components(forecast)
    
def main():
    df = pd.read_csv('./train.csv',usecols=['Datetime','Count'])
    UseProphet(df,217)

if __name__ == "__main__":
    main()