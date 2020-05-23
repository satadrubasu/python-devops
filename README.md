

## Some Basic Operators varations

a / b = return floating point  
a // b = return only the integral part ( no rounding off )

## 1.1 Scalar Types ( Basic ) 
1. __int__  
  
  __int as constructor__  
     int(3.5) = 3  ( rounding is always close to 0)  
     int("234") = 243  
  
2. __float__   
   
   3.125  
   3e8  = 3 X 10^8
   1.616e-35 = 1.616 X 10^(-35)
   
   __float as constructor__
   
   float("2.234")
   float("nan")
   
   
3. NoneType  

   a = None  
   > a is None == true  
                               
4. bool

   any integer or float with 0 value is Falsy else Truthy
   
   bool(o)  
   bool(0.0)
   
   any String or collection if empty is considered falsy , else truthy
   
   > bool("")  --> False  
   > bool([])  --> False  
   
   > bool("Some value")  --> True  
   > bool(["one","two"]) --> True  
   > bool("False")   --> True ( as it has value important to keep note)  


 ## 1.2 Relational Operators ( Basic )                                                                                                                                                                                                                                         
                                                
| Relational Operator | Relevance |
|--|--|
|==|value equality / equivalence|
|!=|value inequality / inequivalence|
|<|less-than|
|>|greater-than|
|<=|less-than or equal|
|>=|greater-than or equal|                                                
                                                                                                                                                                                 

## 1.3 While Loops

> while {boolean evaluated expression}:
 
```
   counter = 5
   while counter != 0:
       print(counter)
       counter-=1
```

Using break

```
   while True:
       print("press a number which is multiple of 5 to break and come out from the infinite loop")
       data_in = input()
       if int(data_in) % 5 == 0:
           break
```


## Python Coding Bestpractices - Python Enhancement Proposal (PEP)

Master PEP
> https://www.python.org/dev/peps/

Style Guide
> https://www.python.org/dev/peps/pep-0008/

> Readability counts Satadru