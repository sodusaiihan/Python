import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squeres = [1, 4, 9, 16, 25]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(input_values ,squeres, linewidth = 3)

# Set chart title and label axes.0
ax.set_title("Square Numbers", fontsize = 24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square of value", fontsize = 14)

# Set size of tick labels.
ax.tick_params(axis='both', labelsize = 14)
plt.show()

# Plotting and Styling Individual Points with scatter()
