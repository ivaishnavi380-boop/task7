import numpy as np
from scipy import stats

# Dataset
marks = [45, 50, 52, 48, 47, 49, 51, 53, 46, 200]

# Z-Score
z_scores = stats.zscore(marks)

print("Z Scores:")
print(z_scores)

# Detect Outliers
outliers = []

for i in range(len(marks)):
    if abs(z_scores[i]) > 3:
        outliers.append(marks[i])

print("Outliers using Z-Score:", outliers)