python logging module provides a flexible way to handle logging of applications
it is used to track the events when we run our code
 
Debug: detailed information for diagnosing problem
INFO : Confirmation that things are working as expected
WARNING: An indication that something unexpected happened
ERROR: A serious issue occured, program will stop
CRITICAL: A severor error, but program may continue


Level= logging.INFO - Prints all except Debug
level = logging.DEBUG --> Prints all logging
level=logging.warning --> Warning, error, CRITICAL


SO Hierarchy is like
at top 
DEBUG prints all
INFO
WARNING
ERROR
CARITICAL

========================================
Timeformat
%(asctime) : timestamp when log entered
%(level)s : Level of the log
%(message)s: Meaning ACtual message
---------------------------------------

Critical does not stop processing while error and fatal does !