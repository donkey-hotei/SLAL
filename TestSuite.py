"""
Test Suite for debuggin'
"""
from vector import *
from matrix import Matrix

def tst(exp):
    if exp == True: return "Success"
    else: return "Fail"

def runVectorTests():
    print("Running Vector Test Suite...")
    v = Vector({'a','b','c', 'd'},{'a':2,'c':1,'d':3})
    print(v)
    print("Testing getter function ... ", end = '')
    print(tst(v['a'] == 2 and v['b'] == 0))
    
    v['b'] = 3
    print(v)
    print("Testing setter function ... ", end = '')
    print(tst(v['b'] == 3))
    
    print("Testing vector negation ... ", end = '')
    print(tst(-v == Vector({'a','b','c','d'}, {'a':-2, 'b':-3, 'c':-1, 'd':-3})))
    
    v = Vector({c for c in 'abcd'}, {'a':2, 'b':4, 'c':6, 'd':8})
    print("Testing scalar multiplcation ... ", end = '')
    print(tst(2 * v == Vector({'a','b','c','d'}, {'a': 4, 'b':8, 'c':12, 'd':16})))

    # test for __mul__
    # what is the difference between one vecvtor and another ??? 
if __name__ == '__main__':
    runVectorTests()
    
