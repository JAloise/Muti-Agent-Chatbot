from pathlib import Path
import os



DIRECTORY_PATH = str(Path.cwd())

# =================== data format ======================
# *collection name *data location * embedded data location
EMPTY_DATA = [] # used for models with no extra path
# concordia
CONCORDIA_PATH = DIRECTORY_PATH + r"\data\concordia\\"
CONCORDIA_DATA = ["concordia",CONCORDIA_PATH,CONCORDIA_PATH+r"db\\" ]
if os.system == "Darwin" or os.system == "Linux":
    CONCORDIA_PATH = DIRECTORY_PATH + r"/data/concordia//"
    CONCORDIA_DATA = ["concordia", CONCORDIA_PATH, CONCORDIA_PATH + r"db//"]


