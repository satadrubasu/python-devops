
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
        1.[String concatenation via join() best practice](#collections_str_join)  
        2.[String split via partition() best practice](#collections_str_part)  
        3.[String format() usage](#collections_str_format)  
        4.[String format f-strings usage](#collections_str_fstring)  
    2. [Lists](#collections_list)  
        1.[Slicing a list](#collections_list_slice)  
    3. [Dict](#collections_dict)  
    4. [For-loop](#collections_for)  
        1. [enumerate](#collections_for_enum)  
    5. [tuple](#collections_tuple)  
    6. [range](#collections_range)  
    7. [set](#collections_set)  
3. [Modularity](#modular)  
    1. [def Functions](#modular_func)  
    2. [\__name\__](#modular_name)  
    3. [sys.argv[]](#modular_cmd)  
    4. [docstring](#modular_doc)  
    5. [shebang](#modular_shbang)  
4. [Object and Types](#object)  
    1. [arguments and return](#object_args)  
    2. [Function arguments](#object_func)  
    3. [Type Check](#object_type)  
    4. [Scopes](#object_scope)  


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
  
  #### 2.1.1 Strings with Newlines   
  
   - __Multiline Strings:__  
    
    ```  
    """  
    A multiline string  
    Starting and ending with triple quotes   
    Single Or Double  
    """    
    ```   
   
   #### 2.1.2 Escape Sequences   
  
   ( \n is universtal to all platforms)  
       \r for windows not needed  
     
   #### 2.1.3 Raw Strings for Regex:   
    
   If multiple \ used , python supports raw string which doesnt support any escape.  
     Begin with a r.With this kind of initialization the variable automatically added the \.  
     
     ```
     variable_path = r'D:\Program~1\'  
     ```
   #### 2.1.4 Strings Concatenation <a name="collections_str_join"></a>  
   
   * str.join() much more memory eficient than +  
   * the joined object acts as separator  
   > ';'.join(["fname","mname","lname"])     
      results in   : fname;mname,lname     
    
   * We can use the '' empty string to perform normal concatenations  
   
   #### 2.1.5 Strings Split with partition() <a name="collections_str_part"></a>  
   
   * partition() returns tuple  
   > "unforgetable".parition('forget')   
      results in   : ('un','forget','able')    
    
      
   #### 2.1.6 Strings format <a name="collections_str_format"></a>  
   
   * Positional parameters to format  
   > "My first name is {0} , and last name is {1}".format('Satadru','Basu')     

   * Keyword parameters  
   > "My first name is {fname} , and last name is {lname}".format(fname="Satadru",lname="Basu")   
        
   #### 2.1.7 Strings f-string <a name="collections_str_fstring"></a>  
   
   * Evaluate Expressions and embed in the string , including calling a function  
   > f'Current time is {datetime.datetime.now().isoformat()}.'    

   * Keyword parameters  
   > "My first name is {fname} , and last name is {lname}".format(fname="Satadru",lname="Basu")  
    
### 2.2 Lists ( Heterogeous content ) <a name="collections_list"></a>  

* slicedList = list[sliceStart:sliceEnd]  
* slicedList = list[1:]   
* slicedList = list[:5]  
* slicedList = list[:]   
* list.reverse() AND list.sort()  

* use copy module for deep copy of nested collections.  

* remove an element from list  
> del list[3]  
* insert an element from list  
> del list[3]  

### 2.3 dict ( Heterogeous content ) <a name="collections_dict"></a>  

    my_dict = {}
    
* dest_dict.update(sourceDict)  
* looping through dict : dict.items()  

 ```
    for key in colors:   
        print(f"{key} => {colors[key]}")  

    for key,value in colors:   
        print(f"{key} => {value}")  
 ```
* "red" in colors_dict  
* "blue" not in colors_dict  
* del colors_dict['blue']  
    
### 2.4 for-loop ( Heterogeous content ) <a name="collections_for"></a>  

   ```
   inventory = {"car":"ciaz","phone":"nokia","laptop":"mac","salary":00,"comments":"dont take these seriously"}  
   for item in inventory:  
       print(item,inventory[item])  
   ```

   #### 2.4.1 enumerate to help with index , value in a collection <a name="collections_for_enum"></a>  
   ```
     mylist = [11,22,33,44,55]  
     for item in enumerate(mylist):  
         print(item)  
   ```
   
   * Using tuple unpackin on the go  
      
   ```
     mylist = [11,22,33,44,55]  
     for i,v in enumerate(mylist):  
         print(f"index = {i} , value = {v}")  
   ```
### 2.5 Tuple <a name="collections_tuple"></a>  

> t = ("Pune",1.234,5)  

* Immutable sequences of arb objects once initialized can't be change   
* tuples can be added or multipled :  
   t + ("London",1.00,3)  
   t * 8  
* tuples can be nested - good for multi dimensional matrix  
  > t = ((101,102),(201,202),(301,302),(401,402))  
  > t[2][2]  
* tuple complex initializations  
  > (a,(b,(c,d))) = (4,(3,(2,1)))  
* tuple swap  
  > a,b = b,a  
* tuple constructor  
  > tuple([11,22,33,44])  
* Check for containment  
  > 5 in (3,5,6,7)  
                
### 2.6 Range <a name="collections_range"></a>  

* generally used as counters  
* range(stop)  OR range(start,stop)  OR range(start,stop,step)     
> range(5)  = 0 to 4  
> list(range(5,10))      = [5, 6, 7, 8, 9]  
> list(range(1,21,3))    = [1, 4, 7, 10, 13, 16, 19] 


### 2.7 Set <a name="collections_set"></a>  

* Set is unordered and Initialization like dict has {}    
 > python_coders = {'satbasu','goku',krillin'}  

* Note {} empty initializes a dict so need to use a set constructor for empty ones.  
 > java_coders = set()     
 > shell_coders = set(["goku","gohan","trunks","satbasu"])   
 > java_coders.add("satbasu")  
 > java_coders.update(["goku","gohan"])  

* Set Algebras  

  ```
   java_coders.intersection(shell_coders)  
   java_coders.intersection(shell_coders) == java_coders.intersection(python_coders)  
   java_coders.difference(shell_coders)  

  ```


##  3 Modularity in Python <a name="modular"></a>  

  If we import a python file without functions , just during import statement it executes the entire File.Hence the need of functions.  
  
  \__feature\__ is called dunder : double underscore  
  
   
  Source code files called modules - A module is executed once on first import.  
  Python Arguments - sys.argv ( parameters)  
  Making programs executable using (\__name\__ == \__main\__ )  
  docstring used in help(Object name)  

###  3.1 Defining functions  <a name="modular_func"></a>  

Ideal not to print but return some value.  
```
def cube(x):  
    return x*x*x  
```

###  3.2 \__Name\__ <a name="modular_name"></a>  
 dunder name : Special variable allows to detect whether a module is run as a script or imported into another module.  
 
 print(\__name\__) behaviour :  
 |When|Output|  
 |---|---|  
 |import sample|sample|  
 |import sample|No output as sample was already imported and printed the module name on  first time|  
 |python sample.py|\__main\__|  
 
 
 So to ensure flow of code when a python script is executed from shell python <scriptname.py>  
 ```
  if __name__ == '__main__':  
      fetch_workds()  
 ```
 
###  3.3 Python Command line Model <a name="modular_cmd"></a>  
 Refer to samply.py for reference  
  
   ```
   if __name__ == '__main__':
    ## run this program with sample.py https://raw.githubusercontent.com/satadrubasu/Unix-PythonReference/master/resources/sample.txt  
    ## From SHELL : python sample.py  
    ## From REPL : import sample  
    ## From REPL : main('https://raw.githubusercontent.com/satadrubasu/Unix-PythonReference/master/resources/sample.txt')
    main(sys.argv[1])  
   ```

###  3.4 Python docstrings <a name="modular_doc"></a>  
 
* The first line of a block ( function / module / class ) to have comments in triple double quotes  
* Tool like Sphinx to create HTML documentation from python docstrings  
* see help in interpreter :    
     > from sample import \*  
 
     > help(fetch_words)  
     

   ```
    """ 
     def fetch_words(url):   
     Fetchs list of words , read from a passed URL.  

        Args:  
            url: The URL of a UTF-8 text Document  

        Returns:  
            List of strings containing the words from the document.  
    """  
   ```  
###  3.5 Python SHEBANG <a name="modular_shbang"></a>  

* Locate Python Using PATH : #!/usr/bin/env python3  

## 4 Object and Types  <a name="object"></a>  

* Python Object Model ( same Garbage collection as Java)  

* Named references to objects  

  ```
     Mutable Objects  
     r = [11,22,33]   
     s = r    # s is a new name pointing to same objet as r  
     s[1] = 17  # change to s = change to r  
     s is r == True  
   ```

* Value equality vs identity equality  
   ```  
    p = [11,22]  
    q = [11,22]  
    p == q     ( Value Equality )  
       True       
    p is q      ( id equality )  
       False  
   ```  
* Passing args and returning values  
* Pythons type sysmtem  
* scope to limit name access  
* Evertything is an Object    
   Even int is an immutable object so changing value , keeps the old value floating till GC  
   
> id()  --> returns a unique int identifier constant for the lifetime of an value object.  


### 4.1 Argument Passing and return <a name="object_arg"></a>  

#### 4.1.1 Arguments ( Function arguments are pass by object reference )    
 
Mutable Objects passes a reference and hence the original object also changes in the following example.
m will reflect the new value added. Note since we are using the append()
   
   ```
   m = [11,5,12]  
   def modify(k):  
       k.append(33)  
       print("k = ", k)  

   modify(m)  
   m = [11,5,12,33]   
   ```

Note the following variant of the above example where the variable is altogether assigned to a new list.
By the core concept , the k is now pointing to a new value object reference.While the calling object m points to the original list.This results in m continue to point to its old data.
   
   ```
   m = [11,5,12]  
   def modify(k):  
       k = [44,55,66,77]  
       print("k = ", k)  

   modify(m)  
   m = [11,5,12]  
   ```  


#### 4.1.2 Return objects ( object reference semantics )  

   ```
   m = [11,5,12]  
   def function_my(k):  
       return k  

   p = function_my(k)  
   p is m   
    True  
   ```

### 4.2 Default Argument values in Functions ( ones with defaults shud come after the non defaults) <a name="object_func"></a>  
   positional arguments and keyword arguments ( with keys)  
    city - is a keyword argument and is optional and non -positional.  
    
   Always use immutable default values , else when its called without the pramas , it initializes once during def and keeps working on it.  
   
```
   def labelled_msg(msg,separator='-'):  
       seperator_line = separator * len(msg)  
       print(seperator_line)  
       print(msg)  
       print(seperator_line)  
       
   labelled_msg("Positional Parameter")  
   labelled_msg("Positional Parameter",separator="#")  
   ```

### 4.3 Type System in python <a name="object_type"></a>  

 No Type declarations are needed in python.    
 
 |command| response|  
 |---|---|  
 | type(sample) | class 'module' |  
 | type(32) | class 'int' |  
 | type(32) | class 'int' |    
 |dir(sample)|all attributes inclusive of the module and what we defined|  
 |type(sample.print_items)|all attributes inclusive of the module and what we defined|  
 
### 4.4 Scopes / namespaces in python <a name="object_scope"></a>  


* Scopes in python do not correspond to source code blocks by indentation  
* global <variable>  -- refers to outer namespace of the same variable name and not the local.  

|Scope order|SHort|Scope|Description|  
|---|---|---|---|  
|Narrowest|L|Local|Inside the current function|  
|Narrower|E|Enclosing|Inside Enclosing functions|  
|Broader|B|Global|Top level of module|  
|Boradest|G|Built-in|In the special built in modules|  
