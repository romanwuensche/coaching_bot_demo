import argparse
import configparser
import sys

from src.App import App

if __name__ == "__main__":
    try:
        """ Parse CLI arguments """
        """
        parser = argparse.ArgumentParser(description='Arguments...')
        parser.add_argument('-k', '--telegram-api-key', required=False, action='store', default='INSERT_YOUR_KEY_HERE',
                            help='Telegram api key')
        parser.add_argument('-d', '--debug', required=False, type=bool, action='store', help='Enable debug mode')
        args = parser.parse_args()
        """

        """ Init Application """
        config = configparser.ConfigParser()
        config.read("default.config.txt")

        app = App(config)

        try:
            """ Init Bot """
            bot = app.getBot()
            bot.start()
            bot.listen()
            bot.stop()
        except Exception as e:
            app.getLogger().error(str(e))
            raise e

    except Exception as e:
        print(e)
        sys.exit(1)
