import sqlite3
import pandas as pd

conn = sqlite3.connect("ethiopia.db")

def run(title, sql):
    print("\n" + title)
    print(pd.read_sql_query(sql, conn))

run("1. Population since 2015", """
SELECT year, population
FROM ethiopia
WHERE year >= 2015
ORDER BY year
""")

run("2. Average life expectancy and internet use per decade", """
SELECT (year / 10) * 10 AS decade,
       AVG(life_expectancy) AS avg_life_expectancy,
       AVG(internet_pct) AS avg_internet_pct
FROM ethiopia
GROUP BY decade
ORDER BY decade
""")

run("3. First 5 years with internet use above 10 percent", """
SELECT year, internet_pct
FROM ethiopia
WHERE internet_pct > 10
ORDER BY year
LIMIT 5
""")

run("4. GDP per person (USD) since 2010", """
SELECT year, gdp_usd / population AS gdp_per_person
FROM ethiopia
WHERE gdp_usd IS NOT NULL AND year >= 2010
ORDER BY year
""")

conn.close()