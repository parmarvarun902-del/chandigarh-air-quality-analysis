
# 🌍 Air Quality Data Analysis of Chandigarh

## 📌 Project Overview

This project analyses sample air-quality data for Chandigarh using Python. It demonstrates how data analysis and visualisation can help us understand pollutant values through statistics, graphs, and correlation analysis.

**Note:** The dataset provided with this project contains simulated educational data, not official or real-time Chandigarh measurements.

## 🎯 Objectives

- Analyse PM2.5, PM10, NO2, and CO values.
- Calculate average pollutant values.
- Generate descriptive statistical summaries.
- Visualise data using different graphs.
- Explore relationships between pollutants using correlation analysis.

## 🛠️ Technologies Used

- **Python 3** — Programming language
- **Pandas** — Data handling and analysis
- **NumPy** — Numerical operations
- **Matplotlib** — Data visualisation

## 📂 Project Structure

```text
Air-Quality-Data-Analysis/
│
├── air_quality_analysis.py
├── chandigarh_air_quality_sample.csv
├── requirements.txt
├── README.md
│
├── graphs/
│   ├── daily_indicator.png
│   ├── pm25_pm10.png
│   ├── average_pollutants.png
│   └── correlation_heatmap.png
│
└── screenshots/
```

## 📊 Dataset Description

The CSV dataset contains sample readings for the following parameters:

| Parameter | Description |
|---|---|
| Date | Date of the sample record |
| PM2.5 | Fine particulate matter |
| PM10 | Particulate matter |
| NO2 | Nitrogen dioxide |
| CO | Carbon monoxide |
| Illustrative Indicator | A simple project-specific indicator |

The dataset contains 30 sample daily records.

## 📈 Visualisations

The project generates the following graphs:

1. **Daily Indicator Graph** — Displays changes in the illustrative indicator.
2. **PM2.5 and PM10 Graph** — Compares the two particulate matter values.
3. **Average Pollutant Graph** — Shows the average values of the selected pollutants.
4. **Correlation Heatmap** — Displays correlations between pollutant variables.

Generated graphs are saved in the `graphs/` folder.

## ⚙️ Installation

Make sure Python 3 is installed on your computer.

Install the required libraries by running:

```bash
pip install -r requirements.txt
```

Alternatively, install them individually:

```bash
pip install pandas numpy matplotlib
```

## ▶️ How to Run the Project

1. Download or clone this repository.
2. Open the project folder in VS Code or another Python editor.
3. Ensure the CSV dataset is in the same folder as the Python script.
4. Run the following command:

```bash
python air_quality_analysis.py
```

5. View the printed analysis and generated graphs.

## 🔍 Expected Results

After running the program, you should see:

- The first five dataset records.
- Descriptive statistics for the pollutants.
- Average pollutant values.
- The highest illustrative indicator in the dataset.
- A correlation matrix.
- Four graphs saved in the `graphs/` directory.

## ✅ Benefits

- Makes sample data easier to understand.
- Demonstrates basic data analysis using Python.
- Presents results in a visual format.
- Provides practice with CSV files and popular Python libraries.

## ⚠️ Limitations

- The supplied dataset is simulated and does not represent actual Chandigarh air-quality readings.
- The illustrative indicator is not the official CPCB Air Quality Index (AQI).
- The analysis is intended for educational purposes only.
- The results should not be used for health decisions or environmental policy.

## 🎓 Learning Outcomes

Through this project, we learn how to:

- Read CSV files using Pandas.
- Calculate averages and descriptive statistics.
- Create graphs using Matplotlib.
- Analyse correlations between numerical variables.
- Organise a Python data-analysis project for GitHub.

## 🔮 Future Scope

- Use verified air-quality data from official monitoring sources.
- Analyse longer periods of data.
- Compare readings across locations.
- Explore forecasting methods after obtaining suitable real-world data.

## 📚 References

- Python: https://docs.python.org/3/
- Pandas: https://pandas.pydata.org/docs/
- NumPy: https://numpy.org/doc/
- Matplotlib: https://matplotlib.org/stable/

## 👨‍💻 Author

**Varun Parmar**

Chandigarh University

---

⭐ This project was created for educational and academic purposes.
