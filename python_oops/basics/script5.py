
import pandas as pd
# from script2 import MATH_FUNCTION
# obj1=MATH_FUNCTION
# print(dir(obj1))


class DATAFRAME_CREATION:
    def dataframe(self,list1,list2):
        # list1=[1,2,3,4]
        # list2=['A','B','C']
        df1=pd.DataFrame(zip(list1,list2))
        return(df1)
   
class DATA_READ:
    def data_read(self, filename):
        df2=pd.read_csv(filename)
        return(df2)
 


if __name__=="__main__":
    df1=DATAFRAME_CREATION().dataframe()
    df2=DATA_READ().data_read()
    print(df1)
    print(df2.shape)
