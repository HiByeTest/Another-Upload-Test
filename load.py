import json
import os

from PyQt6.QtWidgets import QFileDialog

import shared

def open_file(main_window):
    file_path,_ = QFileDialog.getOpenFileName(
        main_window,
        "Open File",
        f"{os.getcwd()}",
        "(*.json)",
        )
    if file_path:
        with open(file_path, encoding='utf-8') as f:      
            try:
                shared.json_file = json.load(f)
            except:
                raise json.JSONDecodeError("The selected file was not not a valid JSON document.")
    else:
        raise FileNotFoundError("The specified file was not found.")