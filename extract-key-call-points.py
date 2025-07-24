import openai  
transcript = open("zoom_transcript.txt").read()  
print(openai.ChatCompletion.create(model="gpt-4o", messages=[{"role":"user","content":f"Summarize this call:\n{transcript}"}]))
