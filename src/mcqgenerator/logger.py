import logging
import os
from datetime import datetime
# Logging is created which us basically to know abt the log informations of various we created in python code.
LOG_FILE=f"{datetime.now().strftime('%m_%d_%y_%H_%M_%S')}.log"

# add the log file to the current directory(i.e the directory which we are wirking in vscode)
log_path=os.path.join(os.getcwd(),"logs")
os.makedirs(log_path,exist_ok=True)

# Adding LOG_FILE to log path 
LOG_FILEPATH=os.path.join(log_path,LOG_FILE)


# The logging.INFO will captures all the info and what and all info it will retrieve is you can
#--see from the python logger documentation and in there the functions which is present below the info
#-- that includes logging.WARNING,logging.ERROR,logging.CRICTICAL etc etc details can be retrieved.
logging.basicConfig(
    level=logging.INFO,
    filename=LOG_FILEPATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(messages)s"
)