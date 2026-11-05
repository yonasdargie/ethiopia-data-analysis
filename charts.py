import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("ethiopia.db")
data = pd.read_sql_query("SELECT * FROM ethiopia ORDER BY year", conn)
conn.close()

data["population_millions"] = data["population"] / 1_000_000
data["gdp_billion_usd"] = data["gdp_usd"] / 1_000_000_000

fig, axes = plt.subplots(2, 2, figsize=(11, 8))
fig.suptitle("Ethiopia: key indicators (World Bank data)")

charts = [
    ("population_millions", "Population (millions)"),
    ("gdp_billion_usd", "GDP (billion USD)"),
    ("life_expectancy", "Life expectancy (years)"),
    ("internet_pct", "Internet users (% of population)"),
]

for ax, (col, title) in zip(axes.flat, charts):
    ax.plot(data["year"], data[col])
    ax.set_title(title)
    ax.set_xlabel("Year")
    ax.grid(True)

plt.tight_layout()
plt.savefig("ethiopia_charts.png", dpi=150)
plt.show()