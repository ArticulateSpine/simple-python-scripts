import os, time, requests  
while not os.path.exists("report.csv"): time.sleep(5)  
requests.post("https://slack.webhook.url", json={"text": "New report.csv uploaded!"})
