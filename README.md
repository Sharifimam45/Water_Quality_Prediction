# 🌊 Water Quality Prediction Project

This project uses historical water quality data to forecast `BSK5` values using lag-based features and a Random Forest model.

## 📂 Folder Structure

```
Water_Quality_Prediction/
├── data/                   # Input dataset (water_quality.csv)
├── notebook/               # Model notebook or scripts
├── results/                # Prediction output files
├── requirements.txt        # List of required packages
└── README.md               # This file
```

## 🛠️ How to Run

1. Place your dataset as `data/water_quality.csv`
2. Run the notebook or script from the `notebook/` folder
3. Required packages are listed in `requirements.txt`

## 📊 Model

- Algorithm: Random Forest Regressor
- Features: Lag values of key water quality indicators + time-based features
- Target: `BSK5`

## 📈 Output

- Mean Squared Error and R² Score
- Plot comparing actual vs predicted `BSK5`