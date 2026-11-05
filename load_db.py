import glob
import sqlite3
import pandas as pd

# indicator code in the file name -> column name in our table
indicators = {
    "SP.POP.TOTL": "population",
    "NY.GDP.MKTP.CD": "gdp_usd",
    "SP.DYN.LE00.IN": "life_expectancy",
    "IT.NET.USER.ZS": "internet_pct",
}

tables = []
for code, name in indicators.items():
    filename = glob.glob("API_" + code + "*.csv")[0]
    df = pd.read_csv(filename, skiprows=4)
    eth = df[df["Country Code"] == "ETH"]
    years = [c for c in eth.columns if c.isdigit()]
    long = eth[years].melt(var_name="year", value_name=name)
    long["year"] = long["year"].astype(int)
    tables.append(long)

data = tables[0]
for t in tables[1:]:
    data = data.merge(t, on="year")

conn = sqlite3.connect("ethiopia.db")
data.to_sql("ethiopia", conn, if_exists="replace", index=False)
conn.close()

print(data.shape)
print(data.tail())