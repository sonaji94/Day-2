# Student Result Analyzer
# Author: Sonu
# Day 2 Project

import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv("students.csv")

# Calculate total and average
data["Total"] = data[["Maths", "Physics", "Chemistry"]].sum(axis=1)
data["Average"] = data["Total"] / 3

# Pass / Fail
data["Result"] = data["Average"].apply(lambda x: "Pass" if x >= 40 else "Fail")

# Display results
print("\nStudent Results:\n")
print(data)

# Topper
topper = data.loc[data["Total"].idxmax()]
print("\nTopper:")
print(topper[["Name", "Total"]])

# Subject-wise average
subject_avg = data[["Maths", "Physics", "Chemistry"]].mean()

# Plot
subject_avg.plot(kind="bar", title="Subject-wise Average Marks")
plt.xlabel("Subject")
plt.ylabel("Average Marks")
plt.tight_layout()
plt.show()
