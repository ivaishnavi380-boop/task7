import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.preprocessing import StandardScaler

# Load Titanic Dataset
df = sns.load_dataset("titanic")

# Quartiles
Q1 = df['age'].quantile(0.25)
Q2 = df['age'].quantile(0.50)
Q3 = df['age'].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

print("Q1 =", Q1)
print("Median =", Q2)
print("Q3 =", Q3)
print("IQR =", IQR)

outliers = df[(df['age'] < lower_bound) |
              (df['age'] > upper_bound)]

print("Number of Outliers =", len(outliers))

# Box Plot
plt.boxplot(df['age'].dropna())
plt.title("Box and Whisker Plot - Age")
plt.show()

# Z Score
z_scores = stats.zscore(df['age'].dropna())

outliers_z = df['age'].dropna()[abs(z_scores) > 3]

print("\nOutliers using Z Score")
print(outliers_z)

# Standardization
scaler = StandardScaler()

df['age_standardized'] = scaler.fit_transform(
    df[['age']].fillna(df['age'].mean())
)

print("\nStandardized Data")
print(df[['age', 'age_standardized']].head())

# Scatter Plot
plt.scatter(df['age'], df['fare'])
plt.xlabel("Age")
plt.ylabel("Fare")
plt.title("Scatter Plot : Age vs Fare")
plt.show()