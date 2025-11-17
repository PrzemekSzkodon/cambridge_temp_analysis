# Cambridge Temperature Forecasting Analysis

Time series analysis and forecasting of monthly maximum temperatures in Cambridge, UK (1959-2018).

## 📊 Project Overview

This project performs econometric analysis on Cambridge temperature data to:
- Analyze time series patterns and seasonality
- Detect signs of global warming trends
- Model autocorrelation structures
- Forecast future temperature values

## 📁 Data

**Dataset**: `cambridge.dta` (Stata format) or `cambridge.csv`

**Variables**:
- `maxtemp`: Monthly means of daily maximum temperature (degrees Celsius)
- Time period: January 1959 to September 2018
- Example: September 2018 average maximum daily temperature = 19.9°C

## 🎯 Analysis Tasks

### (a) Exploratory Time Series Analysis
- Create a time series plot of `maxtemp`
- Summarize the behavior of the time series
- Plot the correlogram (autocorrelation function) of `maxtemp`
- Comment on patterns and characteristics

### (b) Seasonal Decomposition via Regression
- Regress `maxtemp` on month dummies (avoiding dummy variable trap)
- Interpret the regression coefficients
- Save residuals as variable `res`

### (c) Residual Analysis and Global Warming Detection
- Create a time series plot of residuals (`res`)
- Analyze for signs of global warming trend
- Plot correlogram of `res`
- Comment on findings

### (d) Trend Removal
- Regress `res` on time index variable `t` and a constant
- Save residuals as variable `res1`
- Plot correlogram of `res1`
- Compare with correlogram of `res` and explain differences

### (e) AR(1) Modeling
- Estimate an AR(1) model for `res1`
- Test hypothesis of no AR(1) serial correlation in model errors

### (f) Forecasting
- Using estimates from parts (b)-(e), forecast the mean daily maximum temperature in Cambridge for February 2018

## 🛠️ Setup

### Requirements

```bash
# Install required packages
pip install pandas numpy matplotlib seaborn statsmodels scipy
```

### Required Python Packages

- `pandas` - Data manipulation and reading .dta files
- `numpy` - Numerical operations
- `matplotlib` - Basic plotting
- `seaborn` - Statistical visualizations
- `statsmodels` - Econometric models (AR models, regression, correlograms)
- `scipy` - Statistical tests

Or create a `requirements.txt`:

```bash
pandas>=1.5.0
numpy>=1.23.0
matplotlib>=3.6.0
seaborn>=0.12.0
statsmodels>=0.14.0
scipy>=1.9.0
```

Install with:
```bash
pip install -r requirements.txt
```

## 🚀 Usage

```bash
# Run the analysis script
python question_3.py
```

The script performs all analysis tasks (a)-(f) and generates:
- Time series plots
- Correlograms (ACF plots)
- Regression results
- AR(1) model estimates
- Temperature forecast for February 2018

## 📂 Project Structure

```
cambridge_temp_analysis/
│
├── question_3.py          # Main analysis script
├── cambridge.dta          # A: Input data (Stata format)
├── cambridge.csv          # or B: Input data (CSV format, if available)
├── README.md              # This file
├── .gitignore            # Git ignore file
└── requirements.txt      # Python dependencies (optional)
```

## 📈 Methods Used

- **Time Series Visualisation**: Time plots and correlograms
- **Seasonal Dummy Regression**: Capturing monthly seasonality
- **Trend Analysis**: Detecting long-term warming patterns
- **AR(1) Modelling**: Modeling autocorrelation in residuals
- **Forecasting**: Combining seasonal, trend, and AR components

## 🔬 Key Econometric Concepts

- Dummy variable trap avoidance
- Seasonal decomposition
- Global warming trend detection
- Serial correlation analysis
- AR(1) modeling and hypothesis testing
- Out-of-sample forecasting

## 📝 Notes

- The analysis covers **59 years** of monthly temperature data
- Data spans from **January 1959** to **September 2018**
- Final forecast target: **February 2018** mean maximum temperature

## 🎓 Course Context

This project is part of **E300 Econometrics** coursework at the University of Cambridge, focusing on time series analysis, forecasting, and econometric modeling.

## 📄 License

Educational project for coursework purposes.

---

**Author**: Przemek Szkodon  
**Course**: E300 Econometrics  
**Institution**: University of Cambridge
