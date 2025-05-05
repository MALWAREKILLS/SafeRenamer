# Safe Renamer

**Safe Renamer** is a user-friendly GUI tool for batch renaming files and folders. It allows you to remove or replace specific words in file and folder names while ensuring the safety of your system by restricting access to sensitive directories.

---

## Features

- **Batch Renaming**: Rename multiple files and folders in a selected directory.
- **Word Removal or Replacement**: Remove a specific word or replace it with another word.
- **Folder Analysis**: Analyze the selected folder to display the total number of files and their types before renaming.
- **Restricted Directories**: Prevents renaming in sensitive system directories like `C:\Windows` or `C:\Program Files`.
- **Customizable GUI**: Modern and intuitive interface built with `tkinter`.
- **Developer Contact**: Includes a button to contact the developers on Telegram.

---

## How to Use

1. **Select a Target Directory**:
   - Click the "Browse" button to choose the folder containing the files and folders you want to rename.
   - A popup will display the total number of files and their types in the selected folder.

2. **Specify the Word to Remove**:
   - Enter the word you want to remove from file and folder names.

3. **Optional: Replace the Word**:
   - Check the "Replace with" checkbox to enable the replacement feature.
   - Enter the word you want to replace the targeted word with.

4. **Start Renaming**:
   - Click the "Start Renaming" button to begin the renaming process.
   - The output log will display the renaming progress and a summary of the changes.

---

## Screenshots

### Main Interface
![Main Interface](https://i.imgur.com/pG8Twpz.png)

### Folder Analysis
![Folder Analysis](https://i.imgur.com/MG3g3DW.png)

---

## Installation
Windows: https://github.com/MALWAREKILLS/SafeRenamer/releases/tag/Release

### Prerequisites
- Python 3.7 or higher
- Required libraries: `tkinter`, `webbrowser`, `collections`

### Usage
 Clone the repository:
   ```bash
   git clone https://github.com/MALWAREKILLS/safe-renamer.git
   cd safe-renamer
   python3 SafeRenamer.py
