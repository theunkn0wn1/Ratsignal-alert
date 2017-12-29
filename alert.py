__module_name__ = "Alert"
__module_version__ = "0.0.1a"
__module_description__ = "Customizable ratsignal alerts"

# ### alert.py
# Author: Theunkn0wn1
# function: provide means of setting customizable alerts for ratsignals
#   such as for specific platforms / languages

import logging

logging.basicConfig(format="%(levelname)s :%(message)s")
logger = logging.getLogger('alerts')
logger.addHandler(logging.FileHandler("logs/alerts.log", 'w'))
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)

logging.info("logger setup done.")
logging.basicConfig(level=logging.DEBUG)  # write all the things

if __name__ == "__main__":
    pass
