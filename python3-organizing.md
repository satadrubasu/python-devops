
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
 
 
 ## NOTES MAC- multi python 3 versions :  
 ```
 ==> /usr/local/Cellar/python@3.9/3.9.10/bin/python3 -m ensurepip
==> /usr/local/Cellar/python@3.9/3.9.10/bin/python3 -m pip install -v --no-deps --no-index --upgrade --isolated --target=/usr/local/lib/python3.9/si
==> Caveats
Python has been installed as
  /usr/local/bin/python3

Unversioned symlinks `python`, `python-config`, `pip` etc. pointing to
`python3`, `python3-config`, `pip3` etc., respectively, have been installed into
  /usr/local/opt/python@3.9/libexec/bin

You can install Python packages with
  pip3 install <package>
They will install into the site-package directory
  /usr/local/lib/python3.9/site-packages

tkinter is no longer included with this formula, but it is available separately:
  brew install python-tk@3.9

See: https://docs.brew.sh/Homebrew-and-Python
==> Summary
🍺  /usr/local/Cellar/python@3.9/3.9.10: 3,080 files, 54.9MB
==> Running `brew cleanup python@3.9`...
Removing: /usr/local/Cellar/python@3.9/3.9.7... (3,144 files, 55.3MB)
==> Checking for dependents of upgraded formulae...
==> No broken dependents found!
==> Caveats
==> python@3.8
Python has been installed as
  /usr/local/opt/python@3.8/bin/python3

Unversioned symlinks `python`, `python-config`, `pip` etc. pointing to
`python3`, `python3-config`, `pip3` etc., respectively, have been installed into
  /usr/local/opt/python@3.8/libexec/bin

You can install Python packages with
  /usr/local/opt/python@3.8/bin/pip3 install <package>
They will install into the site-package directory
  /usr/local/lib/python3.8/site-packages

See: https://docs.brew.sh/Homebrew-and-Python

python@3.8 is keg-only, which means it was not symlinked into /usr/local,
because this is an alternate version of another formula.

If you need to have python@3.8 first in your PATH, run:
  echo 'export PATH="/usr/local/opt/python@3.8/bin:$PATH"' >> /Users/satbasu/.bash_profile

For compilers to find python@3.8 you may need to set:
  export LDFLAGS="-L/usr/local/opt/python@3.8/lib"

==> python@3.9
Python has been installed as
  /usr/local/bin/python3

Unversioned symlinks `python`, `python-config`, `pip` etc. pointing to
`python3`, `python3-config`, `pip3` etc., respectively, have been installed into
  /usr/local/opt/python@3.9/libexec/bin

You can install Python packages with
  pip3 install <package>
They will install into the site-package directory
  /usr/local/lib/python3.9/site-packages


 ```
 
