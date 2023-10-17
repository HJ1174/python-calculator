# python-calculator
# About
This calculator is written in python that does addition, subtraction, division and multiplication. 

# Example Usage
```
> python main.py

Select your calculator operation:                         
1. Addition                        
2. Subtraction                        
3. Multiplication                        
4. Division                        
Other. EXIT()                        

Choice:1

Provide your 2 values:100 200
The result is:300
```

# Test Performed
```

limhongjun@Lims-MacBook-Air python-calculator % pytest -v -cov
===================================================================== test session starts ======================================================================
platform darwin -- Python 3.11.4, pytest-7.4.0, pluggy-1.2.0 -- /Library/Frameworks/Python.framework/Versions/3.11/bin/python3
cachedir: .pytest_cache
rootdir: /Users/limhongjun/Documents/day7/act3/python-calculator
configfile: ov
collected 22 items                                                                                                                                             

test_calculator.py::test_add[-3--2--5] PASSED                                                                                                            [  4%]
test_calculator.py::test_add[-1-0--1] PASSED                                                                                                             [  9%]
test_calculator.py::test_add[1-2-3] PASSED                                                                                                               [ 13%]
test_calculator.py::test_add[3-4-7] PASSED                                                                                                               [ 18%]
test_calculator.py::test_add[-1-1-0] PASSED                                                                                                              [ 22%]
test_calculator.py::test_subtract[-3--1--2] PASSED                                                                                                       [ 27%]
test_calculator.py::test_subtract[-2-0--2] PASSED                                                                                                        [ 31%]
test_calculator.py::test_subtract[0-2--2] PASSED                                                                                                         [ 36%]
test_calculator.py::test_subtract[3--3-6] PASSED                                                                                                         [ 40%]
test_calculator.py::test_subtract[-3-4--7] PASSED                                                                                                        [ 45%]
test_calculator.py::test_multiply[-3--2-6] PASSED                                                                                                        [ 50%]
test_calculator.py::test_multiply[-1-0-0] PASSED                                                                                                         [ 54%]
test_calculator.py::test_multiply[1-2-2] PASSED                                                                                                          [ 59%]
test_calculator.py::test_multiply[3--4--12] PASSED                                                                                                       [ 63%]
test_calculator.py::test_multiply[0-0-0] PASSED                                                                                                          [ 68%]
test_calculator.py::test_multiply[-2-4--8] PASSED                                                                                                        [ 72%]
test_calculator.py::test_divide[-4--2-2] PASSED                                                                                                          [ 77%]
test_calculator.py::test_divide[-1-0-Cannot divide by zero] PASSED                                                                                       [ 81%]
test_calculator.py::test_divide[1-2-0.5] PASSED                                                                                                          [ 86%]
test_calculator.py::test_divide[3--4--0.75] PASSED                                                                                                       [ 90%]
test_calculator.py::test_divide[0--1-0] PASSED                                                                                                           [ 95%]
test_calculator.py::test_powerof PASSED                                                                                                                  [100%]

====================================================================== 22 passed in 0.01s ======================================================================


```
