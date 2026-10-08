# Wednesday 7 Oct 2026 — Train/Test Split

## What I learned

### 1. Hold-Out Set

A hold-out set is the data that we keep separate from the training data.

The model does not see this data while training. Later, we use it to check how well the model works on unseen data.

This is important because testing the model on the same data it learned from would not give us a real idea of its performance.

- https://scikit-learn.org/stable/modules/cross_validation.html

### 2. Train/Test Split

I learned how to split a dataset into training and testing data using `train_test_split`.

Some important parameters are:

- `test_size` - decides how much data will be used for testing.
- `random_state` - keeps the split the same every time we run the code.

This is useful because we need reproducible results while working with machine learning models.

- https://scikit-learn.org/stable/modules/cross_validation.html
- https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html

### 3. Stratified Split

For classification problems, we can use `stratify` while splitting the data.

It helps keep a similar class distribution in both the training and testing data.

This is especially useful when the classes are not balanced.

- https://scikit-learn.org/stable/modules/cross_validation.html

### 4. Comparing Split Sizes

I compared different ways of splitting the dataset:

| Split | Training Data | Testing Data |
|---|---:|---:|
| 60/20/20 | 60% | 20% |
| 80/20 | 80% | 20% |

The main thing I noticed is that the amount of data used for training can affect the model's performance, while the test data is used to check how well the model performs on unseen data.

### Conclusion

More training data can help the model learn better, but we still need enough unseen data to properly test the model.