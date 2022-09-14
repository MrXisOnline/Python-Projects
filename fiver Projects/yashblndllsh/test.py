import datetime
import pandas as pd
from breeze_connect import BreezeConnect

data = pd.read_excel("C:\\Users\\SG704\\OneDrive\\Documents\\bug in file.xlsx")

# # Removing instances where expiry date isn't defined

SESSION_KEY = '1613992'
APP_KEY = '3F15H9n51K*65059628d1f8Bs0058771'
SECRET_KEY = '99294jiM6hF06B9945F6385584565m76'

data = data[data["Expiry"].isnull() == False]
for i in range(0, len(data)):
    data["time.1"] = data["time.1"].apply(lambda x: str(x))
    record = data.iloc[i]
    date_str = record.time.strftime("%Y-%m-%d ") + record["time.1"]
    date = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    start_date = record.time.strftime("%Y-%m-%dT00:00:00.000Z")
    end_date = date.strftime("%Y-%m-%dT%H:%M:%S.000Z")
    expiry = record.Expiry.strftime("%Y-%m-%dT15:15:00.000Z")
    print(date)
    isec = BreezeConnect(api_key=APP_KEY)
    isec.generate_session(api_secret=SECRET_KEY, session_token=SESSION_KEY)
    time_interval = "30minute"

    data1 = isec.get_historical_data(interval=time_interval,
                                     from_date=start_date,
                                     to_date=end_date,
                                     stock_code="NIFTY",
                                     exchange_code="NFO",
                                     product_type="options",
                                     expiry_date=expiry,
                                     right=record["TradeDecision"],
                                     strike_price=int(record["Sell Strike"]))
    df = pd.DataFrame(data1["Success"])
    if date.time() == datetime.time(10, 15, 0):
        # data.at[i, "Sell-StrikePrice"] = df.iloc[2]["open"]
        print(pd.DataFrame(data1["Success"])["open"].iloc[2])
    elif date.time() == datetime.time(11, 15, 0):
        # data.at[i, "Sell-StrikePrice"] = df.iloc[4]["open"]
        print(pd.DataFrame(data1["Success"])["open"].iloc[4])
    elif date.time() == datetime.time(12, 15, 0):
        # data.at[i, "Sell-StrikePrice"] = df.iloc[6]["open"]
        print(pd.DataFrame(data1["Success"])["open"].iloc[6])
    elif date.time() == datetime.time(13, 15, 0):
        # data.at[i, "Sell-StrikePrice"] = df.iloc[8]["open"]
        print(pd.DataFrame(data1["Success"])["open"].iloc[8])
    elif date.time() == datetime.time(14, 15, 0):
        # data.at[i, "Sell-StrikePrice"] = df.iloc[8]["open"]
        print(data1)