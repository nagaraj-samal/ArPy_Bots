# import logging
#
# def test_logging():
#         logger = logging.getLogger(__name__)
#         fileHandler = logging.FileHandler('logfile.log')
#         formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
#         fileHandler.setFormatter(formatter)
#
#         logger.addHandler(fileHandler)
#         logger.setLevel(logging.INFO)
#         logger.info("hello")
#         logger.warning("hi")
#         logger.error("err")
#         return logger