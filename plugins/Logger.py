import logging


class Logger:
    def __init__(self, debug, file_name):
        self.logger = logging.getLogger('thu-stadium-logger')
        if debug:
            level = logging.DEBUG
        else:
            level = logging.ERROR
        self.logger.setLevel(level)

        fh = logging.FileHandler(file_name)
        fh.setLevel(level)
        ch = logging.StreamHandler()
        ch.setLevel(level)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def log(self, title, contents=list()):
        self.logger.debug(title)
        for content in contents:
            self.logger.debug(content)

    def error(self, title, contents=list()):
        self.logger.error(title)
        for content in contents:
            self.logger.error(content)
