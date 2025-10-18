import tkinter as tk

# Function to calculate simple interest
def calculate_si():
    try:
        p = float(principal_entry.get())
        r = float(rate_entry.get())
        t = float(time_entry.get())

        si = (p * r * t) / 100
        result_label.config(text=f"Simple Interest = ₹{si:.2f}")
    except ValueError:
        result_label.config(text="Please enter valid numbers.")

# Create main window
window = tk.Tk()
window.title("Simple Interest Calculator")
window.geometry("350x250")
window.configure(bg="#f9f9f9")

# Heading
heading = tk.Label(window, text="Simple Interest Calculator", font=("Arial", 14, "bold"), bg="#f9f9f9", fg="#004466")
heading.pack(pady=10)

# Principal
tk.Label(window, text="Principal (₹):", bg="#f9f9f9").pack()
principal_entry = tk.Entry(window, width=25)
principal_entry.pack(pady=5)

# Rate of Interest
tk.Label(window, text="Rate of Interest (%):", bg="#f9f9f9").pack()
rate_entry = tk.Entry(window, width=25)
rate_entry.pack(pady=5)

# Time
tk.Label(window, text="Time (in years):", bg="#f9f9f9").pack()
time_entry = tk.Entry(window, width=25)
time_entry.pack(pady=5)

# Calculate Button
calc_button = tk.Button(window, text="Calculate", command=calculate_si,
                        bg="#007acc", fg="white", activebackground="#005f99")
calc_button.pack(pady=10)

# Result Label
result_label = tk.Label(window, text="", font=("Arial", 12), bg="#f9f9f9", fg="#333")
result_label.pack(pady=10)

# Run the application
window.mainloop()

