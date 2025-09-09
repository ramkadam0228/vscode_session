""" **Key Word ARGuments, here the value passed ss always a key value pair and becomes a dictionary...
double star indicated key value pair"""
""" *ARGSuments, here the value passed is always a tuple  and becomes a tuple... Single variable means simple list of variables"""
def func1(**kwargs):
    print(kwargs)

def func2(*args):
    print(args)

def func3(*args, **kwargs):
    print(args)
    print(kwargs)

func1(a=1,b=2,c='Ram')
func2(5,6,'Kadam')
func3(100,'pune,mumbai', a=10,b='bombay')
func3(100,['pune','mumbai'], a=10,b='bombay')
func3(100,('pune','mumbai'), a=10,b='bombay')
# func3(100,func2(5,6,'Kadam'), a=10,b='bombay')


