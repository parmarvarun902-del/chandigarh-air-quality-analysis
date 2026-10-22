
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

os.makedirs("graphs", exist_ok=True)

data = pd.read_csv("chandigarh_air_quality_sample.csv")

print("AIR QUALITY DATA ANALYSIS - CHANDIGARH")
print("\nFirst Five Records:")
print(data.head())

pollutants = [
    "PM2.5 (µg/m³)",
    "PM10 (µg/m³)",
    "NO2 (µg/m³)",
    "CO (mg/m³)"
]

print("\nDataset Information:")
print(data.info())

print("\nStatistical Summary:")
print(data[pollutants].describe().round(2))

print("\nAverage Pollutant Values:")
print(data[pollutants].mean().round(2))

print("\nMaximum PM2.5 Value:")
print(data["PM2.5 (µg/m³)"].max())

print("\nMaximum PM10 Value:")
print(data["PM10 (µg/m³)"].max())

highest_day = data.loc[
    data["Illustrative Indicator"].idxmax()
]

print("\nHighest Illustrative Indicator:")
print(highest_day[["Date", "Illustrative Indicator"]])

plt.figure(figsize=(10, 5))
plt.plot(
    data["Date"],
    data["Illustrative Indicator"],
    marker="o"
)
plt.title("Daily Illustrative Air Quality Indicator - Chandigarh")
plt.xlabel("Date")
plt.ylabel("Illustrative Indicator (Not Official AQI)")
plt.xticks(rotation=60)
plt.tight_layout()
plt.savefig("graphs/daily_indicator.png")
plt.show()

plt.figure(figsize=(10, 5))
plt.plot(
    data["Date"],
    data["PM2.5 (µg/m³)"],
    marker="o",
    label="PM2.5"
)
plt.plot(
    data["Date"],
    data["PM10 (µg/m³)"],
    marker="s",
    label="PM10"
)
plt.title("PM2.5 and PM10 Sample Values")
plt.xlabel("Date")
plt.ylabel("Concentration (µg/m³)")
plt.legend()
plt.xticks(rotation=60)
plt.tight_layout()
plt.savefig("graphs/pm25_pm10.png")
plt.show()

averages = data[pollutants].mean()

plt.figure(figsize=(8, 5))
averages.plot(kind="bar")
plt.title("Average Pollutant Values")
plt.xlabel("Pollutants")
plt.ylabel("Average Value (Units Vary)")
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig("graphs/average_pollutants.png")
plt.show()

correlation = data[pollutants].corr()

plt.figure(figsize=(7, 5))
plt.imshow(correlation, aspect="auto")
plt.colorbar(label="Correlation")
plt.xticks(
    range(len(pollutants)),
    pollutants,
    rotation=35,
    ha="right"
)
plt.yticks(range(len(pollutants)), pollutants)
plt.title("Correlation Between Sample Pollutants")
plt.tight_layout()
plt.savefig("graphs/correlation_heatmap.png")
plt.show()

print("\nCorrelation Matrix:")
print(correlation.round(2))

print("\nAll graphs have been saved in the graphs folder.")
print("Analysis completed successfully.")
