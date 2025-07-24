import openai  
print(openai.ChatCompletion.create(model="gpt-4o", messages=[{"role":"user","content":open("nda.txt").read()+"\nSummarize in plain English."}]))
