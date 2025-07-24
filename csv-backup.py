import gspread; import pandas as pd  
df = pd.DataFrame(gspread.service_account().open("Sheet1").sheet1.get_all_records());
df.to_csv("backup.csv", index=False)
