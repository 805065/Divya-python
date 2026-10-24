import pandas as pd
import numpy as np
from functions import calculate_total, calculate_average, assign_grade, get_result

print("=== Student Performance Analytics System ===")

# Step 1 - Data Load
df = pd.read_csv("students.csv")
print(f"\nTotal Students: {len(df)}")
print(df.head())

# Step 2 - Calculation using Loop
results = []
for index, row in df.iterrows():
    marks = [row['Python'], row['Maths'], row['English']]
    total = calculate_total(marks)
    avg = calculate_average(marks)
    grade = assign_grade(avg)
    status = get_result(avg, row['Attendance'])
    results.append([row['Name'], total, round(avg,2), grade, status])

result_df = pd.DataFrame(results, columns=['Name','Total','Average','Grade','Result'])
print("\n--- Student Results ---")
print(result_df)

# Step 3 - Analysis using NumPy & Pandas
print("\n--- Overall Analysis ---")
print(f"Class Average: {np.mean(result_df['Average']):.2f}")
print(f"Highest Average: {np.max(result_df['Average'])}")
print(f"Lowest Average: {np.min(result_df['Average'])}")
print(f"Pass Count: {(result_df['Result']=='Pass').sum()}")
print(f"Fail Count: {(result_df['Result']=='Fail').sum()}")

print("\n--- Subject Wise Average ---")
print(f"Python: {df['Python'].mean():.2f}")
print(f"Maths: {df['Maths'].mean():.2f}")
print(f"English: {df['English'].mean():.2f}")

print("\n--- Top 3 Performers ---")
top3 = result_df.sort_values(by='Average', ascending=False).head(3)
print(top3)

# Save output
result_df.to_csv("results.csv", index=False)
print("\nResults saved to results.csv")