from pathlib import Path
import os


project_name = 'California_House_Price_Prediction'

list_of_items = [
    'notebook/1.EDA.ipynb',
    'notebook/2.MODEL_TRAINER.ipynb',
    'setup.py',
    'requirements.txt',
    'app.py', 
    'src/__init__.py',
    'src/exception.py',
    'src/logger.py',
    'src/utils.py',
    'src/components/__init__.py',
    'src/components/data_ingestion.py',
    'src/components/data_transformation.py',
    'src/components/model_trainer.py',
]

for file in list_of_items:
    file = Path(file)
    file_dir, file_name = os.path.split(file)

    if file_dir != '':
        os.makedirs(file_dir, exist_ok=True)

    if (not os.path.exists(file)) or (not os.path.getsize(file)):
        with open(file, 'w') as file_obj:
            pass
    else:
        print('File already exits.')
    