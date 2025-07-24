from wordcloud import WordCloud  
WordCloud().generate(open("10K.txt").read()).to_file("cloud.png")
