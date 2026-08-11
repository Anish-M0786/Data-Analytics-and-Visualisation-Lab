# Experiment 2C: Reading Data from Text Files, Excel, and the Web

## AIM
To read and process data from various sources, including text files, Excel spreadsheets, and web-based data, using Python's Pandas library.

## Requirements
- Python: Version 3.13.2
- Jupyter Notebook: Version 7.3.2

## Theory
- **Python**: Interpreted general-purpose, high-level programming language with easy syntax and dynamic semantics.
- **Jupyter Notebook**: An interactive environment that allows executing Python code.
- **Pandas**: A powerful Python library for data analysis and manipulation. It provides functions to read data from different formats like CSV, text, Excel, and web-based sources such as JSON and HTML.

## Procedure
1. Open Jupyter Notebook and import Pandas.
2. Read data from a CSV file using `pd.read_csv()`.
3. Read data from an Excel file using `pd.read_excel()`.
4. Read data from a web-based source (URL) using `pd.read_csv(url)`.
5. Display the first few rows of each dataset using `.head()`.
6. Handle missing values using `ffill()`, `bfill()`, or `dropna()`.
7. Save the processed data into new file formats using `.to_csv()` and `.to_excel()`.
8. Run the script and check the output files.

## Input Files Required
| File | Format | Description |
|---|---|---|
| `Google_data.csv` | CSV | Google Play Store app dataset |
| `data.xlsx` | Excel | Sample product/sales data |
| Web URL | CSV | Countries dataset from GitHub |

## Result
The experiment successfully demonstrated reading data from text files, Excel spreadsheets, and web-based sources using Pandas. The output verified the correctness of each operation performed.
