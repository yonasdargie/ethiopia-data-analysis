import pandas as pd

df = pd.read_csv("API_SP.POP.TOTL_DS2_en_csv_v2_5254.csv", skiprows=4)
eth = df[df["Country Code"] == "ETH"]
print(eth[["Country Name", "2000", "2010", "2020"]])