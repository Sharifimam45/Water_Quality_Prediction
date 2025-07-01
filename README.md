# 🌊 Water Quality Prediction using Random Forest

This project demonstrates how to use lagged pollutant features and a Random Forest model to predict **BSK5 (Biochemical Oxygen Demand)**, a key indicator of water pollution. The model uses past values of multiple water quality indicators to make future predictions.

---

## 📁 Files Included

- `Water_Quality_Prediction_RF.ipynb` – Jupyter notebook containing the full data preprocessing, feature engineering, model training, evaluation, and visualization.
- `water_quality.csv` – Input dataset with pollutant readings over time (assumed in `../data/` folder).
- `model_parameters.txt` – Description of model hyperparameters and training setup (optional, for documentation).

---

## 🧠 Project Overview

### ✨ Goal
To predict the **BSK5** value based on:
- Previous (lagged) values of 8 water pollutants
- Time features (year, month)
- Station ID

### 📊 Features Used
- **Lag Features**: Previous 1 to 3 days of:
  - NH4, Suspended, O2, NO3, NO2, SO4, PO4, CL
- **Time-Based Features**: `year`, `month`
- **Location**: `id` (station identifier)

### 🎯 Target
- `BSK5`: Biochemical Oxygen Demand (5-day)

---

## 🔧 Model Details

- **Algorithm**: Random Forest Regressor
- **Library**: scikit-learn
- **Train/Test Split**: 80% train, 20% test (time-based split)
- **Hyperparameters**:
  - `n_estimators`: 200
  - `random_state`: 42

---

## 📈 Evaluation Metrics

- **Mean Squared Error (MSE)**
- **R² Score**
- Visualization: Actual vs Predicted BSK5 values (line plot)

---

## ▶️ How to Run

1. Clone this repo:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name

