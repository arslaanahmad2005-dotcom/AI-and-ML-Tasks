# Machine Learning: Definition and Types

## What is Machine Learning?

Machine Learning is a branch of Artificial Intelligence in which computers learn patterns from data and use those patterns to make predictions or decisions without requiring us to manually program every rule.

### Example: Spam Email Detection

Instead of manually writing rules to identify spam emails, we provide examples of spam and non-spam emails to a model. It learns patterns and predicts whether a new email is spam.

## Three Major Types of Machine Learning

### 1. Supervised Learning

The model learns from labeled data, where both the input and the correct output are available.

**Examples:**
- House price prediction
- Email spam detection
- Student result prediction

**Common Algorithms:** Linear Regression, Logistic Regression, and Decision Trees.

### 2. Unsupervised Learning

The model receives data without predefined labels and discovers hidden patterns or groups.

**Examples:**
- Customer segmentation
- Grouping similar products
- Finding unusual transactions

**Common Algorithms:** K-Means, DBSCAN, and Principal Component Analysis (PCA).

### 3. Reinforcement Learning

An agent learns through actions, rewards, and penalties while interacting with an environment.

**Examples:**
- Game-playing AI
- Robotics
- Autonomous decision-making

**Common Methods:** Q-Learning and Deep Q-Networks (DQN).

## Quick Comparison

| Type | Data / Feedback | Main Objective |
|---|---|---|
| Supervised Learning | Labeled data | Predict outcomes |
| Unsupervised Learning | Unlabeled data | Discover patterns |
| Reinforcement Learning | Rewards and interactions | Learn good actions |

## Key Takeaway

- **Supervised Learning:** Learn from examples with known answers.
- **Unsupervised Learning:** Find structure in data without given answers.
- **Reinforcement Learning:** Learn which actions work best through feedback.

# Machine Learning Workflow: From Data to Deployment

## Introduction

The Machine Learning (ML) workflow is a sequence of steps used to develop, train, evaluate, and deploy a Machine Learning model.

It helps us convert raw data into a useful model that can make predictions or decisions.

## Stages of the Machine Learning Workflow

### 1. Problem Definition

Identify the problem that needs to be solved using Machine Learning.

**Example:** Predicting house prices based on area, location, and number of rooms.

### 2. Data Collection

Gather relevant data from different sources such as CSV files, databases, APIs, or datasets.

**Example:** Collecting house prices, locations, and property details.

### 3. Data Preprocessing

Clean and prepare the collected data by:
- Handling missing values
- Removing duplicate records
- Correcting incorrect data
- Converting data into suitable formats

**Tools:** Python, NumPy, Pandas.

### 4. Exploratory Data Analysis (EDA)

Analyze the dataset to understand patterns, relationships, distributions, and trends.

**Tools:** Pandas, Matplotlib, Seaborn.

### 5. Feature Engineering

Select, transform, or create relevant features that help the model learn better.

**Example:** Calculating price per square foot from property price and area.

### 6. Train-Test Split

Divide the dataset into two parts:

- **Training Data:** Used to teach the model.
- **Testing Data:** Used to evaluate the model on unseen examples.

### 7. Model Selection and Training

Choose a suitable Machine Learning algorithm and train it using the training dataset.

**Examples:**
- Linear Regression
- Logistic Regression
- Decision Trees
- Random Forest

**Tool:** Scikit-learn.

### 8. Model Evaluation

Measure how well the trained model performs using appropriate evaluation metrics.

**Examples:**
- Accuracy
- Precision
- Recall
- F1-Score
- Mean Squared Error (MSE)

### 9. Model Deployment

Integrate the trained model into a real-world application so users can access its predictions.

**Tools:** Flask, FastAPI, Docker, AWS, or Google Cloud.

### 10. Model Monitoring and Maintenance

Monitor the model's performance after deployment, detect changes in data, and retrain or update it when necessary.

## Machine Learning Workflow Summary

Problem Definition
        ↓
Data Collection
        ↓
Data Preprocessing
        ↓
Exploratory Data Analysis
        ↓
Feature Engineering
        ↓
Train-Test Split
        ↓
Model Selection and Training
        ↓
Model Evaluation
        ↓
Model Deployment
        ↓
Monitoring and Maintenance

## Why is the ML Workflow Important?

1. Provides a structured approach to solving problems.
2. Improves data quality and model reliability.
3. Helps prevent common errors such as data leakage.
4. Makes experiments reproducible.
5. Ensures that models are properly evaluated before deployment.
6. Helps maintain model performance in real-world applications.

## Conclusion

The Machine Learning workflow provides a roadmap for transforming raw data into an intelligent application.

Understanding these stages is essential before implementing Machine Learning algorithms because building a successful ML solution involves much more than simply training a model.

## Learning Outcome

I understood the major stages of the Machine Learning lifecycle, from problem definition and data collection to model training, evaluation, deployment, and monitoring.

**Day 01 Deliverable: ML Workflow Orientation Completed.**