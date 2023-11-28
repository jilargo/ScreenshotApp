import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

# Initialize the main window
root = tk.Tk()
root.title("Security Tool")
root.geometry("1020x650")  # Set the initial size of the window

# Create a main frame inside the root window to hold everything
main_frame = ttk.Frame(root)
main_frame.pack(fill='both', expand=True)

# Create a canvas inside the main frame
canvas = tk.Canvas(main_frame)
canvas.pack(side='left', fill='both', expand=True)

# Add a scrollbar to the canvas
scrollbar = ttk.Scrollbar(main_frame, orient='vertical', command=canvas.yview)
scrollbar.pack(side='right', fill='y')

# Configure the canvas
canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# Create a frame to hold the widgets that will be scrolled
scrollable_frame = ttk.Frame(canvas)

# Add the scrollable frame to a window in the canvas
canvas.create_window((0, 0), window=scrollable_frame, anchor='nw')
# Define colors
label_bg = '#ffff99'  # Yellow background for labels
entry_bg = '#ffffff'  # White background for entries

#buttons
style = ttk.Style()



# Function to create a labeled entry with alternating colors
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

# Create the first frame and align it to the top left
form_frame = ttk.Frame(scrollable_frame, padding="3")
form_frame.pack(side='top', padx=10, pady=10, fill='x', expand=False, anchor='n')

# Create the second frame and align it to the top left, next to the first frame
form_frame2 = ttk.Frame(scrollable_frame, padding="3")
form_frame2.pack(side='top', padx=10, pady=10, fill='x', expand=False, anchor='n')

#create the third frame
form_frame3 = ttk.Frame(scrollable_frame, padding="3")
form_frame3.pack(side='top', padx=10, pady=10, fill='x', expand=False, anchor='n')


# Create the fourth frame for project-related information
form_frame4 = ttk.Frame(scrollable_frame, padding="3")
form_frame4.pack(side='top', padx=10, pady=10, fill='x', expand=False)

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


frame1_labels = [
    "Last name, First name:",
    "Manager:",
    "Location:",
    "Equipment Management # (1-4 digit):",
    "Computer/Host name:",
    "OS:"
]
#frame2 labels
frame2_labels = [
    "Reconsignment *1",
    "Project/Security Manager *2:",
    "Employment Period (start date):",
    "Employment Period (end date):",  # Make sure there's a comma here
    "Date of submitting Pledge:",
    "Completion date of education for information security:"
]
#frame3 labels
frame3_labels = [
    "Date of return, disposal or deletion(For Resignee):",
    "Reason why ITPN is not installed: ",
    "The Reason for NG:",
    "Reason for not answering the self check:",  # Make sure there's a comma here
    "Email Address:",
    "Telework Period:"
]



#frame1 entries displayed
for idx, label_text in enumerate(frame1_labels):
    create_labeled_entry(form_frame, label_text, idx, label_bg, entry_bg)






#combo box for Reconsigned
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


# Add labeled entries and a combo box to the second frame
for idx, label_text in enumerate(frame2_labels):
    if label_text == "Reconsignment *1":
        reconsigned_combobox(form_frame2, label_text, idx, label_bg, entry_bg, values=["R","-"])
    elif label_text == "Project/Security Manager *2:":
        projectSecurity_combobox(form_frame2, label_text, idx, label_bg, entry_bg, values=["P", "S","P/S","-"])
    
    elif label_text == "Employment Period (start date):":
        create_labeled_date_entry(form_frame2, "Employment Period (start date):", 2, label_bg, entry_bg)
    elif label_text == "Employment Period (end date):":
        create_labeled_date_entry(form_frame2, "Employment Period (end date):", 3, label_bg, entry_bg)
    elif label_text == "Date of submitting Pledge:":
        create_labeled_date_entry(form_frame2, "Date of submitting Pledge:", 4, label_bg, entry_bg)
    elif label_text == "Completion date of education for information security:":
        create_labeled_date_entry(form_frame2, "Completion date of education for information security:", 5, label_bg, entry_bg)
    else:
        create_labeled_entry(form_frame2, label_text, idx, label_bg, entry_bg)


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

for idx, label_text in enumerate(frame3_labels):
    if label_text == "Date of return, disposal or deletion(For Resignee):":
        create_labeled_date_entry(form_frame3, label_text, idx, label_bg, entry_bg)
    elif label_text == "Reason why ITPN is not installed: ":
        ITPN_Reason_combobox(form_frame3, label_text, idx, label_bg, entry_bg, values=["a. Using other tool (ITPN of other company)","b. OS is not supported by ITPN","c.impossible to introduce (rules of the PJ / customer policy)","d. local LAN(cannot connect the PC with JF/WAN/Mobile-FNET/interet)","e. Unused (not yet recieved/setting up/out of order and so on)","f. in process (idle,scrap,transfer(include schedule))","g. several reasons as shown above"])
    elif label_text == "The Reason for NG:":
        ReasonForNG_combobox(form_frame3, label_text, idx, label_bg, entry_bg, values=["a. Unused", "b. Confirm prior to next use","c. No target items","d. Cannot confirm","e. Several reasons as shown from above"])
    else:
        create_labeled_entry(form_frame3, label_text, idx, label_bg, entry_bg)









form_frame.columnconfigure(0, weight=1)
form_frame.columnconfigure(1, weight=1)


form_frame2.columnconfigure(0, weight=1)
form_frame2.columnconfigure(1, weight=1)


form_frame3.columnconfigure(0, weight=1)
form_frame3.columnconfigure(1, weight=1)

#last Part

# Create the bottom frame for the new layout
bottom_frame = ttk.Frame(scrollable_frame, padding="3")
bottom_frame.pack(side='top', padx=10, pady=10, fill='x', expand=False)

# Create the labels, entries, and buttons
label1 = tk.Label(bottom_frame, text="Upload Bios Password Image", anchor="w")
entry1 = ttk.Entry(bottom_frame)
button1 = ttk.Button(bottom_frame, text="Upload")

label2 = tk.Label(bottom_frame, text="Select Tree Path Folder", anchor="w")
entry2 = ttk.Entry(bottom_frame)
button2 = ttk.Button(bottom_frame, text="Select Folder")

button3 = tk.Button(bottom_frame, text="Run tool", bg='green', fg='white')  # bg for background, fg for foreground (text)

# Grid configuration for the bottom frame
label1.grid(row=0, column=0, sticky="ew")
entry1.grid(row=0, column=1, sticky="ew")
button1.grid(row=0, column=2)

label2.grid(row=1, column=0, sticky="ew")
entry2.grid(row=1, column=1, sticky="ew")
button2.grid(row=1, column=2)

button3.grid(row=0, column=3, rowspan=2, sticky="ns")

# Configure the columns within the bottom frame to distribute space
bottom_frame.columnconfigure(0, weight=1)
bottom_frame.columnconfigure(1, weight=3) # give more weight to entry
bottom_frame.columnconfigure(2, weight=1)
bottom_frame.columnconfigure(3, weight=1)

# Run the main loop
root.mainloop()




