import logging

class BaseClass:

        def getLogger(self):
            logger = logging.getLogger(__name__)
            # if not logger.handlers:
            fileHandler = logging.FileHandler('logfile.log')
            formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
            fileHandler.setFormatter(formatter)

            logger.addHandler(fileHandler)
            logger.setLevel(logging.INFO)
            #logger.info("hello")
            #logger.warning("hi")
            return logger