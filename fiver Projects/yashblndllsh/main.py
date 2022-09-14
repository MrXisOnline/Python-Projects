import pandas as pd
from breeze_connect import BreezeConnect
from dotenv import load_dotenv
import os
import time
import datetime

# Loading Environment Variables
load_dotenv("C:\\Users\\SG704\\PythonProjects\\fiver Projects\\yashblndllsh\\.env")

# Environment Variables
SESSION_KEY = os.environ["SESSION_KEY"]
APP_KEY = os.environ["APP_KEY"]
SECRET_KEY = os.environ["SECRET_KEY"]

# Loading excel file which will be updated
data = pd.read_excel("C:\\Users\\SG704\\OneDrive\\Documents\\NSE_NIFTY.xlsx")

# Removing instances where expiry date isn't defined
data = data[data["Expiry"].isnull() == False]

# Connecting to the API
isec = BreezeConnect(api_key=APP_KEY)
isec.generate_session(api_secret=SECRET_KEY, session_token=SESSION_KEY)
time_interval = "30minute"


for i in range(0, len(data)):

    print("\n"*100)
    print(f"{round((i/len(data))*100, 2)}% Completed...")
    # after every 10 iteration this will reset connection
    if i % 10 == 0:
        isec = BreezeConnect(api_key=APP_KEY)
        isec.generate_session(api_secret=SECRET_KEY, session_token=SESSION_KEY)
    record = data.iloc[i]

    # Creating all temporary Variables
    start_date = record.time.strftime("%Y-%m-%dT00:00:00.000Z")
    end_date = record.time.strftime("%Y-%m-%d") + record["time.1"].strftime("T%H:%M:%S.000Z")
    expiry = record.Expiry.strftime("%Y-%m-%dT15:15:00.000Z")

    # get Buy/Sell Strike Value on particular instance
    for j, strike in enumerate([int(record["Sell Strike"]), int(record["Buy Strike"])]):

        # Downloading Historical Data for Start Date
        data1 = isec.get_historical_data(interval=time_interval,
                                         from_date=start_date,
                                         to_date=end_date,
                                         stock_code="NIFTY",
                                         exchange_code="NFO",
                                         product_type="options",
                                         expiry_date=expiry,
                                         right=record["TradeDecision"],
                                         strike_price=strike)

        try:
            # Loading Historical Data
            df = pd.DataFrame(data1["Success"])

            # Checking Historical Data is Right
            if len(df.columns) != 0:
                if j == 0:

                    # Appending the Sell Value for Start Date in the Excel
                    if record["time.1"] == datetime.time(10, 15, 0):
                        data.at[i, "Sell-StrikePrice"] = df.iloc[2]["open"]
                        # print(pd.DataFrame(data1["Success"])["open"].iloc[1])
                    elif record["time.1"] == datetime.time(11, 15, 0):
                        data.at[i, "Sell-StrikePrice"] = df.iloc[4]["open"]
                        # print(pd.DataFrame(data1["Success"])["open"].iloc[3])
                    elif record["time.1"] == datetime.time(12, 15, 0):
                        data.at[i, "Sell-StrikePrice"] = df.iloc[6]["open"]
                        # print(pd.DataFrame(data1["Success"])["open"].iloc[5])
                    elif record["time.1"] == datetime.time(13, 15, 0):
                        data.at[i, "Sell-StrikePrice"] = df.iloc[8]["open"]
                        # print(pd.DataFrame(data1["Success"])["open"].iloc[7])
                else:

                    # Appending the Buy Value for Start Date in the Excel
                    if record["time.1"] == datetime.time(10, 15, 0):
                        data.at[i, "Buy-StrikePrice"] = df.iloc[2]["open"]
                        # print(pd.DataFrame(data1["Success"])["open"].iloc[1])
                    elif record["time.1"] == datetime.time(11, 15, 0):
                        data.at[i, "Buy-StrikePrice"] = df.iloc[4]["open"]
                        # print(pd.DataFrame(data1["Success"])["open"].iloc[3])
                    elif record["time.1"] == datetime.time(12, 15, 0):
                        data.at[i, "Buy-StrikePrice"] = df.iloc[6]["open"]
                        # print(pd.DataFrame(data1["Success"])["open"].iloc[5])
                    elif record["time.1"] == datetime.time(13, 15, 0):
                        data.at[i, "Buy-StrikePrice"] = df.iloc[8]["open"]
                        # print(pd.DataFrame(data1["Success"])["open"].iloc[7])
        except:
            continue
        # 1-Second Sleep so Because API can only answer 75 calls per minute
        time.sleep(1)

        # Downloading Historical Data for Expiry Date
        data2 = isec.get_historical_data(interval=time_interval,
                                         from_date=expiry,
                                         to_date=expiry,
                                         stock_code="NIFTY",
                                         exchange_code="NFO",
                                         product_type="options",
                                         expiry_date=expiry,
                                         right=record["TradeDecision"],
                                         strike_price=strike)

        try:
            df = pd.DataFrame(data2["Success"])
            if len(df.columns) != 0:
                if j == 0:
                    data.at[i, "Sell-Square"] = df.iloc[-1]["close"]
                else:
                    data.at[i, "Buy-Square"] = df.iloc[-1]["close"]
        except:
            continue
        time.sleep(1)

# Saving New Data into Excel Name Can be changed to Orginal Excel File(Will Cause All instance with no Expiry Date to Vanish)
data.to_excel("C:\\Users\\SG704\\OneDrive\\Documents\\New_NSE_NIFTY.xlsx")

