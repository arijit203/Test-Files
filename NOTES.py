'''
import time
print(time.time())
a=time.time();print(sum(list(range(1000n))));b=time.time()
print(b-a) ## denotes the time required for the operation
'''
def sum(n):
    if n<=0:
        return n
    else:
        return n+sum(n-1)
print(sum(100000))    
##maximum recursion depth exceeded(generally max.recursion depth is 999)
##but recursion depth can be increased using the sys module
##import calender---calender.month(<Year>,<Month>)
                ##---calender.calender(<year>)

'''
import random
random.random()---returns random floating point no. 0<=  <=1
random.randrange(no1,no2.,step)-----no. is exlusive but gives random int.no upto no2. but no1 is inclusive
random.randint(no1,no2) both boundaries inclusive ;2 arguments needed in ()
random.uniform(a,b) ---- floating point no. a<=  <=b wher a<=b orr b<=  <=a wher b<=a
