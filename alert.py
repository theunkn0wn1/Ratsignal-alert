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
from utils.playground.shared_resources import CommandBase, eat_all, Parser, Case, hc

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

class Hooks():
    """
    Hexchat event hooks Hooks and their methods
    """
    # ('hookable', method)
    hooks = [('PRIVMSG')]
    @classmethod
    def on_load(cls)->None:
        """
        Hex event fired when module is loaded
        :return: None
        """
        pass

    @classmethod
    def on_unload(cls)->None:
        """
        Event fired during module unload
        :return:
        """
        pass

    @classmethod
    def on_message(cls, word:list, word_eol:list, userdata:None)->int:
        """
        Event fired when a message is received
        :param word: list of space-deliminated words in event
        :param word_eol: list of space-delimiated words-to-eol
        :param userdata: Custom data, nothing of interest
        :return: 3 # equal to HC.EAT_ALL
        """
        logger.debug("got data {word}".format(word=word))
        data:Case = Parser.parse(data=word)
        if isinstance(data, Case):
            logger.info("Received RATSIGNAL event, got case data!")
            logger.debug("RSIG data: client={client}, plaform={plat}, cr={cr}".format(client=data.client,
                                                                                      plat=data.platform,
                                                                                      cr = data.cr))
        else:
            logger.info("Unknown event data")
            logger.debug("event was of type {} obj = {}".format(type(data), data))
    def __init__(self):
        """
        Init the event hooks
        """
        if hc:
            pass



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

