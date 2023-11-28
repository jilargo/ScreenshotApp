from home import ttk
from home import tk
from home import DateEntry

def create_labeled_entry(parent, label_text, row, label_bg, entry_bg,entry_width=30,label_width=50):
    # Create the label with the specified background color
    label = tk.Label(parent, text=label_text, bg=label_bg, anchor="w",width=label_width)
    label.grid(row=row, column=0, sticky="ew")

    # Create the entry with the specified background color
    entry = ttk.Entry(parent,width=entry_width)
    entry.grid(row=row, column=1, sticky="ew", padx=(0, 10))

    # Set the background color for the entry widget
    entry.config(background=entry_bg)

    return entry

def create_header_label(parent, text, row, column, bg_color, columnspan=1):
    header_label = tk.Label(parent, text=text, bg=bg_color, anchor='center')
    header_label.grid(row=row, column=column, columnspan=columnspan, sticky='ew')
    
def create_entry_row(parent, num_entries, row, column, columnspan=1):
    entries = []
    for i in range(num_entries):
        entry = ttk.Entry(parent)
        entry.grid(row=row, column=column + i, columnspan=columnspan, sticky='ew', padx=5, pady=5)
        entries.append(entry)
    return entries 

# Create header labels for form 3
def create_labeled_date_entry(parent, label_text, row, label_bg, entry_bg, entry_width=30):
    # Create the label with the specified background color
    label = tk.Label(parent, text=label_text, bg=label_bg, anchor="w")
    label.grid(row=row, column=0, sticky="ew")

    # Create the DateEntry with the specified background color
    date_entry = DateEntry(parent, width=entry_width, background=entry_bg, foreground='black', borderwidth=2)
    date_entry.grid(row=row, column=1, sticky="ew", padx=(0, 10))

    return date_entry


def reconsigned_combobox(parent, label_text, row, label_bg, entry_bg, values):
    # Create the label with the specified background color
    label = tk.Label(parent, text=label_text, bg=label_bg, anchor="w")
    label.grid(row=row, column=0, sticky="ew")

    # Create the combo box with the specified background color and values
    combo = ttk.Combobox(parent, values=values)
    combo.grid(row=row, column=1, sticky="ew", padx=(0, 10))

    # Set the background color for the combobox widget
    combo.config(background=entry_bg)

    return combo

#Project/Security/Manager combo box

def projectSecurity_combobox(parent, label_text, row, label_bg, entry_bg, values, entry_width=30):
    # Create the label with the specified background color
    label = tk.Label(parent, text=label_text, bg=label_bg, anchor="w")
    label.grid(row=row, column=0, sticky="ew")

    # Create the combo box with the specified background color and values
    combo = ttk.Combobox(parent, values=values, width=entry_width)
    combo.grid(row=row, column=1, sticky="ew", padx=(0, 10))

    # Set the background color for the combobox widget
    combo.config(background=entry_bg)

    return combo

def ITPN_Reason_combobox(parent, label_text, row, label_bg, entry_bg, values):
    # Create the label with the specified background color
    label = tk.Label(parent, text=label_text, bg=label_bg, anchor="w")
    label.grid(row=row, column=0, sticky="ew")

    # Create the combo box with the specified background color and values
    combo = ttk.Combobox(parent, values=values)
    combo.grid(row=row, column=1, sticky="ew", padx=(0, 10))

    # Set the background color for the combobox widget
    combo.config(background=entry_bg)

    return combo

def ReasonForNG_combobox(parent, label_text, row, label_bg, entry_bg, values):
    # Create the label with the specified background color
    label = tk.Label(parent, text=label_text, bg=label_bg, anchor="w")
    label.grid(row=row, column=0, sticky="ew")

    # Create the combo box with the specified background color and values
    combo = ttk.Combobox(parent, values=values)
    combo.grid(row=row, column=1, sticky="ew", padx=(0, 10))

    # Set the background color for the combobox widget
    combo.config(background=entry_bg)

    return combo