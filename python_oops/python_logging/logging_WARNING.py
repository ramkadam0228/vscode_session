import logging

logging.basicConfig(level=logging.WARNING)

a=5
logging.debug("This is Debugging")
logging.info("This is Info")
logging.warning("This is Warning")
logging.error("This is error")
logging.critical(f"This is critical {a}")


logging.basicConfig(level=logging.WARN)

a=5
logging.debug("This is Debugging")
logging.info("This is Info")
logging.warning("This is Warning")
logging.error("This is error")
logging.critical(f"This is critical {a}")

# WARN and WARNING are same