import FunctionDemo.Math

res=FunctionDemo.Math.add(10,20)
print(res)

dif=FunctionDemo.Math.sub(30,10)
print(dif)

pr=FunctionDemo.Math.mul(3,9)
print(pr)

import FunctionDemo.Math as mo

res=mo.add(3,4)
print(res)

from FunctionDemo.Math import add,sub

res=add(5,30)
print(res)

from FunctionDemo.Math import * #to import all the functions

flo=flodiv(32,5)
print(flo)
