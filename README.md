# MAI201 Assignment 2

## Student Information

**Name:** Eric Rathod

## Project Overview

The following is a project that utilizes the concepts of automated data validation and unit testing via the use of Great Expectations and Pytest. The client data set, which contains some data quality problems, has been tested against predefined expectations.

## Project Files

* `MAI201_Assignment2_Eric_Rathod.ipynb` – Main notebook
* `assignment2_report.md` – Assignment report
* `customer_data.csv` – Dataset
* `test_data_utils.py` – Utility functions and Pytest test cases
* `data_docs/` – Great Expectations HTML Data Docs

## Technologies Used

* Python
* Pandas
* Great Expectations
* Pytest
* Google Colab

## Validation Summary

Eight data validation expectations were created:

* Customer ID should not be null
* Customer ID should be unique
* Age should be between 0 and 120
* Email should match a valid format
* Salary should have at least 95% non-null values
* Country should belong to the approved list
* Signup date should follow the required date format
* Table row count should be within the expected range

The dataset intentionally contains data quality issues, so all validation checks correctly identified the problems.

## Pytest Results

* Total Tests: **14**
* Passed: **14**
* Failed: **0**

## Data Docs

Great Expectations Data Docs have been created for the purpose of generating an HTML documentation of the data validation process.

## Author

**Eric Rathod**
