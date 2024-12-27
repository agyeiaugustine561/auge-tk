import tkinter as tk
from tkinter import ttk, messagebox

class PharmacyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pharmacy Management System")
        self.root.geometry("900x600")


        # Navbar
        nav_frame = tk.Frame(self.root, bg="#004c8c")
        nav_frame.pack(fill=tk.X, pady=5)
        nav_buttons = ["Dashboard", "Create Options", "Inventory", "Sales", "Accounting", "Manage Staff", "Welcome", "Logout"]
        for btn_text in nav_buttons:
            btn = tk.Button(nav_frame, text=btn_text, bg="#004c8c", fg="white", bd=0, padx=10, pady=5, cursor="hand2")
            btn.pack(side=tk.LEFT, padx=10)

        # Inventory Section
        inventory_frame = tk.Frame(self.root, bg="white", padx=20, pady=20)
        inventory_frame.pack(fill=tk.BOTH, expand=True)

        inventory_label = tk.Label(inventory_frame, text="Inventory", font=("Arial", 18), bg="white")
        inventory_label.pack(anchor=tk.W, pady=10)

        # Insert Medicine Form
        form_frame = tk.Frame(inventory_frame, bg="#e6f3ff", bd=2, relief="solid")
        form_frame.pack(fill=tk.X, padx=10, pady=10)

        form_title = tk.Label(form_frame, text="Insert Medicine Purchase Information", font=("Arial", 16), bg="#3399ff", fg="white", padx=10, pady=5)
        form_title.pack(fill=tk.X)

        fields = [
            ("Medicine Name", ["-- Select --", "Ace Plus", "Napa Extra"]),
            ("Generic", ["-- Select --", "Paracetamol"]),
            ("Presentation", ["-- Select --", "Tablet"]),
            ("Total Quantity", None),
            ("Volume (gm/ml)", None),
            ("Unit Price", None),
            ("Total Amount", None),
            ("Supplier Company", ["-- Select --", "Square Pharmaceuticals Ltd.", "Beximco Pharmaceuticals Ltd."]),
            ("Selling Price", None),
            ("Expire Date", None)
        ]

        self.entries = {}
        for label_text, options in fields:
            field_frame = tk.Frame(form_frame, bg="#e6f3ff")
            field_frame.pack(fill=tk.X, padx=10, pady=5)
            label = tk.Label(field_frame, text=label_text, bg="#e6f3ff")
            label.pack(side=tk.LEFT, padx=5)
            if options:
                self.entries[label_text] = ttk.Combobox(field_frame, values=options, state="readonly", width=30)
                self.entries[label_text].pack(side=tk.LEFT, padx=5)
            else:
                self.entries[label_text] = tk.Entry(field_frame, width=33)
                self.entries[label_text].pack(side=tk.LEFT, padx=5)

        create_button = tk.Button(form_frame, text="Create", bg="#0066cc", fg="white", padx=10, pady=5, cursor="hand2", command=self.add_record)
        create_button.pack(pady=10)

        # Medicine List (Data Table)
        table_frame = tk.Frame(inventory_frame, bg="#e6f3ff", bd=2, relief="solid")
        table_frame.pack(fill=tk.BOTH, padx=10, pady=10, expand=True)

        table_title = tk.Label(table_frame, text="Medicine List", font=("Arial", 16), bg="#3399ff", fg="white", padx=10, pady=5)
        table_title.pack(fill=tk.X)

        # Table content
        self.table_frame = tk.Frame(table_frame, bg="white")
        self.table_frame.pack(fill=tk.BOTH, expand=True)

        # Table headers
        headers = ["#", "Details", "Supplier", "Available Qty", "Unit Price", "Total Amount", "Selling Price", "Expiry", "Action"]
        for i, header in enumerate(headers):
            label = tk.Label(self.table_frame, text=header, font=("Arial", 12, "bold"), bg="#004c8c", fg="white", width=15, height=2, relief="raised")
            label.grid(row=0, column=i, sticky="nsew")

        # Configuring columns to adjust width dynamically
        for i in range(len(headers)):
            self.table_frame.grid_columnconfigure(i, weight=1)

        self.row_count = 1

    def add_record(self):
        # Check if all required fields are filled
        if not all(entry.get() for entry in self.entries.values()):
            messagebox.showwarning("Incomplete Data", "Please fill all fields before creating a record.")
            return

        # Collect data from form
        details = (
            self.entries["Medicine Name"].get(),
            self.entries["Generic"].get(),
            self.entries["Presentation"].get(),
            self.entries["Volume (gm/ml)"].get(),
        )
        new_row = [
            str(self.row_count),
            f"Medicine: {details[0]}\nGeneric: {details[1]}\nPresentation: {details[2]}\nVolume: {details[3]}",
            self.entries["Supplier Company"].get(),
            self.entries["Total Quantity"].get(),
            self.entries["Unit Price"].get(),
            self.entries["Total Amount"].get(),
            self.entries["Selling Price"].get(),
            self.entries["Expire Date"].get()
        ]

        # Insert the new row into the table
        for col, text in enumerate(new_row):
            label = tk.Label(self.table_frame, text=text, bg="#ffe6e6", width=15, height=5, relief="ridge")
            label.grid(row=self.row_count, column=col, sticky="nsew")

        # Add action buttons (edit, delete)
        action_frame = tk.Frame(self.table_frame)
        edit_btn = tk.Button(action_frame, text="Edit", command=lambda: self.edit_row(self.row_count))
        delete_btn = tk.Button(action_frame, text="Delete", command=lambda: self.delete_row(self.row_count))
        edit_btn.pack(side=tk.LEFT, padx=5)
        delete_btn.pack(side=tk.RIGHT, padx=5)
        action_frame.grid(row=self.row_count, column=8)

        # Adjust the row count
        self.row_count += 1

    def edit_row(self, row):
        # Define the functionality for editing a row
        pass

    def delete_row(self, row):
        # Define the functionality for deleting a row
        pass

# Main Tkinter loop
if __name__ == "__main__":
    root = tk.Tk()
    app = PharmacyApp(root)
    root.mainloop()
   
