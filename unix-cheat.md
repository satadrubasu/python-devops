## GREP ##

|Description|Command|
|---|---|
|print 2 lines above and 2 lines below after a pattern grep|grep -B 2 -A 2 --color 'keyword' /path/to/file.log|


## SED ##

Note: the sed command prints the contents of the file on terminal by removing the lines.To Remove the lines from the source file itself, use the -i option with sed command.

###  Sed Command to Delete Lines - Based on Pattern Match
 
 * for Mac add     '' -e  ( single quote X 2 )
 > sed -i '' -e "/keyword/d" file.txt

|Description|Command|
|---|---|
|Delete lines that contain a pattern|sed -i '/debian/d' file|
|Delete lines that begin with specified character|sed -i '/^u/d' file|
|Delete lines that end with specified character|sed -i '/x$/d' file|
|Delete lines which are in upper case or capital letters|sed -i '/^[A-Z]*$/d' file|

## AWK ##

https://www.geeksforgeeks.org/awk-command-unixlinux-examples/

|Description| Command|
|---|---|
|Use a custom single char Field Separator(:) and print 3rd column from a file|cat read.txt \| awk -F ':' '{print $3}'|
