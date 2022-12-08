import tkinter
import os
# from tkinter.messagebox import showinfo, showerror  # Uncomment to use the messagebox module

# Global Variables
global root
global rep_text, job_name_text, directory_text

# Static Pathing Variables
parent_dir = os.getcwd()
static_dir = "static"
default_dist_dir = os.path.join(parent_dir, "dist")

# Static Variables
root_window_name = "Folder Structure Creator"
root_window_icon = os.path.join(static_dir, "favicon.ico")
root_window_bg = "#ffffff"
root_window_size = {
    "width": 450,
    "height": 500,
}
folder_name = "Folder"
mode = 0o666

# Container Objects to maintain references to all entry fields and variables.
entry_list: list[tkinter.Entry] = []  # List of Entry Objects (tkinter.Entry)
entry_var_list: list[tkinter.StringVar] = []  # List of Entry Object *variables* (tkinter.StringVar)
checkbox_list: list[tkinter.Checkbutton] = []  # List of CheckButton Objects (tkinter.Checkbutton)
checkbox_var_list: list[tkinter.IntVar] = []  # List of CheckButton Object *variables* (tkinter.IntVar)


# Root Window Configuration
def root_window_init():
    print("Initializing root window...")
    global root
    root = tkinter.Tk()
    root.title(root_window_name)
    root.iconbitmap(root_window_icon)
    root.geometry(f"{root_window_size.get('width')}"
                  f"x{root_window_size.get('height')}")
    root.configure(bg=root_window_bg)
    print("Root window initialized.")


# Create Window Layout
def content_init():
    print("Initializing content...")
    global root
    global rep_text, job_name_text, directory_text

    # Assign Entry text variables
    rep_text = tkinter.StringVar()
    job_name_text = tkinter.StringVar()
    directory_text = tkinter.StringVar()

    # Initialize Text Boxes
    text_boxes_init()
    # Initialize Check Boxes
    check_boxes_init()
    # Initialize Buttons
    buttons_init()

    print("Content initialized.")


# Initialize Text Box Entries
def text_boxes_init():
    print("Initializing text boxes...")
    global root
    global rep_text, job_name_text, directory_text
    global entry_list

    # First empty the lists to store all entry fields and variables for clearing later.
    entry_list.clear()
    entry_var_list.clear()

    # Rep Entry
    rep_label = tkinter.Label(root, text="Rep:", bg="#FFFFFF", fg="#000000")
    rep_label.grid(row=0, column=0, sticky="W")
    rep_entry = tkinter.Entry(root, textvariable=rep_text, width=50, name="rep")
    rep_entry.grid(row=0, column=1, sticky="W")
    # Add to list
    entry_list.append(rep_entry)
    entry_var_list.append(rep_text)

    # Job Name Entry
    job_name_label = tkinter.Label(root, text="Job Name:", bg="#FFFFFF", fg="#000000")
    job_name_label.grid(row=1, column=0, sticky="W")
    job_name_entry = tkinter.Entry(root, textvariable=job_name_text, width=50, name="job_name")
    job_name_entry.grid(row=1, column=1, sticky="W")
    # Add to list
    entry_list.append(job_name_entry)
    entry_var_list.append(job_name_text)

    # Directory Entry
    directory_label = tkinter.Label(root, text="Directory:", bg="#FFFFFF", fg="#000000")
    directory_label.grid(row=2, column=0, sticky="W")
    directory_entry = tkinter.Entry(root, textvariable=directory_text, width=50, name="directory")
    directory_entry.grid(row=2, column=1, sticky="W")
    # Add to list
    entry_list.append(directory_entry)
    entry_var_list.append(directory_text)

    print("Text boxes initialized.", f"{entry_list.__len__()} entries added to stack.")


# Initialize Checkboxes
def check_boxes_init():
    print("Initializing check boxes...")
    global root
    global checkbox_list

    # First empty the lists to store all checkbox fields and variables for clearing later.
    checkbox_list.clear()
    checkbox_var_list.clear()

    pre_prod_checked = tkinter.IntVar()
    prod_checked = tkinter.IntVar()

    pre_prod_btn = tkinter.Checkbutton(root, text="PreProduction", variable=pre_prod_checked, onvalue=1, offvalue=0)
    pre_prod_btn.grid(row=4, column=1)
    pre_prod_btn.select()
    checkbox_list.append(pre_prod_btn)
    checkbox_var_list.append(pre_prod_checked)

    prod_btn = tkinter.Checkbutton(root, text="Production", variable=prod_checked, onvalue=1, offvalue=0)
    prod_btn.grid(row=5, column=1)
    prod_btn.select()
    checkbox_list.append(prod_btn)
    checkbox_var_list.append(prod_checked)

    print("Check boxes initialized.", f"{checkbox_list.__len__()} checkboxes added to stack.")


# Initialize Buttons
def buttons_init():
    print("Initializing buttons...")
    global root

    # Submit Button
    submit_btn = tkinter.Button(root, text="Submit", command=submit)
    submit_btn.grid(row=6, column=1, columnspan=2, pady=10, padx=10, ipadx=100)


# Create Directories
def create_directories():
    # Dynamically build and retrieve the path using our construct_path function
    path = construct_path()

    if os.path.exists(path):
        # showwarning("Error", "Directory already exists.") # Show error message
        print(f"Directory already exists: {path}")
    else:
        try:  # Try to create the directory
            os.makedirs(path, mode)
        except OSError as e:  # If the directory cannot be created
            print(f"Creation of the directory {path} failed.\n strerror: {e.strerror}")
            # showerror("Error", f"Creation of the directory {path} failed.\n{e.strerror}") # Show error message
        else:  # If the directory is successfully created, we can now clean up/exit/proceed
            # Reset the various UI elements from their containers.
            reset_ui_elements()
            print(f"Successfully created the directory {path}.")
            # showinfo("Success", "Directory created.") # Show success message


def construct_path():
    global rep_text, job_name_text, directory_text
    # Can now use the 3 variables above to construct the path. 'global' tells the function to use the global variables.
    # e.g. path = os.path.join(parent_dir, rep_text, job_name_text, directory_text)
    # yields the following path: "C:\Users\user\PycharmProjects\folder_structure_creator\rep\job_name\directory"
    # e.g. path = os.path.join(parent_dir, child_dir, child_dir2, ... n) where n is the number of child directories
    path = os.path.join(default_dist_dir, folder_name, rep_text.get(), job_name_text.get(),
                        directory_text.get())  # path: 'parent_dir/default_dist_dir/folder_name'
    print(f"Path: {path}")
    return path  # Return the resulting path string to the caller function


# On Submit Button Click
def submit():
    print("Submit button pressed.")
    create_directories()


def reset_ui_elements():
    print("Resetting UI elements...")
    global entry_list, entry_var_list, checkbox_list, checkbox_var_list

    # Merge the lists together to iterate through them in a single loop. [(entry, entry_var), (checkbox, checkbox_var)]
    entries = list(zip(entry_list, entry_var_list))
    checkboxes = list(zip(checkbox_list, checkbox_var_list))
    # Clear all entries
    clear_entries(entries)
    # Clear all checkboxes
    clear_check_boxes(checkboxes)
    print("UI elements reset.")


# Reset Entry Inputs
def clear_entries(entries):
    # Clear all fields
    print("Clearing entries...")
    # if length of the entries array is greater than 0 (entry/variable tuples are present), clear all entries.
    if len(entries) > 0:  # If the entries array is not empty
        for entry, entry_var in entries:  # Iterate through the entries array
            entry_var.set("")  # Clear the entry variable
            entry.delete(0, tkinter.END)  # Clear the entry field
    else:
        print("No entries to clear.")
        return
    entries.clear()  # Clear the entries array
    print("Entries cleared.")


# Reset Checkbox Inputs
def clear_check_boxes(checkboxes):
    # Clear all fields
    print("Clearing checkboxes...")
    # if length of the checkboxes array is greater than 0 (checkbox/variable tuples are present), clear all checkboxes.
    if len(checkboxes) > 0:  # If the checkboxes array is not empty
        for checkbox, checkbox_var in checkboxes:  # Iterate through the checkboxes array
            checkbox_var.set(0)  # Clear the checkbox variable
            checkbox.deselect()  # Clear the checkbox field
            print(f"Cleared {checkbox.widgetName} checkbox.")
    else:
        print("No checkboxes to clear.")
        return
    checkboxes.clear()  # Clear the checkboxes array
    print("Checkboxes cleared.")

# # # # # # # # # # # # # # # #
#  .     ,-'""`-.             #
# (,-.`._,'(       |\`-/|     #
#     `-.-' \ )-`( , o o)     #
#           `-    \`_`"'-     #
# # # # # # # # # # # # # # # #


# Main Function Call (Entry Point)
if __name__ == '__main__':  # If this file is the main file being executed
    global root  # Make the root variable global, so it can be accessed by other functions.
    root_window_init()  # Initialize the root window
    content_init()  # Initialize the content
    root.mainloop()  # Start the main loop
