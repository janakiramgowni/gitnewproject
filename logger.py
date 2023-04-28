# import logging
#
# import logger
# logging.basicConfig(filename="C://logger//test.log",
#                     format='%(asctime)s:%(level name)s:%(message)s',
#                     datefmt='%m %d %y %I %m:%s:%p')
# logger = logging.getlogger()
# #logger.setlevel(logging.DEBUG)
# logger.debug("this is debug message")
# logger.info("this is info message")
# logger.warning("this is warning message")
# logger.error("this is error message")
# logger.critical("this is critical message")




import logging

import logger
logging.basicConfig(filename="C://logger//test.log",
                    format='%(asctime)s:%(level name)s:%(message)s',
                    level=logging.DEBUG
                    )

logging.debug("this is debug message")
logging.info("this is info message")
logging.warning("this is warning message")
logging.error("this is error message")
logging.critical("this is critical message")