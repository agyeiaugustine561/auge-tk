import tkinter as tk
from tkinter import ttk

class PharmacyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Pharmacy Management System")
        self.geometry("900x700")
        self.configure(bg="#f2f2f2")
        
        # Header Section
        self.create_header()
        
        # Inventory Section
        self.create_inventory_section()
        
        # Footer Section
        self.create_footer()

    def create_header(self):
        header_frame = tk.Frame(self, bg="#004c8c", bd=2, relief="raised", pady=10)
        header_frame.pack(fill="x")
        
        title_label = tk.Label(header_frame, text="Pharmacy Management System", font=("Arial", 24), bg="#004c8c", fg="white")
        title_label.pack()
        
        nav_bar = tk.Frame(header_frame, bg="#004c8c")
        nav_bar.pack()
        
        # Navigation Buttons
        nav_items = ["Dashboard", "Create Options", "Inventory", "Sales", "Accounting", "Manage Staff", "Welcome", "Logout"]
        for item in nav_items:
            nav_button = tk.Button(nav_bar, text=item, bg="#004c8c", fg="white", bd=0, font=("Arial", 10), padx=10)
            nav_button.pack(side="left")

    def create_inventory_section(self):
        inventory_frame = tk.Frame(self, bg="white", pady=20)
        inventory_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # Inventory Label
        inventory_label = tk.Label(inventory_frame, text="Inventory", font=("Arial", 18), bg="white", fg="black")
        inventory_label.pack(anchor="w")

        # Medicine Form Section
        form_frame = tk.Frame(inventory_frame, bg="#e6f3ff", padx=10, pady=10, relief="groove", bd=2)
        form_frame.pack(fill="x", pady=10)

        form_title = tk.Label(form_frame, text="Insert Medicine Purchase Information", bg="#3399ff", fg="white", font=("Arial", 14), anchor="w", padx=5)
        form_title.pack(fill="x")

        self.create_form(form_frame)

        # Medicine List Section
        list_frame = tk.Frame(inventory_frame, bg="#e6f3ff", padx=10, pady=10, relief="groove", bd=2)
        list_frame.pack(fill="x", pady=10)

        list_title = tk.Label(list_frame, text="Medicine List", bg="#3399ff", fg="white", font=("Arial", 14), anchor="w", padx=5)
        list_title.pack(fill="x")
        
        self.create_table(list_frame)

    def create_form(self, parent_frame):
        form_fields = [
            ("Medicine Name", "Select"),
            ("Generic", "Select"),
            ("Presentation", "Select"),
            ("Total Quantity", "Input"),
            ("Volume (gm/ml)", "Input"),
            ("Unit Price", "Input"),
            ("Purchase Paid", "Input"),
            ("Total Amount", "Input"),
            ("Supplier Company", "Select"),
            ("Selling Price", "Input"),
            ("Expire Date", "Input")
        ]

        for index, (label_text, input_type) in enumerate(form_fields):
            row_frame = tk.Frame(parent_frame, bg="#e6f3ff")
            row_frame.pack(fill="x", pady=5)

            label = tk.Label(row_frame, text=label_text, bg="#e6f3ff", anchor="w")
            label.pack(side="left", padx=5, pady=5)

            if input_type == "Select":
                entry = ttk.Combobox(row_frame)
                entry['values'] = ['-- Select --']
                entry.current(0)
            else:
                entry = tk.Entry(row_frame)
            
            entry.pack(side="right", fill="x", padx=10)

        submit_button = tk.Button(parent_frame, text="Create", bg="#0066cc", fg="white", padx=20, pady=5)
        submit_button.pack(pady=10)

    def create_table(self, parent_frame):
        table = ttk.Treeview(parent_frame, columns=('Details', 'Supplier', 'Qty', 'Unit Price', 'Total Amount', 'Selling Price', 'Paid', 'Due', 'Expiry', 'Action'), show='headings')
        
        headers = ['Details', 'Supplier', 'Qty', 'Unit Price', 'Total Amount', 'Selling Price', 'Paid', 'Due', 'Expiry', 'Action']
        
        # Set column headings
        for col in headers:
            table.heading(col, text=col)
            table.column(col, anchor="center", width=80)
        
        # Sample Data
        sample_data = [
            ("Ace Plus", "Square Pharmaceuticals Ltd.", "190", "$2.52", "$504", "$3", "$350", "$154", "2021-01-01", "Edit | Delete"),
            ("Napa Extra", "Beximco Pharmaceuticals Ltd.", "170", "$2.50", "$500", "$3", "$300", "$200", "2020-01-01", "Edit | Delete")
        ]
        
        # Insert Sample Data
        for item in sample_data:
            table.insert("", "end", values=item)
        
        table.pack(fill="x")

    def create_footer(self):
        footer_frame = tk.Frame(self, bg="#3399ff", pady=10)
        footer_frame.pack(fill="x", side="bottom")

        footer_label = tk.Label(footer_frame, text="© CI Pharmacy Sales and Inventory System, 2022", bg="#3399ff", fg="white")
        footer_label.pack()

if __name__ == "__main__":
    app = PharmacyApp()
    app.mainloop()
