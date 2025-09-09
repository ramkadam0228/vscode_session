"""
create a script5.py
copy the script3.py code in script5.py
at last add if __name__=="__main__"
call script5 here
"""

from script4 import MATH_FUNCTION
from script5 import DATA_READ,DATAFRAME_CREATION
from dotenv import load_dotenv
import os
load_dotenv()

a=os.getenv("A")
b=os.getenv("B")
filename=os.getenv("FILE")
l1=os.getenv("L1")
l2=os.getenv("L2")

MATH_FUNCTION().add(eval(a),eval(b))
df1=DATA_READ().data_read(filename)
df2=DATAFRAME_CREATION().dataframe(l1,l2)
print(df1.shape)
print(df2)