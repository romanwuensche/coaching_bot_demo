import logging

from src.Bot import Bot
from src.DbService import DbService
from src.UI import UI


class App(object):
    config = None
    logger = None
    dbService = None
    bot = None

    def __init__(self, config):
        self.config = config
        self._init()

    def _init(self) -> None:
        self._initLogger()
        self._initServices()

    def _initLogger(self) -> None:
        logger = logging.getLogger('app')
        logger.setLevel(logging.DEBUG)

        # create console handler with a higher log level
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # create formatter and add it to the handlers
        stream_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        json_formatter = logging.Formatter(
            "{'time':'%(asctime)s', 'name': '%(name)s', 'level': '%(levelname)s', 'message': '%(message)s'}")
        ch.setFormatter(json_formatter)

        # add the handlers to the logger
        logger.addHandler(ch)

        self.logger = logger

    def _initServices(self) -> None:
        config = self.getConfig()
        self.getLogger().debug('Init services...')

        """ Init Database """
        if "DATABASE" in config:
            config = config["DATABASE"]
        else:
            raise Exception("No database configuration submitted. Abort.")

        self.dbService = DbService(config=config, logger=self.getLogger())

    def getConfig(self) :
        return self.config

    def getLogger(self) -> logging.Logger:
        return self.logger

    def getBot(self) -> Bot:
        config = self.getConfig()
        if "BOT" in config:
            config = config["BOT"]
        else:
            raise Exception("No bot configuration submitted. Abort.")

        return Bot(config=config,logger=self.getLogger())

    def getUI(self) -> UI:
        config = self.getConfig()
        if "UI" in config:
            config = config["UI"]
        else:
            raise Exception("No ui configuration submitted. Abort.")

        return UI(config=config, dbService=self.dbService, logger=self.getLogger())

