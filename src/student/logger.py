import logging
import os
from datetime import datetime

now=datetime.now()

file_name=f"{now.date()}.log"
file_path="LOGS"
os.makedirs(file_path,exist_ok=True)

log_path=os.path.join(file_path,file_name)

logging.basicConfig(
    filename=log_path,
    format="[%(asctime)s] %(module)s-%(lineno)d- %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
