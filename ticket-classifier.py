import openai, pandas as pd  
df = pd.read_csv("tickets.csv")
df["category"] = df["text"].apply(lambda x: openai.ChatCompletion.create(model="gpt-4o", messages=[{"role":"user","content":f"Classify: {x}"}])["choices"][0]["message"]["content"])
