__module_name__ = "Alert"
__module_version__ = "0.0.1a"
__module_description__ = "Customizable ratsignal alerts"

# ### alert.py
# Author: Theunkn0wn1
# function: provide means of setting customizable alerts for ratsignals
#   such as for specific platforms / languages
# ###
import logging
# attempt to import hexchat
try:
    import hexchat
    hex = True
except ImportError:
    hex = False

# utilities imports
from utils.playground.shared_resources import CommandBase, eat_all, Parser, Case

logging.basicConfig(format="%(levelname)s :%(message)s")
logger = logging.getLogger('alerts')
logger.addHandler(logging.FileHandler("logs/alerts.log", 'w'))
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)

logging.info("logger setup done.")
logging.basicConfig(level=logging.DEBUG)  # write all the things

class HelpCommand(CommandBase):
    """
    Command displaying module help
    """
    name = "help"
    alias = ['alertHelp']

    @eat_all
    def func(self, word:list, word_eol:list, userdata=None)->None:
        """
        Help Command
        :param word:
        :param word_eol:
        :param userdata:
        :return:
        """
        print("{name} version {version}".format(name=__module_name__, version=__module_version__))
def init()->None:
    """
    Module init
    :return: None
    """
    commands = [
        HelpCommand,
    ]
    for cmd in commands:
        cmd()

if __name__ == "__main__":
    pass

