from pathlib import Path
import os


#Base Directory
DIRECTORY_PATH = Path.cwd()

# =================== data format ======================
# *collection name *data location * embedded data location * data type
EMPTY_DATA = [] # used for models with no extra path
# controller
CONTROLLER_PATH = DIRECTORY_PATH + r"\data\controller\\"
CONTROLLER_DATA = ["controller",CONTROLLER_PATH,CONTROLLER_PATH+r"db\\","csv" ]
# concordia
CONCORDIA_PATH = DIRECTORY_PATH + r"\data\concordia\\"
CONCORDIA_DATA = ["concordia",CONCORDIA_PATH,CONCORDIA_PATH+r"db\\","pdf" ]
# ai
AI_PATH = DIRECTORY_PATH + r"\data\ai\\"
AI_DATA = ["ai",AI_PATH,AI_PATH+r"db\\","" ]
# general
GENERAL_PATH = DIRECTORY_PATH + r"\data\general\\"
GENERAL_DATA = ["general",GENERAL_PATH,GENERAL_PATH+r"db\\","" ]
if os.system == "Darwin" or os.system == "Linux":
    # controller
    CONTROLLER_PATH = DIRECTORY_PATH + r"/data/controller//"
    CONTROLLER_DATA = ["controller", CONTROLLER_PATH, CONTROLLER_PATH + r"db//", "csv"]
    # concordia
    CONCORDIA_PATH = DIRECTORY_PATH + r"/data/concordia//"
    CONCORDIA_DATA = ["concordia", CONCORDIA_PATH, CONCORDIA_PATH + r"db//","pdf"]
    # ai
    AI_PATH = DIRECTORY_PATH + r"/data/ai//"
    AI_DATA = ["ai", AI_PATH, AI_PATH + r"db//", ""]
    # general
    GENERAL_PATH = DIRECTORY_PATH + r"/data/general//"
    GENERAL_DATA = ["general", GENERAL_PATH, GENERAL_PATH + r"db//", ""]


