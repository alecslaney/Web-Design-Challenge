#dependencies
import pandas as pd

#path to data csv, conversion from pandas frame to html
data = "cities.csv"
data = pd.read_csv(data)
html = data.to_html(index=False)

#write html to text file
text_file = open("data_html.txt", "w")
text_file.write(html)
text_file.close()