import configparser


config = configparser.RawConfigParser()

config.read(".\\configData.ini")


class ReadConfig:

    @staticmethod
    def getUrl():
        url = config.get("common value", "url")
        return url


