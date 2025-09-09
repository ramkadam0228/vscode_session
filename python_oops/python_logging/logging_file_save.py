import logging
 
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s-%(levelname)s-%(filename)s-%(funcName)s-%(message)s',
                    filename='app.log',
                    filemode='a',
                    force=True)
 
 
def add_numbers(a,b):
    logging.info(f"add numbers a:{a}, b={b}")
    c=a+b
    logging.debug(f"Addition result is: {c}")
    return(c)
 
def subtract_numbers(a,b):
    logging.info(f"add numbers a:{a}, b={b}")
    c=a-b
    logging.debug(f"Addition result is: {c}")
    return(c)
 
class Calculator:
    def __init__(self):
        logging.info("Claculator instance created")
 
    def multiply_numbers(self,a,b):
        logging.info(f"multiply numbers a:{a}, b={b}")
        c=a*b
        logging.debug(f"multiply result is: {c}")
        return(c)
   
    def divide_numbers(self,a,b):
        logging.info(f"divide numbers a:{a}, b={b}")
        try:
            c=a/b
            logging.debug(f"divide result is: {c}")
            return(c)
       
        except ZeroDivisionError:
            logging.error("Attempted divsion by zero",exc_info=True)
            return None
       
 
 
if __name__=="__main__":
    logging.info("Application started")
    add_numbers(10,20)
    subtract_numbers(200,100)
 
    calc=Calculator()
    # calc.divide_numbers(5,0)
    calc.multiply_numbers(6,7)
    calc.divide_numbers(60,70)
    calc.divide_numbers(5,0)
 
    logging.info("Application finished")