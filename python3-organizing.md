
##  Package Management in python

 __Module Definition :__   
   - Normally a single Python source file.  
   - Load Modules with import  
   - Represented by module objects.  

# Table of contents
1. [Nesting Modules with packages](#chap_01)  
    1. PYTHONPATH
2. [Implementing Packages](#chap_02)  
    
3. [Namespace and Executable Packages](#chap_03)  

4. [Recommended Package Layout](#wrapper)  
 
5. [Package Distribution](#wrapper)  

    
    
## 1. Nesting Modules with packages <a name="chap_01"></a>  

__Package Definition :__
  - Special type of module  
  - contains other modules and packages meaning hierarchy of modules  
  - sys.path is a list of directories  
  - package dir paths are stored in __path__  

   package[dir]-->module.py  
  
### 1.1 PYTHONPATH
   - Env Variable   
      Windows : set PYTHONPATH=path1;path2  
      UNIX    : export PYTHONPATH=path1:path2  
   - List of paths added to sys.path 
   
   - Use case where we have created sub folders in our python project

## 2 Implementing Packages  <a name="chap_02"></a>

  - Create a root directory ( which was be imported in the sys.path )  
  - create a special file \__init__.py ( it can be empty ) [ optional for 3.3+ ]  
 
 > refer to example : demo_reader with nested packages / modules / classes

Running Code #1 and understand the flow:  

 > python -m <Fully Qualified Module Name> sys.argv[1]  sys.argv[n]..  
 > pythom -m demo_reader.compressed.bzipped test.bz2 data compressed with bz2  

### 2.1 Relative Imports within the same package only 

 Relative Imports within the same package:
   > from ..module_name import name


#### 2.1 Projects and VirtualEnvs

## 3. VENVWRAPPER  <a name="wrapper"></a>  
 
   - User firndly wrapper of virtualenv
   - Bind projects with virtualenv