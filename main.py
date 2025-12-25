import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42) 
marks = np.random.randint(40, 100, 50)  

data = pd.DataFrame({
    "Student_ID": range(1, 51),
    "Assignment_Marks": marks
})

print("Dataset Preview:")
print(data.head())

mean_marks = data["Assignment_Marks"].mean()
std_marks = data["Assignment_Marks"].std()

print("\nMean Marks:", round(mean_marks, 2))
print("Standard Deviation:", round(std_marks, 2))

plt.figure(figsize=(8, 5))
plt.hist(data["Assignment_Marks"], bins=10, color='skyblue', edgecolor='black')


plt.axvline(mean_marks, color='red', linestyle='dashed', linewidth=2, label='Mean')

plt.title("Distribution of Assignment Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.legend()
plt.grid(axis='y', alpha=0.3)

plt.show()

if std_marks < 10:
    print("\nGrading is fairly consistent.")
else:
    print("\nThere is high variation in grading.")
