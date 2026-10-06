import pandas as pd

data = pd.DataFrame({
    "Name": ["Aman", "Riya", "Karan", "Neha", "Aman", "Sahil", "Priya", "Rohit"],
    "Age": [20, 21, 20, None, 20, 22, 21, 20],
    "Study_Hours": [3, 4, "5", 2, 3, None, 4, 6],
    "Attendance": [85, 90, 78, 88, 85, 92, None, 80],
    "Result": ["Pass", "Pass", "Pass", "Pass", "Pass", "Pass", "Pass", "Fail"]
})

data = data.drop_duplicates()

data["Age"] = data["Age"].fillna(data["Age"].median()).astype(int)

data["Study_Hours"] = pd.to_numeric(data["Study_Hours"], errors="coerce")
data["Study_Hours"] = data["Study_Hours"].fillna(data["Study_Hours"].median())

data["Attendance"] = data["Attendance"].fillna(data["Attendance"].median())

print("Cleaned Dataset:")
print(data)

print("\nDataset Shape:")
print(data.shape)

data.to_csv("cleaned_student_dataset.csv", index=False)