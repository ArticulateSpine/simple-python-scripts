import requests; from bs4 import BeautifulSoup  
print([job.text for job in BeautifulSoup(requests.get("https://example.com/jobs").text, "html.parser").find_all("h2")])
