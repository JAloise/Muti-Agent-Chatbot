from pathlib import Path
import os


#Base Directory
DIRECTORY_PATH = Path.cwd()

# =================== data format ======================
# *collection name *data location * embedded data location * data type
EMPTY_DATA = [] # used for models with no extra path

# concordia
CONCORDIA_PATH = DIRECTORY_PATH/"data"/"concordia"
CONCORDIA_DATA = ["concordia",str(CONCORDIA_PATH), str(CONCORDIA_PATH / "db"), "pdf"]
#CONCORDIA_PATH = DIRECTORY_PATH + r"\data\concordia\\"
#CONCORDIA_DATA = ["concordia",CONCORDIA_PATH,CONCORDIA_PATH+r"db\\","pdf" ]


# controller
CONTROLLER_PATH = DIRECTORY_PATH / "data" / "controller"
CONTROLLER_DATA = ["controller", str(CONTROLLER_PATH), str(CONTROLLER_PATH / "db"), "csv"]
#CONTROLLER_PATH = DIRECTORY_PATH + data_path#r"\data\controller\\"
#CONTROLLER_DATA = ["controller",CONTROLLER_PATH,CONTROLLER_PATH+r"db\\","csv" ]
if os.system == "Darwin" or os.system == "Linux":
    # concordia
    CONCORDIA_PATH = DIRECTORY_PATH + r"/data/concordia//"
    CONCORDIA_DATA = ["concordia", CONCORDIA_PATH, CONCORDIA_PATH + r"db//","pdf"]
    # controller
    CONTROLLER_PATH = DIRECTORY_PATH + r"/data/controller//"
    CONTROLLER_DATA = ["controller", CONTROLLER_PATH, CONTROLLER_PATH + r"db//", "csv"]


