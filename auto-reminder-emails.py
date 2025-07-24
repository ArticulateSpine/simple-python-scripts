import pandas as pd, smtplib  
[smtplib.SMTP("smtp.gmail.com",587).sendmail("me@gmail.com", row["email"], "Reminder!") for _, row in pd.read_excel("contacts.xlsx").iterrows()]
