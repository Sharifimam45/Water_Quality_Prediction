# # 🌊 Southern Bug River Water Quality Forecasting

This project analyzes and forecasts the water quality of the Southern Bug River using historical monitoring data from multiple stations. The dataset covers water quality indicators such as pH, DO, BOD, COD, Nitrate, Phosphate, and more.

---

## 📂 Dataset Description

### 1️⃣ **River Water Quality Dataset**
- Source: [Kaggle - River Water Quality EDA and Forecasting – Southern Bug River](https://www.kaggle.com/datasets/vbmokin/wq-southern-bug-river-01052021)
- Period: 2000–2021
- Stations: 22 monitoring stations
- Columns:
  - `Date`
  - `Station_ID`
  - `pH`
  - `Dissolved Oxygen (DO)`
  - `Biochemical Oxygen Demand (BOD)`
  - `Chemical Oxygen Demand (COD)`
  - `Nitrate`
  - `Phosphate`
  - (and other parameters)

### 2️⃣ **Ammonium Prediction Dataset**
- Source: [Kaggle - Ammonium Prediction in River Water](https://www.kaggle.com/datasets/vbmokin/ammonium-prediction-in-river-water)
- Period: 1996–2019
- Focus: Ammonium nitrogen (NH₄)

---

## 🧪 Project Goals

- Exploratory Data Analysis (EDA)
- Data Cleaning and Preprocessing
- Visualization of water quality indicators
- Forecasting future water quality using machine learning models
- Water Quality Index (WQI) computation

---

## 🛠️ Tools and Technologies

- Python 🐍
- Pandas
- NumPy
- Matplotlib / Seaborn
- Scikit-learn
- Statsmodels
- Jupyter Notebooks

---

## 🚀 Project Structure

```bash
📦 Southern-Bug-Water-Quality
 ┣ 📂 data
 ┃ ┣ 📄 wq-southern-bug-river-01052021.csv
 ┃ ┣ 📄 ammonium-prediction-in-river-water.csv
 ┣ 📂 notebooks
 ┃ ┣ 📄 data_cleaning.ipynb
 ┃ ┣ 📄 eda_visualization.ipynb
 ┃ ┣ 📄 forecasting_model.ipynb
 ┣ 📄 README.md
 ┣ 📄 requirements.txt
