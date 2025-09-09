# class name need to have brackets while calling it
class args:
    # def __init__(self) -> None:
    #      pass
    # def __init__(self,):
    #      pass
    def func1(self,**kwargs):
        print(kwargs)

    def func2(self,*args):
        print(args)

if __name__ == "__main__":
       obj=args()
       obj.func1(a=100,b='Cheenai') 

print(dir(args))