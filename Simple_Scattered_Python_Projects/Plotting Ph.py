import matplotlib.pyplot as plt

# Sample data extracted from the image (You will need to input the actual data)
# Time in minutes
time = [0, 2, 4, 6, 8, 10, 12, 14]

# Absorbance values for different pH levels
abs_ph7 = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]
abs_ph5 = [0.16, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5]
abs_ph8 = [0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45]
abs_ph3 = [0.22, 0.23, 0.25, 0.27, 0.28, 0.28, 0.28, 0.3]
abs_ph9 = [0.14, 0.15, 0.15, 0.16, 0.16, 0.14, 0.15, 0.15]

# Creating the plot
plt.plot(time, abs_ph7, marker='o', color='blue', label='pH 7')
plt.plot(time, abs_ph5, marker='o', color='green', label='pH 5')
plt.plot(time, abs_ph8, marker='o', color='red', label='pH 8')
plt.plot(time, abs_ph3, marker='o', color='purple', label='pH 3')
plt.plot(time, abs_ph9, marker='o', color='brown', label='pH 9')

# Adding titles and labels
plt.title('Effect of pH on catechol oxidase')
plt.xlabel('Time (min)')
plt.ylabel('Absorbance')

# Adding a legend
plt.legend()

# Show grid
plt.grid(True)

# Display the plot
plt.show()
