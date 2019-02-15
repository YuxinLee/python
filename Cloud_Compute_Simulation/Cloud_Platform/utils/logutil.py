import logging.config


def get_logger(level):
    return Log(level)


class Log:

    def __init__(self, level):
        ''
        self.level = level
        logging.config.fileConfig('./conf/logging.ini')
        self.info_log = logging.getLogger('infoLogger')
        self.warn_log = logging.getLogger('warnLogger')
        self.error_log = logging.getLogger('errorLogger')

    def info(self, msg, *args, **kwargs):
        self.info_log.info(msg, *args, **kwargs)

    def warn(self, msg, *args, **kwargs):
        self.info_log.warn(msg, *args, **kwargs)
        self.warn_log.warn(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        self.info_log.error(msg, *args, **kwargs)
        self.warn_log.error(msg, *args, **kwargs)
        self.error_log.error(msg, *args, **kwargs)
