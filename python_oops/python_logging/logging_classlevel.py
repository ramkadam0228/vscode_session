import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s-%(levelname)s-%(filename)s-%(funname)s:%(lineno)d-%(message)s')

def addition(a,b):
    logging.info(f"add numbers a {a} , b {b}")
    c=a+b
    return (c)

def Sub(a,b):
    logging.info(f"Sub numbers a {a} , b {b}")
    c=a-b
    return (c)

def mul(a,b):
    logging.info(f"Multiply numbers a {a} , b {b}")
    c=a*b
    return (c)

def div(a,b):
    if b==0:
        logging.critical("Divide by 0")
    else:
        logging.info(f"Divide numbers a {a} , b {b}")    

    
    c=a/b
    return (c)


if __name__=="__main__":
    logging.info("Application Started")
    addition(10,20)
    Sub(30,5)
    mul(29,2)
    div(5,5)
    logging.info("Application stops")