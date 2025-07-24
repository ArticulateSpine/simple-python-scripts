import requests; from collections import Counter  
print(Counter(requests.get("https://other-website.com").text.lower().split()))
