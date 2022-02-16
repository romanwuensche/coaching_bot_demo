import configparser
import sys

from src.App import App

if __name__ == "__main__":
    try:
        """ Init Application """
        config = configparser.ConfigParser()
        config.read("default.config.txt")

        app = App(config)

        try:
            """ Init UI """
            ui = app.getUI()
            ui.start()
            users = ui.getUsers()

            for user in users:
                print(user)

        except Exception as e:
            app.getLogger().error(str(e))
            raise e

    except Exception as e:
        print(e)
        sys.exit(1)
