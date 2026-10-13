
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Weather Data Analysis.csv")

print(df.head())
print(df.info())
#print(df.describe(numeric_only=True))

print("\nAverage Temperature:", np.mean(df["Temperature"]))
print("Maximum Temperature:", np.max(df["Temperature"]))
print("Minimum Temperature:", np.min(df["Temperature"]))
print("Average Humidity:", np.mean(df["Humidity"]))
print("Total Rainfall:", np.sum(df["Rainfall"]))

print("\nWeather by City:")
print(df.groupby("City")["Temperature"].mean())

print("\nAverage Humidity by City:")
print(df.groupby("City")["Humidity"].mean())

#df["Date"] = pd.to_datetime(df["Date"])

sns.lineplot(data=df, x="Date", y="Temperature", hue="City", marker="o")
plt.title("Temperature Trends")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

sns.barplot(data=df, x="City", y="Temperature", estimator="mean")
plt.title("Average Temperature by City")
plt.tight_layout()
plt.show()

sns.barplot(data=df, x="City", y="Humidity", estimator="mean")
plt.title("Average Humidity by City")
plt.tight_layout()
plt.show()

sns.barplot(data=df, x="City", y="Rainfall", estimator="sum")
plt.title("Total Rainfall by City")
plt.tight_layout()
plt.show()

sns.scatterplot(data=df, x="Temperature", y="Humidity", hue="City")
plt.title("Temperature vs Humidity")
plt.tight_layout()
plt.show()

sns.histplot(data=df, x="Temperature", bins=10, kde=True)
plt.title("Temperature Distribution")
plt.tight_layout()
plt.show()

print("\nWeather Analysis Completed!")
