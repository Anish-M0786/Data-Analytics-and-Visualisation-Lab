# Experiment 3B: Bivariate Analysis – Linear and Logistic Regression Modeling

## AIM
To perform Bivariate Analysis on the UCI Diabetes Dataset and Pima Indians Diabetes Dataset using Linear Regression and Logistic Regression.

## Requirements
- Python: Version 3.13.2
- Jupyter Notebook: Version 7.3.2

## Theory
- **Python**: Interpreted general-purpose, high-level programming language.
- **Jupyter Notebook**: Interactive environment for executing Python code.
- **NumPy**: Fundamental library for numerical computing in Python.
- **Pandas**: Data manipulation and analysis library providing DataFrame and Series.
- **Seaborn**: Statistical data visualization library built on Matplotlib.
- **Matplotlib**: Powerful plotting library for static, animated, and interactive visualizations.
- **Scikit-Learn (sklearn)**: Machine learning library providing tools for data mining, analysis, and predictive modeling.
- **UCI Diabetes Dataset**: Contains various medical predictor variables and a target variable indicating diabetes presence.
- **Pima Indians Diabetes Dataset**: Includes health-related attributes such as glucose level, blood pressure, BMI, and diabetes diagnosis.

### Bivariate Analysis
Bivariate analysis examines the relationship between two variables.

| Method | Use Case |
|---|---|
| **Linear Regression** | Used when both variables are continuous. Predicts one variable based on another (e.g., BMI from Glucose). |
| **Logistic Regression** | Used when the target variable is categorical (Yes/No). Predicts whether a person has diabetes based on health factors. |

## Procedure
1. Open Jupyter Notebook and import pandas, numpy, matplotlib, seaborn, sklearn.
2. Load the UCI Diabetes and Pima Indians Diabetes datasets.
3. Perform Linear Regression to analyze the relationship between Glucose Level and BMI.
4. Perform Logistic Regression to predict Diabetes Presence based on selected features.
5. Evaluate the models using R² score (for Linear Regression) and Accuracy Score (for Logistic Regression).
6. Compare and interpret the results for both datasets.

## Result
Linear Regression reveals the relationship between Glucose Level and BMI, while Logistic Regression predicts Diabetes Presence with varying accuracy. Differences in R² and accuracy scores indicate dataset variations.
