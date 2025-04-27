import subprocess

def select_file_via_explorer(filetypes="All files (*.*)|*.*"):
    # Use PowerShell to open a file dialog
    command = [
        "powershell",
        "-NoProfile",
        "-Command",
        f"[System.Reflection.Assembly]::LoadWithPartialName('System.windows.forms') | Out-Null;"
        f"$ofd = New-Object System.Windows.Forms.OpenFileDialog;"
        f"$ofd.Filter = '{filetypes}';"
        f"if ($ofd.ShowDialog() -eq 'OK') {{ Write-Output $ofd.FileName }}"
    ]

    result = subprocess.run(command, capture_output=True, text=True)
    selected_file = result.stdout.strip()

    if selected_file:
        return selected_file
    else:
        return None

# Example usage: limit to text files
# file_path = select_file_via_explorer("Text files (*.pdf)|*.pdf")
# if file_path:
#     print("Selected file:", file_path)
# else:
#     print("No file selected.")