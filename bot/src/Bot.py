class Bot(object):
    config = None
    logger = None

    def __init__(self, config, logger):
        self.logger = logger
        self.config = config

    def start(self) -> None:
        self.logger.debug('Bot started.')
        self.logger.debug('  API KEY: ' + self.config["telegram_api_key"])

    def listen(self) -> None:
        try:
            self.logger.debug('  Waiting for input... CTRL-C to interrupt.')
        except Exception as e:
            raise Exception('There was an error during listing. Abort.') from e

    def stop(self):
        self.logger.debug('Bot stopped.')