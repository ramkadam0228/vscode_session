# class name need to have brackets while calling it
class args:
    # def __init__(self) -> None:
    #      pass
    def __init__(self, *args, **kwargs):
         self.args=args
         self.kwargs=kwargs
         
    def func1(self):
        print(self.kwargs)

    def func2(self):
        print(self.args)

if __name__ == "__main__":
    #    obj=args()
       args(a=100,b='Cheenai').func1() 
       args(222,'PUNE').func2() 

# print(dir(args))