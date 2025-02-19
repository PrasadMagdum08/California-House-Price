from pathlib import Path
import os

project_name = "California-House-Price"

list_of_items = [
    f'{project_name}/requirements.txt',
    f'{project_name}/setup.py',
    f'{project_name}/.env',
]

for file_path in list_of_items:

    file_path = Path(file_path)
    file_dir, file_name = os.path.split(file_path)

    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)

    if (not os.path.exists(file_path)) or (not os.path.getsize(file_path)):
        with open(file_path, 'w') as f:
            pass
    else:
        print('File already exits.')