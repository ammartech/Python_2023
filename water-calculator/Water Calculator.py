import tkinter as tk
from tkinter import messagebox

def calculate_water_intake():
    try:
        weight = float(weight_entry.get())
        age = float(age_entry.get())

        water_intake = (weight / 2.2) * (age / 28.3) / 8

        if water_intake >= intake_slider.get():
            message = "Your water intake is sufficient. Drink enough water to stay hydrated."
        else:
            message = "Your water intake is below the recommended amount. Drink more water to stay hydrated."

        messagebox.showinfo("Water Intake", message)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid weight and age.")

# Create the main window
window = tk.Tk()
window.title("Water Calculator")
window.geometry("400x200")

# Create and place the widgets
label_frame = tk.LabelFrame(window, text="Enter Details")
label_frame.pack(pady=10)

weight_label = tk.Label(label_frame, text="Weight (kg):")
weight_label.grid(row=0, column=0, padx=10, pady=5)
weight_entry = tk.Entry(label_frame)
weight_entry.grid(row=0, column=1, padx=10, pady=5)

age_label = tk.Label(label_frame, text="Age:")
age_label.grid(row=1, column=0, padx=10, pady=5)
age_entry = tk.Entry(label_frame)
age_entry.grid(row=1, column=1, padx=10, pady=5)

intake_label = tk.Label(label_frame, text="Water Intake (oz):")
intake_label.grid(row=2, column=0, padx=10, pady=5)
intake_slider = tk.Scale(label_frame, from_=0, to=100, orient=tk.HORIZONTAL)
intake_slider.grid(row=2, column=1, padx=10, pady=5)

calculate_button = tk.Button(window, text="Calculate", command=calculate_water_intake)
calculate_button.pack(pady=10)

# Start the main event loop
window.mainloop()
