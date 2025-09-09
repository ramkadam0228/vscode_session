import logging

logging.basicConfig(level=logging.ERROR)

a=5
logging.debug("This is Debugging")
logging.info("This is Info")
logging.warning("This is Warning")
logging.error("This is error")
logging.critical(f"This is critical {a}")