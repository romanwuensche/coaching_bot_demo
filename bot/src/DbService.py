import psycopg2

class DbService(object):
    config = None
    logger = None
    connection = None
    cursor = None

    def __init__(self, config, logger):
        self.config = config
        self.logger = logger

    def connect(self) -> None:
        try:
            self.logger.debug("Trying to connect to database...")

            self.connection = psycopg2.connect(
                database=self.config.get('database'),
                user=self.config.get('username'),
                password=self.config.get('password'),
                host=self.config.get('hostname'),
                port=self.config.get('port'),
            )
            self.cursor = self.connection.cursor()

            self.logger.debug("Database connection established!")

        except Exception as e:
            self.logger.debug(e)
            raise ConnectionError("Could not connect to the database. Show log for more details.") from e

    def disconnect(self) -> None:
        self.connection = None
        self.logger.debug('Database connection closed.')

    def _query(self, query, params = []) -> []:
        self.logger.debug('Querying database...')

        cursor = self.cursor
        cursor.execute(query)
        return cursor.fetchall()

    def findAll(self, table, filterParams = []) -> []:
        #sql = 'SELECT * FROM ' + table + ' WHERE :filter'
        sql = 'SELECT * FROM ' + table
        return self._query(sql, params=filterParams)

    def findById(self, id, table) -> []:
        filter = {}
        filter.id = id

        sql = 'SELECT * FROM ' + table + ' WHERE id = :id'

        return self._query(sql, params=filter)

    def remove(self, id, table) -> []:
        sql = 'DELETE FROM ' + table + ' WHERE id = :id'
        return self._query(sql)