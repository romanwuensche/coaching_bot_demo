class UI(object):
    config = None
    logger = None
    dbService = None

    def __init__(self, config, dbService, logger):
        self.logger = logger
        self.config = config
        self.dbService = dbService
        self._initRoutes()

    def _initRoutes(self) -> None:
        self.logger.debug('Init UI routes...')

    def start(self) -> None:
        self.dbService.connect()
        self.logger.debug('Starting UI...')
        #flaskApp = Flask(__name__)
        #flaskApp.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
        #flaskApp.run(host="0.0.0.0", debug=True)

    def getUsers(self) -> None:
        self.logger.debug('Fetching users...')
        return self.dbService.findAll(table="users")

    def stop(self):
        self.logger.debug('UI stopped.')