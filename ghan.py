import tkinter as tk
from tkinter import ttk

def add_medicine():
    # Get form data
    medicine_name = medicine_name_var.get()
    generic = generic_var.get()
    presentation = presentation_var.get()
    quantity = quantity_var.get()
    volume = volume_var.get()
    unit_price = unit_price_var.get()
    total_amount = total_amount_var.get()
    supplier = supplier_var.get()
    selling_price = selling_price_var.get()
    expire_date = expire_date_var.get()

    # Ensure all fields are filled
    if not all([medicine_name, generic, presentation, quantity, unit_price, total_amount, supplier, selling_price, expire_date]):
        print("Please fill in all fields.")
        return

    # Add the data to the treeview (simulating the table)
    medicine_table.insert('', 'end', values=(medicine_name, generic, presentation, volume, quantity, unit_price, total_amount, supplier, selling_price, expire_date))

    # Clear form after submission
    clear_form()

def clear_form():
    # Clear all form fields
    medicine_name_var.set('')
    generic_var.set('')
    presentation_var.set('')
    quantity_var.set('')
    volume_var.set('')
    unit_price_var.set('')
    total_amount_var.set('')
    supplier_var.set('')
    selling_price_var.set('')
    expire_date_var.set('')

# Main window
root = tk.Tk()
root.title("Pharmacy Management System")
root.geometry("900x600")

# Create a canvas to hold the content and a scrollbar
canvas_frame = tk.Frame(root)
canvas_frame.pack(fill="both", expand=True)

canvas = tk.Canvas(canvas_frame)
scrollbar = tk.Scrollbar(canvas_frame, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)

scrollbar.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)

# Create a frame inside the canvas
content_frame = tk.Frame(canvas)

# Bind the canvas to update its scroll region when the frame is resized
content_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=content_frame, anchor="nw")

# Header section
header_frame = tk.Frame(content_frame, bg='#004c8c', height=60)
header_frame.pack(fill="x")

header_label = tk.Label(header_frame, text="Pharmacy Management System", fg="white", bg='#004c8c', font=("Arial", 20))
header_label.pack(pady=10)

# Navigation bar
nav_bar_frame = tk.Frame(content_frame, bg='#004c8c')
nav_bar_frame.pack(fill="x")

nav_items = ["Dashboard", "Create Options", "Inventory", "Sales", "Accounting", "Manage Staff", "Welcome", "Logout"]
for item in nav_items:
    button = tk.Button(nav_bar_frame, text=item, bg='#004c8c', fg="white", relief="flat")
    button.pack(side="left", padx=10, pady=10)

# Inventory Section
inventory_frame = tk.Frame(content_frame, bg="white", padx=10, pady=10)
inventory_frame.pack(fill="both", expand=True)

inventory_label = tk.Label(inventory_frame, text="Inventory", font=("Arial", 16), bg="white")
inventory_label.grid(row=0, column=0, sticky="w", pady=(10, 20))

# Medicine Form Section
form_frame = tk.Frame(inventory_frame, bg="#e6f3ff", bd=1, relief="solid", padx=10, pady=10)
form_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nw")

form_label = tk.Label(form_frame, text="Insert Medicine Purchase Information", bg="#3399ff", fg="white", font=("Arial", 14))
form_label.grid(row=0, column=0, columnspan=2, sticky="ew", pady=10)

# Form Fields
medicine_name_var = tk.StringVar()
generic_var = tk.StringVar()
presentation_var = tk.StringVar()
quantity_var = tk.StringVar()
volume_var = tk.StringVar()
unit_price_var = tk.StringVar()
total_amount_var = tk.StringVar()
supplier_var = tk.StringVar()
selling_price_var = tk.StringVar()
expire_date_var = tk.StringVar()

fields = [
    ("Medicine Name", medicine_name_var, ["-- Select --", "Ace Plus", "Napa Extra"]),
    ("Generic", generic_var, ["-- Select --", "Paracetamol"]),
    ("Presentation", presentation_var, ["-- Select --", "Tablet"]),
    ("Total Quantity", quantity_var, []),
    ("Volume (gm/ml)", volume_var, []),
    ("Unit Price", unit_price_var, []),
    ("Total Amount", total_amount_var, []),
    ("Supplier Company", supplier_var, ["-- Select --", "Square Pharmaceuticals Ltd.", "Beximco Pharmaceuticals Ltd."]),
    ("Selling Price", selling_price_var, []),
    ("Expire Date", expire_date_var, [])
]

for i, (label_text, var, options) in enumerate(fields):
    label = tk.Label(form_frame, text=label_text, bg="#e6f3ff")
    label.grid(row=i+1, column=0, sticky="w", pady=5)
    
    if options:
        dropdown = ttk.Combobox(form_frame, textvariable=var, values=options)
        dropdown.grid(row=i+1, column=1, pady=5, sticky="ew")
        dropdown.current(0)  # Set default to '-- Select --'
    else:
        entry = tk.Entry(form_frame, textvariable=var)
        entry.grid(row=i+1, column=1, pady=5, sticky="ew")

# Submit Button
submit_button = tk.Button(form_frame, text="Create", command=add_medicine, bg="#0066cc", fg="white", padx=10, pady=5)
submit_button.grid(row=len(fields)+1, column=0, columnspan=2, pady=10)

# Medicine List (Treeview Table)
medicine_table_frame = tk.Frame(inventory_frame, bg="#e6f3ff", bd=1, relief="solid", padx=10, pady=10)
medicine_table_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nw")

medicine_table_label = tk.Label(medicine_table_frame, text="Medicine List", bg="#3399ff", fg="white", font=("Arial", 14))
medicine_table_label.grid(row=0, column=0, sticky="ew", pady=10)

medicine_table = ttk.Treeview(medicine_table_frame, columns=("Name", "Generic", "Presentation", "Volume", "Quantity", "Unit Price", "Total Amount", "Supplier", "Selling Price", "Expire Date"), show="headings")
medicine_table.grid(row=1, column=0)

# Define Table Columns
columns = ["Name", "Generic", "Presentation", "Volume", "Quantity", "Unit Price", "Total Amount", "Supplier", "Selling Price", "Expire Date"]
for col in columns:
    medicine_table.heading(col, text=col)
    medicine_table.column(col, width=100)

# Run the application
root.mainloop()
