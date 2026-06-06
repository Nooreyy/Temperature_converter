import tkinter as tk
from tkinter import ttk, messagebox # for alerts

root = tk.Tk()

# Setting window size, color and title
root.title("Temperature Convertor")
root.geometry("500x400")
root.configure(bg="honeydew")


# Main heading
lable = tk.Label(root, bg="honeydew",fg="Dark green", text="Temperature Convertor", font=('Inter', 20, 'bold'))
lable.grid(column=0, row=0, columnspan=2, padx=80, pady=20) 

# Degree Label
degree_label = tk.Label(root, bg="honeydew", text="Degrees", font=('Inter', 10))
degree_label.grid(column=0, row=1, padx=10, pady=10, sticky="w")

    # Frame for Entry + Dropdown
input_frame = tk.Frame(root, bg="honeydew")
input_frame.grid(column=0, row=2, padx=10, pady=5, sticky="w")

        # Degree Entry inside frame
degree_entry = tk.Entry(input_frame, font=('Inter', 16), width=15)
degree_entry.pack(side="left")

    # Combobox inside frame
options = ['°C', '°F', 'K']
type_entry = ttk.Combobox(input_frame, width=5, values=options, font=('Inter', 10), state="readonly")
type_entry.set("°C")
type_entry.pack(side="left", padx=5)



# Convertion Label
convert_label = tk.Label(root, bg="honeydew", text="Convert to", font=('Inter', 10))
convert_label.grid(column=0, row=3, padx=10, pady=10, sticky="w")

    # Frame for Entry + Dropdown
input_frame2 = tk.Frame(root, bg="honeydew")
input_frame2.grid(column=0, row=4, padx=10, pady=5, sticky="w")

        # Result inside frame
display_result = tk.Entry(input_frame2, font=('Inter', 16), width=15)
display_result.pack(side="left")

    # Combobox inside frame
convert_options = ['°C', '°F', 'K']
convert_type = ttk.Combobox(input_frame2, width=5, values=options, font=('Inter', 10), state="readonly")
convert_type.set("°F")
convert_type.pack(side="left", padx=5)

#Function that contains main logic
def Convertion():
    try:
        value = float(degree_entry.get())
        selected = type_entry.get()
        select = convert_type.get()

        if selected=="°C" and select=="°F":
            result = (value * 9/5) + 32
        elif selected=="°C" and select=="K":
            result = value + 273.15
        elif selected=="°F" and select=="K":
            result = (value - 32) * 5/9 + 273.15
        elif selected=="°F" and select=="°C":
            result = (value - 32) * 5/9
        elif selected=="K" and select=="°C":
            result = value - 273.15
        elif selected=="K" and select=="°F":
            result = (value - 273.15) * 9/5 + 32

        #Show results
        display_result.config(state="normal")
        display_result.delete(0, tk.END)
        display_result.insert(0, f"{result:.2f}")
        display_result.config(state="readonly")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number!")

# Convert Button
convert_button = tk.Button(root,width=10, text="Convert", bg="Dark Green", fg="White", font=('Inter', 18), command=Convertion )
convert_button.grid(column=0, row=9, columnspan=2, pady=15)

root.mainloop()     