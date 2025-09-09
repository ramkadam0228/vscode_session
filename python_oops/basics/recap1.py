class MATH_FUNCTION:
 
    def add(self,a,b):
        return(a+b)
 
    def mul(self,a,b):
        return(a*b)
    


class utils:
        def creat_a_file(self, file_name):
            # file_name="dummy.txt"    
            with open(file_name,mode='w') as file:
                file.write("hello good morning")

if __name__=="__main__" :
    ans1=MATH_FUNCTION().add(10,20)
    ans2=MATH_FUNCTION().mul(30,40)
    print("Addition:",ans1)
    print("multiplication:",ans2)
    utils().creat_a_file('dummy.txt')

    """
if we write the function under main
we can run this recap1.py so that we can see answers
also we can use recap1.py in another python file
at that time the answers in this file will not run again
if __name__=="__main__" we should write onetime
all the classes under this..

If we dont write this statement
"""