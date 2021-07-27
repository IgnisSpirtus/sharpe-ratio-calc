from datetime import date,timedelta
from nsepy import get_history
import pandas as pd 
stock_symbols = ["HINDUNILVR","ACC","MARICO"]
df=pd.DataFrame()
start_date=date(2010,1,1)
end_date= start_date + timedelta(days=3650)
for symbol in stock_symbols:
    data=get_history(symbol=symbol,start=start_date,end=end_date)
    df=df.append(data)
df.to_csv('stock_data.csv')

nifty_data = get_history(symbol="NIFTY 50",start=start_date,end=end_date,index=True)
nifty_df = pd.DataFrame(nifty_data)
nifty_df.to_csv('nifty_data.csv')