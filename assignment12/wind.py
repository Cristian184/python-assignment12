import plotly.express as px
import plotly.data as pldata
df = pldata.wind(return_type="pandas")

df["strength"] = df["strength"].str.replace(r"\D", "", regex=True).astype(float)

print("First 10 rows:\n", df.head(10))
print("Last 10 rows:\n", df.tail(10))

fig = px.scatter(df, x="frequency", y="strength", color="direction",
                 title="Wind Strength vs Frequency by Direction",
                 hover_data=["direction"])
fig.write_html("wind.html", auto_open=True)