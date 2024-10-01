import logging
import os


class JZLogger(object):

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            level = logging.WARNING
        level_str = os.environ.get("CRS_LOGGING_LEVEL", "WARNING").upper()
        if level_str in logging._nameToLevel:
            level = logging._nameToLevel[level_str]
        formatter = logging.Formatter(
            '[%(asctime)s][%(levelname)s] - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S')
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        cls.instance = logging.getLogger('cruise')
        cls.instance.addHandler(handler)
        cls.instance.setLevel(level)
        cls.instance.propagate = False
        return cls.instance


def get_cruise_logger():
    return JZLogger()


if __name__ == '__main__':
    logger = get_cruise_logger()
    logger.warning('hello world')
