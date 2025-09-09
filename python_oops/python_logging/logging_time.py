import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s-%(levelname)s-%(message)s')
#format='%(asctime)s-%(levelname)s-%(filenae)s-%(message)s'

a=5
logging.debug("This is Debugging")
logging.info("This is Info")
logging.warning("This is Warning")
logging.error("This is error")
logging.critical(f"This is critical {a}")



import logging
# format='%(asctime)s-%(levelname)s-%(message)s'
# format='%(asctime)s-%(levelname)s-%(filename)s:%(lineno)d-%(message)s'
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s-%(levelname)s-%(filename)s:%(lineno)d-%(message)s')
 
# log messages
logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error('this is an error message')
logging.critical("this is a critical message")
 
# INFO:root:This is an info message
# WARNING:root:This is a warning message
# ERROR:root:this is an error message
# CRITICAL:root:this is a critical message