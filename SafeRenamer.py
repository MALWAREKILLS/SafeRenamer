import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import webbrowser
from collections import Counter

# List of restricted directories
RESTRICTED_DIRECTORIES = [
    "C:\\Windows",
    "C:\\Windows\\System32",
    "C:\\Program Files",
    "C:\\Program Files (x86)",
    "C:\\Users\\Default",
    "C:\\Users\\Public"
]

def is_restricted_directory(directory):
    """Check if the selected directory is restricted."""
    return any(os.path.commonpath([directory, restricted]) == restricted for restricted in RESTRICTED_DIRECTORIES)

def rename_files_and_folders(target_path, word_to_remove, output_text, replacement_word=None):
    """Rename files and folders by removing or replacing the specified word."""
    if not os.path.exists(target_path):
        output_text.insert(tk.END, f"❌ Target path does not exist: {target_path}\n")
        return

    files_renamed = 0
    folders_renamed = 0

    for root, dirs, files in os.walk(target_path, topdown=False):
        for name in files:
            new_name = name.replace(word_to_remove, replacement_word if replacement_word else "")
            if new_name != name:
                old_path = os.path.join(root, name)
                new_path = os.path.join(root, new_name)
                os.rename(old_path, new_path)
                output_text.insert(tk.END, f"✅ Renamed file: {old_path} -> {new_path}\n")
                files_renamed += 1
        for name in dirs:
            new_name = name.replace(word_to_remove, replacement_word if replacement_word else "")
            if new_name != name:
                old_path = os.path.join(root, name)
                new_path = os.path.join(root, new_name)
                os.rename(old_path, new_path)
                output_text.insert(tk.END, f"✅ Renamed folder: {old_path} -> {new_path}\n")
                folders_renamed += 1

    output_text.insert(tk.END, "\n Renaming Summary \n")
    output_text.insert(tk.END, f"Total files renamed: {files_renamed}\n")
    output_text.insert(tk.END, f"Total folders renamed: {folders_renamed}\n")
    output_text.insert(tk.END, f"Renaming completed for target: {target_path}\n")

def browse_directory(entry):
    """Browse and select a directory, then analyze its contents."""
    directory = filedialog.askdirectory()
    if directory:
        if is_restricted_directory(directory):
            messagebox.showerror("Error", "You cannot select a restricted system directory!")
            return

        # Count the number of files and their types in the selected directory
        file_types = Counter()
        total_files = 0

        for root, _, files in os.walk(directory):
            for file in files:
                total_files += 1
                file_extension = os.path.splitext(file)[1] or "No Extension"
                file_types[file_extension] += 1

        # Display the information in a message box
        file_types_summary = "\n".join([f"{ext}: {count}" for ext, count in file_types.items()])
        messagebox.showinfo(
            "Folder Analysis",
            f"Total files: {total_files}\n\nFile types:\n{file_types_summary}"
        )

        # Update the entry field with the selected directory
        entry.delete(0, tk.END)
        entry.insert(0, directory)

def start_renaming(word_entry, path_entry, output_text, replacement_entry, replace_var):
    """Start the renaming process."""
    word_to_remove = word_entry.get()
    target_path = path_entry.get()
    replacement_word = replacement_entry.get() if replace_var.get() else None

    if not word_to_remove or not target_path:
        messagebox.showerror("Error", "Both fields must be filled!")
        return
    if is_restricted_directory(target_path):
        messagebox.showerror("Error", "You cannot select a restricted system directory!")
        return
    output_text.delete(1.0, tk.END)
    rename_files_and_folders(target_path, word_to_remove, output_text, replacement_word)

def open_telegram():
    """Open the Telegram link in the default web browser."""
    webbrowser.open("https://t.me/malwaredot")

# Create the main window
root = tk.Tk()
root.title("Safe Renamer")
root.geometry("800x600")
root.resizable(False, False)  # Disable window resizing

# Create a frame for the banner
banner_frame = tk.Frame(root, height=150, bg="black")
banner_frame.pack(fill=tk.X)

# Add the banner text
banner_label = tk.Label(
    banner_frame,
    text="""
███╗   ███╗ █████╗ ██╗     ██╗    ██╗ █████╗ ██████╗ ███████╗██████╗  ██████╗ ████████╗
████╗ ████║██╔══██╗██║     ██║    ██║██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔═══██╗╚══██╔══╝
██╔████╔██║███████║██║     ██║ █╗ ██║███████║██████╔╝█████╗  ██║  ██║██║   ██║   ██║   
██║╚██╔╝██║██╔══██║██║     ██║███╗██║██╔══██║██╔══██╗██╔══╝  ██║  ██║██║   ██║   ██║   
██║ ╚═╝ ██║██║  ██║███████╗╚███╔███╔╝██║  ██║██║  ██║███████╗██████╔╝╚██████╔╝   ██║   
╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝ ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═════╝  ╚═════╝    ╚═╝
""",
    bg="black",
    fg="magenta",
    font=("Courier", 10),
    justify=tk.LEFT
)
banner_label.pack(pady=10)

# Create a frame for the Telegram button under the banner
telegram_frame = tk.Frame(root)
telegram_frame.pack(pady=10)

# Add the Telegram button
telegram_button = ttk.Button(telegram_frame, text="Contact", command=open_telegram)
telegram_button.pack(pady=5)

# Create a frame for the input fields and buttons
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

# Word to remove
tk.Label(input_frame, text="Word to Remove:", font=("Arial", 10, "bold")).grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
word_entry = ttk.Entry(input_frame, width=50)
word_entry.grid(row=0, column=1, padx=5, pady=5)

# Target directory
tk.Label(input_frame, text="Target Directory:", font=("Arial", 10, "bold")).grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
path_entry = ttk.Entry(input_frame, width=50)
path_entry.grid(row=1, column=1, padx=5, pady=5)
browse_button = ttk.Button(input_frame, text="Browse", command=lambda: browse_directory(path_entry))
browse_button.grid(row=1, column=2, padx=5, pady=5)

# Checkbox for replacement word
replace_var = tk.BooleanVar()
replace_checkbox = ttk.Checkbutton(input_frame, text="Replace with:", variable=replace_var)
replace_checkbox.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)

# Replacement word entry
replacement_entry = ttk.Entry(input_frame, width=50, state="disabled")
replacement_entry.grid(row=2, column=1, padx=5, pady=5)

# Enable/disable replacement entry based on checkbox
def toggle_replacement_entry():
    if replace_var.get():
        replacement_entry.config(state="normal")
    else:
        replacement_entry.delete(0, tk.END)
        replacement_entry.config(state="disabled")

replace_var.trace("w", lambda *args: toggle_replacement_entry())

# Start button
start_button = ttk.Button(root, text="Start Renaming", command=lambda: start_renaming(word_entry, path_entry, output_text, replacement_entry, replace_var))
start_button.pack(pady=10)

# Output text area
output_frame = tk.Frame(root)
output_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
output_text = tk.Text(output_frame, wrap=tk.WORD, height=20, bg="black", fg="white", font=("Courier", 10))
output_text.pack(fill=tk.BOTH, expand=True)

# Run the application
root.mainloop()