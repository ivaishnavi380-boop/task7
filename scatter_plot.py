import matplotlib.pyplot as plt

# X and Y values
x = [1,2,3,4,5,6,7,8,9,10]
y = [45,50,52,48,47,49,51,53,46,200]

# Scatter Plot
plt.scatter(x, y)

plt.title("Scatter Plot")
plt.xlabel("Student Number")
plt.ylabel("Marks")

plt.show()