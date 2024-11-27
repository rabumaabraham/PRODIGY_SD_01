import tkinter as tk
from tkinter import messagebox

def convert_temperature():
    try:
        temp = float(entry_temp.get())
        unit = var_unit.get()

        if unit == "Celsius":
            fahrenheit = (temp * 9/5) + 32
            kelvin = temp + 273.15
            result.set(f"Fahrenheit: {fahrenheit:.2f}°F\nKelvin: {kelvin:.2f}K")
        elif unit == "Fahrenheit":
            celsius = (temp - 32) * 5/9
            kelvin = celsius + 273.15
            result.set(f"Celsius: {celsius:.2f}°C\nKelvin: {kelvin:.2f}K")
        elif unit == "Kelvin":
            celsius = temp - 273.15
            fahrenheit = (celsius * 9/5) + 32
            result.set(f"Celsius: {celsius:.2f}°C\nFahrenheit: {fahrenheit:.2f}°F")
        else:
            result.set("Please select a valid unit.")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid numeric temperature.")

# Create the main window
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("500x400")
root.resizable(False, False)
root.config(bg="#f4f4f4")

# Header
header = tk.Label(
    root,
    text="Temperature Converter",
    font=("Arial", 18, "bold"),
    bg="#3b5998",
    fg="white",
    padx=10,
    pady=10
)
header.pack(fill=tk.X)

# Input Section
frame_input = tk.Frame(root, bg="#f4f4f4", pady=20)
frame_input.pack()

tk.Label(frame_input, text="Enter Temperature:", font=("Arial", 12), bg="#f4f4f4").grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_temp = tk.Entry(frame_input, width=10, font=("Arial", 12))
entry_temp.grid(row=0, column=1, padx=10, pady=5)

# Unit Selection
tk.Label(frame_input, text="Select Unit:", font=("Arial", 12), bg="#f4f4f4").grid(row=1, column=0, padx=10, pady=5, sticky="e")

var_unit = tk.StringVar(value="Celsius")
units_frame = tk.Frame(frame_input, bg="#f4f4f4")
units_frame.grid(row=1, column=1, padx=10, pady=5)

tk.Radiobutton(units_frame, text="Celsius", variable=var_unit, value="Celsius", font=("Arial", 10), bg="#f4f4f4").pack(side=tk.LEFT, padx=5)
tk.Radiobutton(units_frame, text="Fahrenheit", variable=var_unit, value="Fahrenheit", font=("Arial", 10), bg="#f4f4f4").pack(side=tk.LEFT, padx=5)
tk.Radiobutton(units_frame, text="Kelvin", variable=var_unit, value="Kelvin", font=("Arial", 10), bg="#f4f4f4").pack(side=tk.LEFT, padx=5)

# Convert Button
convert_button = tk.Button(
    root,
    text="Convert",
    font=("Arial", 12, "bold"),
    bg="#3b5998",
    fg="white",
    relief=tk.RAISED,
    command=convert_temperature
)
convert_button.pack(pady=20)

# Result Display
result = tk.StringVar()
result_label = tk.Label(
    root,
    textvariable=result,
    font=("Arial", 14),
    bg="#f4f4f4",
    fg="#333333",
    justify="center"
)
result_label.pack(pady=10)

# Footer
footer = tk.Label(
    root,
    text="Created with ❤ by Rabuma",
    font=("Arial", 10, "italic"),
    bg="#3b5998",
    fg="white",
    pady=10
)
footer.pack(fill=tk.X)

# Run the application
root.mainloop()
