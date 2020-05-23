
## Python Coding Bestpractices - Python Enhancement Proposal (PEP)

Master PEP
> https://www.python.org/dev/peps/

Style Guide
> https://www.python.org/dev/peps/pep-0008/  
Readability counts

# Table of contents
1. [Basic Elements](#basicElements)  
    1.[Types](#basicElements_types)  
    2.[Relational Operators](#basicElements_relational)
    3.[While loop](#basicElements_while)  
2. [String,Collections,for-loop](#collections)
    1. [String - immutable](#collections_str)
    2. [Lists](#collections_list)
    3. [Dict](#collections_dict)
    4. [For-loop](#collections_for)
3. [Modularity](#modular)
    1. [replace](#modular_)
    2. [replace](#modular_)
    3. [replace](#modular_)
    4. [replace](#modular_)
    5. [replace](#modular_)
    

## Some Basic Operators varations <a name="basicElements"></a>

a / b = return floating point  
a // b = return only the integral part ( no rounding off )

## 1.1 Scalar Types ( Basic ) <a name="basicElements_types"></a>
1. __int__  
  
  __int as constructor__  
     
     ```
     int(3.5) = 3  ( rounding is always close to 0)   
     int("234") = 243
     ```  
  
2. __float__   
   
   ```
   3.125  
   3e8  = 3 X 10^8
   1.616e-35 = 1.616 X 10^(-35)
   ```
   __float as constructor__
   
   ```
   float("2.234")
   float("nan")
   ```
   
3. NoneType  

   a = None  
   > a is None == true  
                               
4. bool ( Constructor Usages)
   a = True
   a = False
   
   
   ```
   Any integer or float with 0 value is Falsy else Truthy
     bool(0)  --> False
     bool(0.0)  --> False
   
     bool("")  --> False  
     bool([])  --> False  
   
   Any String or collection if empty is considered falsy , else truthy
     bool("Some value")  --> True  
     bool(["one","two"]) --> True  
     bool("False")   --> True ( as it has value important to keep note)
   ```


## 1.2 Relational Operators ( Basic )   <a name="basicElements_relational"></a>                                                                                                                                                                                                                                       
                                                
| Relational Operator | Relevance |
|--|--|
|==|value equality / equivalence|
|!=|value inequality / inequivalence|
|<|less-than|
|>|greater-than|
|<=|less-than or equal|
|>=|greater-than or equal|                                                
                                                                                                                                                                                 

## 1.3 While Loops  <a name="basicElements_while"></a>

 while {boolean evaluated expression}:
 
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

## 2. String, Collections and Iterations <a name="collections"></a>

   1. str
   2. list 
   3. dictionary
   
   4. for-loop

### 2.1 str ( String Literals) ( Is Unicode UTF-8 supports all languages ) <a name="collections_str"></a>

   Key Note : String are immutable in python too. So to capitalize a variable you have to catch the return.
   ```
   name = 'satadru'
   capitalized_name = name.capitalize()
   print(name)               --> satadru
   print(capitalized_name)   --> Satadru
   ```
  
   2.1.1 Strings with Newlines  
  
   - __Multiline Strings:__
    
    ```
    """
    A multiline string
    Starting and ending with triple quotes 
    Single Or Double
    """   
    ```   
        
   - __Escape Sequences:__   
     ( \n is universtal to all platforms)  
      \r for windows not needed
     
   - __Raw Strings for Regex:__   
     If multiple \ used , python supports raw string which doesnt support any escape.
     Begin with a r.With this kind of initialization the variable automatically added the \.
     
     ```
     variable_path = r'D:\Program~1\'
     ```
   
### 2.2 Lists ( Heterogeous content ) <a name="collections_list"></a>


### 2.3 dict ( Heterogeous content ) <a name="collections_dict"></a>

    my_dict = {}
    
### 2.4 for-loop ( Heterogeous content ) <a name="collections_for"></a>

   ```
   inventory = {"car":"ciaz","phone":"nokia","laptop":"mac","salary":00,"comments":"dont take these seriously"}
   for item in inventory:
       print(item,inventory[item])
   ```

##  3 Modularity in Python <a name="modular"></a>

  Reusable Functions  
  Source code files called modules  
  Modules used from other modules  
  Python Execution model ( parameters)  
  Making programs executable    

###  3.1 Modularity in Python <a name="modular_"></a>
###  3.2 Modularity in Python <a name="modular_"></a>
###  3.3 Modularity in Python <a name="modular_"></a>
###  3.4 Modularity in Python <a name="modular_"></a>