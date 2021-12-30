import gspread
from separator import DataSeparator
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint


data = input("Tell me What you did today? \n")
rd_ins = DataSeparator(data)
row_data = rd_ins.sender()

# hook API
scope = ["https://spreadsheets.google.com/feeds",
         'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file",
         "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)
sheet = client.open("tracker").sheet1

# Show records
# data = sheet.get_all_records()
# pprint(data)
# get row
# row = sheet.row_values(2)
# pprint(row)
# get column
# col = sheet.col_values(1)
# pprint(col)

for d in row_data:
    rows = len(sheet.get_all_records())
    sheet.insert_row(d, rows+2)
print("DONE")
