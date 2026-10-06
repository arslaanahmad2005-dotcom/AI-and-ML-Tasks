# Data Quality and Leakage

## Data Quality Dimensions

- Completeness
- Consistency
- Accuracy
- Timeliness

Good quality data helps a machine learning model give better results.

## Data Leakage

Data leakage happens when information that would not be available at prediction time is used for training.

It can make model performance look better than it actually is.

## Detection and Prevention

Compare the model results using a proper train-test split and a full dataset.

A big difference in performance can indicate data leakage.

## Dataset Cleaning

- Handle missing values.
- Remove duplicate rows.
- Fix incorrect data types.
- Check the dataset shape before splitting.

Reference: https://scikit-learn.org/stable/common_pitfalls.html

# Data Cleaning Summary

- Missing values were handled.
- Duplicate rows were removed.
- Incorrect data type was fixed.
- Dataset shape was checked before splitting.

These steps improved the quality of the dataset and prepared it for machine learning.