# Experiment 3C: Statistical Analysis Using Diabetes Datasets – Multiple Regression Analysis

## AIM
To perform multiple regression analysis on the UCI Diabetes and Pima Indians Diabetes datasets to predict BMI based on multiple independent variables.

## Requirements
- Python: Version 3.13.2
- Jupyter Notebook: Version 7.3.2

## Dataset Description
| Dataset | Description |
|---|---|
| **UCI Diabetes Dataset** | Contains medical predictor variables and a target variable indicating diabetes presence |
| **Pima Indians Diabetes Dataset** | Includes health-related attributes of Pima Indian women with diabetes diagnosis labels |

## Theory
- **Python**: Interpreted general-purpose, high-level programming language.
- **Jupyter Notebook**: Interactive environment for executing Python code.
- **NumPy**: Fundamental library for numerical computing in Python.
- **Pandas**: Data manipulation and analysis library providing DataFrame and Series.
- **Seaborn**: Statistical data visualization library built on Matplotlib.
- **Matplotlib**: Powerful plotting library for static, animated, and interactive visualizations.
- **Scikit-Learn (sklearn)**: Machine learning library providing tools for data mining, analysis, and predictive modeling.
- **Multiple Regression**: A statistical method that models the relationship between a dependent variable and multiple independent variables. It helps in predicting outcomes and analyzing the impact of multiple factors simultaneously.

### Independent Variables (Features)
- Glucose
- BloodPressure
- Age

### Target Variable
- BMI

## Procedure
1. Import required libraries.
2. Load UCI and Pima Indians Diabetes datasets.
3. Select relevant independent variables.
4. Split data into training (80%) and testing (20%) sets.
5. Train a multiple regression model using independent variables.
6. Evaluate model performance using R² score.
7. Compare results between both datasets.

## Result
Multiple Regression analysis predicts BMI using Glucose, Blood Pressure, and Age. Differences in R² scores indicate variations in data distribution and model performance across datasets.
